import jsl, json

# ProcessedData Object
class ProcessedData(jsl.Document):
    
    class Options(object):
        additional_properties = True
            
    # Global Properties
    class _id(jsl.Document):
        _id = jsl.StringField(pattern='[a-zA-Z-_]+', required=True)

    class namespace(jsl.Document):
        namespace = jsl.StringField(default='we1sv1.1', required=True)

    class path(jsl.Document):
        path = jsl.StringField(pattern='^,[a-zA-Z-_,]+,$', required=True)

    class description(jsl.Document):
        description = jsl.StringField()

    class notes(jsl.Document):
        class note(jsl.Document):
            note = jsl.StringField()
        notes = jsl.ArrayField(jsl.DocumentField(note, as_ref=True), 
                required=True)

    class date(jsl.Document):
        class daterange(jsl.Document):
            start = jsl.StringField(pattern='DATEFORMAT', required=True)
            end = jsl.StringField(pattern='DATEFORMAT')
        class precisedaterange(jsl.Document):
            start = jsl.DateTimeField(required=True)
            end = jsl.DateTimeField(required=True)
        class normal(jsl.Document):
            normal = jsl.ArrayField(jsl.OneOfField([
                jsl.StringField(pattern='DATEFORMAT'),
                jsl.DocumentField(daterange, as_ref=True)
            ]), required=True)
        class precise(jsl.Document):
            precise = jsl.ArrayField(jsl.OneOfField([
                jsl.DateTimeField(),
                jsl.DocumentField(precisedaterange, as_ref=True)
            ]), required=True)
        options = [
            jsl.StringField(pattern='DATEFORMAT'),
            jsl.DateTimeField(),
            jsl.DocumentField(daterange, as_ref=True),
            jsl.DocumentField(precisedaterange, as_ref=True),
            jsl.DocumentField(normal, as_ref=True),
            jsl.DocumentField(precise, as_ref=True)
        ]

        date = jsl.ArrayField(jsl.OneOfField(options), required=True)

    class group(jsl.Document):
        group = jsl.StringField()

    class label(jsl.Document):
        label = jsl.StringField()

    class title(jsl.Document):
        title = jsl.StringField()

    class altTitle(jsl.Document):
        altTitle = jsl.StringField()

    class refLocation(jsl.Document):
        refLocation = jsl.StringField()
    
    # Instantiate all ProcessedData properties
    _id = jsl.DocumentField(_id, default='ProcessedData', required=True)
    namespace = jsl.DocumentField(namespace, as_ref=True, required=True)
    path = jsl.DocumentField(path, pattern='^,Corpus,[a-zA-Z-_,]+,$', required=True)
    description = jsl.DocumentField(description, as_ref=True)
    date = jsl.DocumentField(date, as_ref=True, required=True)
    group = jsl.DocumentField(group, as_ref=True)
    label = jsl.DocumentField(label, as_ref=True)
    title = jsl.DocumentField(title, as_ref=True)
    altTitle = jsl.DocumentField(altTitle, as_ref=True)
    refLocation = jsl.DocumentField(refLocation, as_ref=True)
    notes = jsl.DocumentField(notes, as_ref=True)

    relationships = jsl.ArrayField()
    OCR = jsl.BooleanField()
    rights = jsl.StringField()
    
def get_manifest(schema):
    # Convert ordered dict to json
    manifest = json.dumps(schema, indent=4)
    # Clean up Python artefacts from JSL
    manifest = manifest.replace('__main__.', '')
    # jsonschema validator does not accept lower case booleans
    # This needs to be improved so there are no false positives
    manifest = manifest.replace(': false', ': False')
    manifest = manifest.replace(': true', ': True')
    # Workaround because JSL cannot generate date formats, only datetime
    manifest = manifest.replace('"pattern": "DATEFORMAT"', '"format": "date"')
    return manifest
    
schema = ProcessedData.get_schema(ordered=True)
manifest = get_manifest(schema)
print(manifest)