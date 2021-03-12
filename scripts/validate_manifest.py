"""validate_manifest.py.

Usage Example:

schema = 'https://raw.githubusercontent.com/whatevery1says/manifest/master/schema/v2.0/Corpus/Data.json'
manifest = 'https://raw.githubusercontent.com/whatevery1says/manifest/master/examples/Data_sample.json'
validation = Validation(schema)
validation.is_valid(manifest)
"""

# Python imports
import json
import requests
from jsonschema import validate, FormatChecker

# Validation class
class Validation():
    """Validate a manifest according to a schema."""

    def __init__(self, schema):
        """Instantiate the Validation object.

        Takes as input a filepath or url to a json schema doc,
        or a dict in json schema format.
        """
        self.schema_path = schema
        self.schema = self.load_schema()

    def load_json(self, path, type='schema'):
        """Load json from url or file."""
        if isinstance(path, dict):
            return path
        elif path.startswith('http'):
            try:
                return requests.get(path).json()
            except:
                print(f'Cannot find {type} at the designated location.')
                return {}
        else:
            try:
                with open(path) as f:
                    doc = json.loads(f.read())
                return doc
            except IOError:
                print(f'Cannot find {type} at the designated location.')
                return {}

    def load_manifest(self, path):
        """Load manifest from url or file."""
        return self.load_json(path, type='manifest')

    def load_schema(self):
        """Load schema from url or file."""
        return self.load_json(self.schema_path, type='schema')

    def is_valid(self, path):
        """Validate the manifest and return a Boolean or raise an error."""
        manifest = self.load_manifest(path)
        validate(manifest, self.schema, format_checker=FormatChecker())
        return True
