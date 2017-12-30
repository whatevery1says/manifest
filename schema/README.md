# Schema Validation Files

## Warning!

These materials are not quite ready for production. After pushing the materials I discovered some extensive problems, which I am slowly fixing. At the moment, the `Publications/Publications.json` schema works and can be generated using `Publications/Publications.py`. It can be tested with the `Publications/sample.json` manifest using `validate_manifest.py`. I will gradually update the other files so that everything works.

This warning message will be updated to reflect ongoing progress.

***

This folder contains a collection of documents for generating schemas for validating WhatEvery1Says manifests. The subfolders contain three files for each manifest type:

1. A `schema_name.py` file that can be used to generate the JSON schema file in Python.
2. A `schema_name.json` file, which is the JSON schema file that can be used to validate manifests.
3. A `schema_name_sample.json` file, which is a sample manifest that can be validated against `schema_name.json`.

## Validating a Manifest against a Schema

Validating manifests against the schema in Python requires the [`jsonschema` validation library](http://python-jsonschema.readthedocs.io/en/latest/#). You can install it with

```python
pip install jsonschema
```

There is a convenient `validate_manifest.py` script in the `schema` folder, which can be used to validate manifests or adapted for use in validation routines elsewhere. It validates against the schemas on GitHub, so it requires internet access to work.

A peculiarity of the `jsonschema` `validate()` method is that it provides no feedback if the manifest is valid. For convenience, the `validate_manifest.py` script wraps this method in a `valid()` function that returns `True` if the manifest is valid.

**Note:**

- `jsonschema` validation errors are often less informative than one would like. But at least you know that there is the data is invalid. If it is not clear what is wrong, it is worth checking whether the manifest is well-formed JSON using [jsonlint](https://jsonlint.com/). If this does not reveal the problem, then the manifest does not follow the WE1S manifest schema in some way.

## Currently Available Validation Schemas

Text links point to the schema documentation. Link icons point directly to the JSON schema files, so right-clicking on them is an easy way to grab their urls.

- [x] [`Publications`](https://github.com/whatevery1says/manifest/blob/master/we1s-manifest-schema-1.1.md#publications) [:link:](https://raw.githubusercontent.com/whatevery1says/manifest/master/schema/Publications/Publications.json)
- [ ] [`collection`](https://github.com/whatevery1says/manifest/blob/master/we1s-manifest-schema-1.1.md#corpus-and-collection-nodes) [:link:](https://raw.githubusercontent.com/whatevery1says/manifest/master/schema/Corpus/collection.json)
- [ ] [`RawData`](https://github.com/whatevery1says/manifest/blob/master/we1s-manifest-schema-1.1.md#rawdata) [:link:](https://raw.githubusercontent.com/whatevery1says/manifest/master/schema/Corpus/RawData.json)
- [ ] [`ProcessedData`](https://github.com/whatevery1says/manifest/blob/master/we1s-manifest-schema-1.1.md#processeddata) [:link:](https://raw.githubusercontent.com/whatevery1says/manifest/master/schema/Corpus/ProcessedData.json)
- [ ] [`Metadata`](https://github.com/whatevery1says/manifest/blob/master/we1s-manifest-schema-1.1.md#metadata) [:link:](https://raw.githubusercontent.com/whatevery1says/manifest/master/schema/Corpus/Metadata.json)
- [ ] [`Outputs`](https://github.com/whatevery1says/manifest/blob/master/we1s-manifest-schema-1.1.md#outputs) [:link:](https://raw.githubusercontent.com/whatevery1says/manifest/master/schema/Corpus/Outputs.json)
- [ ] [`Related`](https://github.com/whatevery1says/manifest/blob/master/we1s-manifest-schema-1.1.md#related) [:link:](https://raw.githubusercontent.com/whatevery1says/manifest/master/schema/Corpus/Related.json)
- [ ] [`Data Documents`](https://github.com/whatevery1says/manifest/blob/master/we1s-manifest-schema-1.1.md#data-documents) [:link:](https://raw.githubusercontent.com/whatevery1says/manifest/master/schema/Corpus/Data.json)
- [ ] `Path Node` (Generic node for branching paths)  [:link:](https://raw.githubusercontent.com/whatevery1says/manifest/master/schema/Corpus/PathNode.json)
- [ ] [`Processes`](https://github.com/whatevery1says/manifest/blob/master/we1s-manifest-schema-1.1.md#processes)
- [ ] [`Step Manifests`](https://github.com/whatevery1says/manifest/blob/master/we1s-manifest-schema-1.1.md#step-manifests)
- [ ] [`Scripts`](https://github.com/whatevery1says/manifest/blob/master/we1s-manifest-schema-1.1.md#scripts)
- [ ] [`Project`](https://github.com/whatevery1says/manifest/blob/master/project-manifests-draft.md)

## Generating a Schema

Generating a JSON schema for a manifest type requires the The documents are all generated using the [Python `JSL` library](http://jsl.readthedocs.io/en/latest/index.html). If the manifests need to be modified, the Python files should be used and the JSON re-generated in order to ensure consistency. You can install `JSL` with

```python
pip install jsl
```

The Python script will output a schema in string format. There is no built-in code to write the string to a file, but it is easy to copy and paste in a file and then saved in JSON format.

JSL is a convenient library for creating JSON schemas, but it has some important limitations in how the schemas can be structured. As a result, JSL is used to initialise the schema and it is then transformed into a dict by pipeline of build functions. Eventually, this can be rewritten as a single class. The pipeline is structured as follows:

1. A manifest class is generated using a single `init` property, which is paced inside the JSON schema `definitions` property and listed as a requirement. `additionalProperties` is set to `true` so that custom properties can be added to the schema. Other properties specific to the manifest type are also initialised.
2. The schema is converted from an ordered dict to a dict to make it easier to work with.
3. The `add_global` function loads the global properties from GitHub and adds them to the schema's `definitions` property. It also deletes the `init` property. Global properties are drawn from the `global/global.js` file on GitHub, so the script will only work if you have internet access.
4. The `add_requirements` function sets the schema's `required` property for both global and manifest-specific requirements.
5. The `set_manifest_definitions` function allows customisation of the schema's definition properties. This most often involves setting the `path` property to require a pattern specific to the type of manifest being generated.
