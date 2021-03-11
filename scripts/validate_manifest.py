## Imports
import requests, json
from jsonschema import validate, FormatChecker

## Configure from list of manifest_types below
manifest_file = 'https://raw.githubusercontent.com/whatevery1says/manifest/master/schema/Publications/sample.json'
manifest_type = 'Publications/Publications'

# These variables only rarely need to be modifed
manifest_types = ['Publications/Publications', 'Corpus/collection', 'Corpus/RawData', 'Corpus/ProcessedData', 'Corpus/Metadata', 'Corpus/Outputs', 'Corpus/Related', 'Corpus/Data', 'Corpus/PathNode', 'Processes/Processes', 'Processes/Step', 'Scripts/Scripts', 'Project/Project']
unavailable = ['Processes/Processes', 'Processes/Step', 'Scripts/Scripts', 'Project/Project']

## Do not edit below this line

# Read the schema file
url = 'https://raw.githubusercontent.com/whatevery1says/manifest/master/schema/'
schema_file = url + manifest_type + '.json'
schema = requests.get(schema_file).text
# print(schema)
schema = json.loads(schema)

# Read the manifest file
with open(manifest_file) as f:
    manifest = f.read()

def valid(manifest, schema):
    # Wrapper to return feedback if the manifest is valid
    validate(manifest, schema, format_checker=FormatChecker())
    return True

# Validate the manifest
is_valid = valid(manifest, schema)
print(is_valid)
