import jsl, json

# Publications Object
class Publications(jsl.Document):
    
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

    # Publications Properties
    class authors(jsl.Document):
        options = [
            jsl.StringField(),
            jsl.DocumentField(group, as_ref=True)
        ]
        authors = jsl.ArrayField(jsl.OneOfField(options))

    # Instantiate all Publications properties
    _id = jsl.DocumentField(_id, as_ref=True, required=True)
    namespace = jsl.DocumentField(namespace, as_ref=True, required=True)
    path = jsl.DocumentField(path, as_ref=True, required=True)
    description = jsl.DocumentField(description, as_ref=True, required=True)
    date = jsl.DocumentField(date, as_ref=True, required=True)
    publication = jsl.StringField(required=True)
    publisher = jsl.StringField(required=True)
    group = jsl.DocumentField(group, as_ref=True)
    label = jsl.DocumentField(label, as_ref=True)
    title = jsl.DocumentField(title, as_ref=True)
    altTitle = jsl.DocumentField(altTitle, as_ref=True)
    refLocation = jsl.DocumentField(refLocation, as_ref=True)
    edition = jsl.StringField()
    contentType = jsl.StringField()
    language = jsl.StringField()
    country = jsl.StringField()
    authors = jsl.ArrayField()
    notes = jsl.DocumentField(notes, as_ref=True)

def get_manifest(schema):
    # Convert ordered dict to json
    manifest = json.dumps(schema, indent=4)
    # Clean up Python artefacts from JSL
    manifest = manifest.replace('__main__.', '')
    # jsonschema validator does not accept lower case booleans
    # This needs to be improved so there are no false positives
    manifest = manifest.replace(': false', ': False')
    # Workaround becuase JSL cannot generate date formats, only datetime
    manifest = manifest.replace('"pattern": "DATEFORMAT"', '"format": "date"')
    return manifest
    
schema = Publications.get_schema(ordered=True)
manifest = get_manifest(schema)
print(manifest)

