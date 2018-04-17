import jsl, json, requests

# Create a Manifest Class
class Global(jsl.Document):
    class Options(object):
        additional_properties = True
    class init(jsl.Document):
        init = jsl.StringField()        
    # Manifest properties
    init = jsl.DocumentField(init, as_ref=True, required=True)

    # Required
    name = jsl.StringField(pattern='[a-z0-9\._-]+')
    namespace = jsl.StringField(pattern='we1sv2.0')
    metapath = jsl.StringField(pattern='[a-zA-Z0-9,]+')

    # Optional
    description = jsl.StringField()
    id = jsl.StringField()
    _id = jsl.StringField()
    image = jsl.StringField()
    keywords = jsl.ArrayField()
    label = jsl.StringField()
    notes = jsl.ArrayField()
    shortTitle = jsl.StringField()
    version = jsl.StringField()

# Add the global properties to the definitions
def add_global(manifest):
    # url = 'https://raw.githubusercontent.com/whatevery1says/manifest/master/schema/global/global.json'
    # manifest['definitions'] = json.loads(requests.get(url).text)
    del manifest['properties']['init']
    return manifest

# Add the requirements, global and manifest-specific
def add_requirements(manifest):
    global_requirements = ['name', 'namespace', 'metapath']
    manifest_requirements = []
    requirements = global_requirements + manifest_requirements
    manifest['required'] = requirements
    return manifest

# Set manifest-specific definitions
def set_manifest_definitions(manifest):
#     manifest['definitions'][''][''] = ''
    return manifest

# Get the manifest as a dict
def get_manifest(schema):
    schema = json.dumps(schema, indent=4).replace('__main__.', '')
    schema = json.loads(schema)
    return schema

# Build the manifest
def build_manifest(schema):
    manifest = get_manifest(schema)
    manifest = add_global(manifest)
    manifest = add_requirements(manifest)
    manifest = set_manifest_definitions(manifest)
    return manifest

manifest = build_manifest(Global.get_schema(ordered=True))
print(json.dumps(manifest, indent=4))
