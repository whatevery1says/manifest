"""validate.py.

Validates a WE1S manifest schema. Arguments can be file paths, urls, or dicts.

Usage:

python validate.py PATH_TO_SCHEMA PATH_TO_DATA
"""

# Python imports
import argparse
import json
import jsonschema
import requests
from jsonschema import Draft7Validator, FormatChecker, validate

# Validator class
class Validator():
    """Validate a manifest."""

    def __init__(self, schema, data):
        """Instantiate the object."""
        self.schema = self._load_json(schema)
        self.data = self._load_json(data)

    def _load_json(self, path):
        """Load json from dict, url, or filepath."""
        if isinstance(path, dict):
                return path
        elif path.startswith('http'):
            try:
                return requests.get(path).json()
            except:
                print('Cannot find file at the designated location.')
                return None
        else:
            try:
                return json.loads(open(path).read())
            except IOError:
                print('Cannot find file at the designated location.')
                return None

    def validate(self):
        """Validate the data."""
        if self.data:
            try:
                validate(self.data, self.schema, format_checker=FormatChecker())
                print('Document is valid.')
            except jsonschema.exceptions.ValidationError as err:
                print('Document is not valid.')
                print('Error(s):\n')
                validator = Draft7Validator(self.schema)
                for error in sorted(validator.iter_errors(err), key=str):
                    print(f'- Error: {error.message}.')
        else:
            print('No data was loaded into the validator. Please check your filepath.')

def main(args=None):
    """Perform the validation."""
    # Read the CLI args
    if args:
        schema = args.schema
        data = args.data
    # Validate
    validator = Validator(schema, data)
    validator.validate()

if __name__ == '__main__':
    # Parse the CLI
    parser = argparse.ArgumentParser(description='Validate a WE1S manifest.')
    parser.add_argument('schema',
                        help='Path to the manifest JSON Schema file.')
    parser.add_argument('data',
                        help='Path to the JSON data file to be validated.')
    args = parser.parse_args()
    main(args)
