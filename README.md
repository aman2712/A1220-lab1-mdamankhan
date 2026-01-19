# Receipt Data Extractor

The program analyzes the content of receipts present inside a receipt folder and returns
an object with `date`, `amount`, `vendor`, `category` attributes for each receipt.

### How to run

Make sure to run export OPENAI_API_KEY="your_api_key" to set the API KEY in the environment variable.

Make sure to create a receipts folder in the root of the directory, with the necessary receipt images inside of it

```
source venv/bin/activate
```

This activates the virtual environment

```
pip install -r requirements.txt
```

To install all the required packages

```
make
```

To use the makefile to run the given program
