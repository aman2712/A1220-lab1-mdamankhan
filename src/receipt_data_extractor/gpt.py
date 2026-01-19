# gpt.py
import json
from openai import OpenAI

CATEGORIES = ["Meals", "Transport", "Lodging", "Office Supplies", 
"Entertainment", "Other"]

def normalize_amount_field(data):
    """Normalize the amount field to a float without a dollar symbol.

    Args:
        data: A dict containing receipt fields, including the amount key.

    Returns:
        The same dict with the amount converted to float when possible.

    Assumptions:
        The amount is either numeric, a numeric string, or a numeric string
        prefixed with "$".
    """
    if not isinstance(data, dict):
        return data

    amount = data.get("amount")
    if amount is None:
        return data

    if isinstance(amount, (int, float)):
        data["amount"] = float(amount)
        return data

    if isinstance(amount, str):
        cleaned = amount.replace("$", "").strip()
        try:
            data["amount"] = float(cleaned)
        except ValueError:
            pass

    return data

def extract_receipt_info(image_b64):
    """Extract receipt fields from a base64-encoded image via OpenAI.
    Args:
        image_b64: Base64-encoded JPEG image string without data URI prefix.
    Returns:
        A dict with keys: date, amount, vendor, category.
    Assumptions:
        The OpenAI client is configured and the model returns valid JSON.
    """
    client = OpenAI()
    prompt = f"""
You are an information extraction system.
Extract ONLY the following fields from the receipt image:

date: the receipt date as a string
amount: the total amount paid as it appears on the receipt
vendor: the merchant or vendor name
category: one of [{", ".join(CATEGORIES)}]

Return EXACTLY one JSON object with these four keys and NOTHING ELSE.
Do not include explanations, comments, or formatting.
Do not wrap the JSON in markdown.
If a field cannot be determined, use null.

The output must be valid JSON.
"""
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        seed=43,
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{image_b64}"
                        }
                    }
                ]
            }
        ]
    )
    data = json.loads(response.choices[0].message.content)
    return normalize_amount_field(data)
