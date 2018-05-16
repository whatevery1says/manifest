# Table of Contents
- [WhatEvery1Says Schema](#whatevery1says-schema)
    - [Language](#language)
    - [Introduction](#introduction)
    - [WE1S Manifests](#we1s-manifests)
    - [Manifests, MongoDB, and the WE1S Ecosystem](#manifests-mongodb-and-the-we1s-ecosystem)
    - [Metapaths, the Database Structure, and Data Packages](#metapaths-the-database-structure-and-data-packages)
    - [Specification](#specification)
        - [Manifest](#manifest)
        - [Global REQUIRED Properties](#global-required-properties)
            - [`name`](#name)
            - [`metapath`](#metapath)
            - [`namespace`](#namespace)
            - [`title`](#title)
        - [Global OPTIONAL Properties](#global-optional-properties)
            - [`id`](#id)
            - [`_id`](#_id)
            - [`description`](#description)
            - [`version`](#version)
            - [`shortTitle`](#shorttitle)
            - [`label`](#label)
            - [`notes`](#notes)
            - [`keywords`](#keywords)
            - [`image`](#image)
        - [Source Manifests](#source-manifests)
            - [REQUIRED Properties](#required-properties)
            - [OPTIONAL Properties](#optional-properties)
                - [`publisher`](#publisher)
                - [`webpage`](#webpage)
                - [`authors`](#authors)
                - [`date`](#date)
                - [`edition`](#edition)
                - [`contentType`](#contenttype)
                - [`country`](#country)
                - [`language`](#language)
                - [`citation`](#citation)
        - [Data Manifests](#data-manifests)
        - [Data Nodes and Property Inheritance](#data-nodes-and-property-inheritance)
            - [REQUIRED properties](#required-properties)
            - [OPTIONAL properties](#optional-properties)
                - [`path`](#path)
                - [`format`](#format)
                - [`mediatype`](#mediatype)
                - [`encoding`](#encoding)
        - [`Collection` Manifests](#collection-manifests)
        - [`Collection` Nodes](#collection-nodes)
            - [REQUIRED Properties](#required-properties)
                - [`created`](#created)
                - [`sources`](#sources)
                - [`contributors`](#contributors)
            - [OPTIONAL Properties](#optional-properties)
                - [`workstation`](#workstation)
                - [`queryTerms`](#queryterms)
                - [`processes`](#processes)
        - [`RawData` Nodes](#rawdata-nodes)
            - [REQUIRED Properties](#required-properties)
            - [OPTIONAL Properties](#optional-properties)
                - [`documentType`](#documenttype)
                - [`relationships`](#relationships)
                - [`OCR`](#ocr)
                - [`licenses`](#licenses)
        - [`ProcessedData` Nodes](#processeddata-nodes)
            - [REQUIRED Properties](#required-properties)
                - [`processes`](#processes)
            - [OPTIONAL Properties](#optional-properties)
        - [`Metadata` Manifests](#metadata-manifests)
            - [REQUIRED Properties](#required-properties)
            - [OPTIONAL Properties](#optional-properties)
        - [`Outputs` Manifests](#outputs-manifests)
            - [REQUIRED Properties](#required-properties)
            - [OPTIONAL Properties](#optional-properties)
        - [`Related` Manifests](#related-manifests)
            - [REQUIRED Properties](#required-properties)
            - [OPTIONAL Properties](#optional-properties)
        - [Data Packages](#data-packages)
        - [`process` Manifests](#process-manifests)
            - [REQUIRED Properties](#required-properties)
                - [`steps`](#steps)
                - [`date`](#date)
                - [`contributors`](#contributors)
            - [OPTIONAL Properties](#optional-properties)
                - [`created`](#created)
                - [`source`](#source)
        - [`Step` Manifests](#step-manifests)
            - [REQUIRED Properties](#required-properties)
                - [`description`](#description)
                - [`type`](#type)
            - [OPTIONAL Properties](#optional-properties)
                - [`path`](#path)
                - [`options`](#options)
                - [`outputs`](#outputs)
                - [`instructions`](#instructions)
        - [`Script` Manifests](#script-manifests)
            - [REQUIRED Properties](#required-properties)
                - [`contributors`](#contributors)
            - [OPTIONAL Properties](#optional-properties)
                - [`created`](#created)
                - [`path`](#path)
                - [`accessed`](#accessed)
                - [`script`](#script)
        - [Conventions](#conventions)
            - [Formatting Dates](#formatting-dates)
        - [WE1S Projects](#we1s-projects)
            - [Project Manifests](#project-manifests)


# WhatEvery1Says Schema
[[back to top](#table-of-contents)]

**v2.0 DRAFT**
_Last Update: March 30, 2018_

## Language
[[back to top](#table-of-contents)]

The key words `MUST`, `MUST NOT`, `REQUIRED`, `SHALL`, `SHALL NOT`,
`SHOULD`, `SHOULD NOT`, `RECOMMENDED`, `MAY`, and `OPTIONAL` in this
document are to be interpreted as described in [RFC
2119](https://www.ietf.org/rfc/rfc2119.txt "RFC 2119").

Throughout this documentation the term "property" refers to the keyword of a key-value pair. The term "field name" is a synonym of for "property". Data types are described using Javascript/JSON nomenclature: the term `array` refers to a list enclosed in `[]` and the term `object` refers to a key-value pair enclosed in `{}`.

## Introduction
[[back to top](#table-of-contents)]

The WhatEvery1Says Schema (hereafter "WE1S Schema") is a set of recommendations for the construction of manifest documents for the WE1S project. By default, manifests are stored in [JSON format](http://www.rfc-editor.org/info/rfc7159.txt "JSON format") as detailed below. These JSON documents can be used as data storage and configuration files for a variety of scripted processes and tools that read the JSON format.

Each JSON document contains a JSON `object` containing a series of comma-separated key-value pairs enclosed in curly brackets (`{}`).

```javascript
{
    "keyword": "value",
    "keyword": "value"
}
```

These pairs are inherently unordered so, to give them sequence, they may be placed in an `array`, designated by square brackets (`[]`):

```javascript
{
    [
        {"keyword1": "value"},
        {"keyword2": "value"}
    ]
}
```

For multiple properties, it may be useful to construct a more elaborate structure consisting of `arrays` of `objects`:

```javascript
{
    "keyword1": [
        {"sequence": 1},
        {"keyword3": "value"}
    ],
    "keyword2": [
        {"sequence": 2},
        {"keyword4": "value"}
    ]
}
```

Sequential order is assumed for the values of `arrays`; items within `objects` have no inherent order.

A JSON document can have an unlimited number of key-value pairs. The WE1S schema places restrictions on what keywords can be used to document resources and makes recommendations for structuring manifests in a consistent manner. The schema is based on [JSON Schema](http://json-schema.org/), a vocabulary that allows you to annotate and validate JSON documents. An excellent overview is provided in Michael Droettboom's [Understanding JSON Schema tutorial](https://spacetelescope.github.io/understanding-json-schema/). WE1S manifests follow the syntax of JSON Schema so that they always have a valid (i.e. predictable) format. This ensures maximum interoperability for a variety of uses.

## WE1S Manifests
[[back to top](#table-of-contents)]

A manifest is a JSON document which describes resources available to the WhatEvery1Says framework. It consists of:

* Metadata that describes the structure and contents of resources (widely defined)
* Pointers to other resources including other manifests and data files

Pointers may be provided as:

* Remote resources, referenced by URL
* "Metapaths" which indicate hierarchically-arranged relationships between resources in the WE1S ecosystem
* Inline resources such as data included directly in the manifest

WE1S manifests can be used for a variety of purposes. They may include metadata describing a publication, a process, a set of data, or an output of some procedure. Their primary intent is to help humans document and keep track of their workflow.

Manifests are designed to be read easily by humans but parsed just as easily by any programming language that can read JSON. Manifests may be standalone files ("JSON files"), or they may be stored in a database. They may also contain data themselves.

## Manifests, MongoDB, and the WE1S Ecosystem
[[back to top](#table-of-contents)]

The WE1S ecosystem consists of a framework of data, tools, and resources which are meant to be used together, with manifest used to control and describe workflow. Manifests may be stored in a standard operating system's hierarchical file storage system. However, WE1S employs the MongoDB database to manage and search the large number of files generated by the project. Because MongoDB stores its records in a JSON-like format, it is an ideal medium for working with WE1S manifests. MongoDB also allows the project to implement a ["materialized path"](https://docs.mongodb.com/v3.2/tutorial/model-tree-structures-with-materialized-paths/) data model, which mirrors the characteristics of hierarchical file storage. Each manifest is given a "materialized path" property called a `metapath` which is similar to an operating system's file path. The similarity to an actual file path is deliberate; it allows human readers to see directly from the manifest where the file lives within the project ecosystem. The `metapath` is a useful property for importing manifests to and exporting them from the database in an intuitive manner.

## Metapaths, the Database Structure, and Data Packages
[[back to top](#table-of-contents)]

"Metapaths" are equivalent to operating system file/folder paths, except that they do not indicate actual locations within the local file hierarchy. Instead, they serve to conceptually model the relationships of resources in a manner similar to local file storage. Because metapaths reference nodes above the level of a given manifest, content can be easily queried in these higher nodes. A given manifest thus effectively inherits  continent from manifests above it along the same metapath.

The concept of the metapath is formalised as the `metapath` property in the WE1S schema. A `metapath` is a `string` with the following additional constraints:

* A `metapath` MUST is a unix-style POSIX path, except that it uses `,` as a separator, rather than `/`.
* Absolute paths equivalent to Unix-style '/' and relative parent paths equivalent to Unix-style `../` MUST NOT be used, and implementations SHOULD NOT support these path types.

The reason why `,` is specified as the separator instead `/` if that MongoDB is the assumed storage medium for the WE1S project. MongoDB searches documents using regex, patterns, which use `/` as a delimiter. A choice must be made whether to store the `metapath` separator as a comma and convert it to a slash for display purposes or to store it as a slash and convert it to a comma every time a database query is made. Since `metapath` does not represent a real file location, the former strategy seemed the better of the two solutions.

The WE1S ecosystem consists of four inter-related database structures which can be referenced through the `metapath` property.

1. `Corpus`: The database storage for all data, including primary source material, transformed data, the results of analysis, and related documents.
2. `Sources`: Metadata about all source material used to compile the data in `Corpus`.
3. `Processes`: Metadata describing the procedures used to collect and analyse the data in `Corpus`.
4. `Scripts`: Files containing code used to implement the procedures described in `Processes` where these procedures were not implemented using external tools or scripts.

Individual projects may create other databases as needed, but these four are assumed to be present for all WE1S project activities.

The WE1S schema builds on the [Frictionless Data](https://frictionlessdata.io) notion of a [Data Package](https://frictionlessdata.io/specs/data-package/). A Data Package is a special type of manifest (called `datapackage.json`) used to containerise data and associated resources. When data is exported from the WE1S database it will be ideally exported in the form of a Data Package with content in subfolders corresponding to the `Corpus`, `Sources`, `Processes`, and `Scripts` databases.

Manifests storing information in these four databases can be considered to belong to different manifest "types", depending on their function or the nature of their content. Other types of manifests are used specifically for storing certain forms of data, e.g. raw or processed, or to create branching structures in the `metapath` hierarchy. Manifests of all types are REQUIRED to contain certain common properties. Other REQUIRED and OPTIONAL properties will depend on the manifest type. The REQUIRED and OPTIONAL properties for each manifest type are described in the Specification.

## Specification
[[back to top](#table-of-contents)]

### Manifest
[[back to top](#table-of-contents)]

A manifest is a JSON file which describes the nature of a resource of any type. A manifest MUST be a valid JSON `object` as defined in [RFC 4627](https://www.ietf.org/rfc/rfc2119.txt]). The name of the manifest file must be the value of its `name` property followed by the `.json` extension. An exception is made for the manifest of a Data Package, which for compatibility with Frictionless Data, must be called `datapackage.json`.

Manifests MUST contain certain REQUIRED properties and MAY contain any number of OPTIONAL properties. Adherence to the WE1S specification does not imply that additional, non-specified properties cannot be used: a manifest MAY include any number of properties in addition to those described as REQUIRED and OPTIONAL properties. For example, if you were storing
time series data and wanted to list the temporal coverage of the data in a
source, you could add a property `temporal` (cf [Dublin Core terms-temporal](http://dublincore.org/documents/dcmi-terms/#terms-temporal)):

```javascript
"temporal": {
    "name": "19th Century",
    "start": "1800-01-01",
    "end": "1899-12-31"
}
```

This flexibility enables specific communities to extend the schema for the data they manage.

A Global property is a JSON keyword which is available to all manifests, regardless of type. Global properties can either be REQUIRED in all manifests or OPTIONAL in all manifests. Additional REQUIRED and OPTIONAL properties for specific manifest types are discussed individually under separate headings.

### Global REQUIRED Properties
[[back to top](#table-of-contents)]

#### `name`
[[back to top](#table-of-contents)]

A short URL-usable (and preferably human-readable) name of
the package. This MUST be lower-case and contain only alphanumeric characters
along with ".", "_" or "-" characters. It will function as a unique
identifier and therefore SHOULD be unique at the level of the terminal node in the `metapath` property (also globally REQUIRED). The value of `name` taken together with the value of `metapath` should form a globally unique identifier.

The `name` SHOULD be invariant, meaning that it SHOULD NOT change when a manifest is updated, unless the new manifest should be considered a
distinct manifest, e.g. due to significant changes in structure or
interpretation. Version distinction SHOULD be left to the `version` property. As
a corollary, the `name` also SHOULD NOT include an indication of time range
covered.

#### `metapath`
[[back to top](#table-of-contents)]

A `string` providing a "materialised" path representing the location of the this manifest relative to its root. A metapath takes the form of a POSIX file path, except that the normal `/` delimiter is replaced with a comma.

#### `namespace`
[[back to top](#table-of-contents)]

A `string` representing the WE1S namespace and version number (e.g. "we1sv2.0"). The presence of `namespace` ensures that applications be designed to be handle legacy materials as the schema changes over time.

**Note:** The value of `namespace` should ultimately be replaced by an `object` consisting of a `name` and a `url` to the location of the WE1S JSON schema file. For example:

```javascript
"namespace": {
    "name": "we1sv2.0",
    "url": "https://github.com/whatevery1says/manifest/tree/master/schema/manifest.json"
}
```

#### `title`
[[back to top](#table-of-contents)]

A `string` providing a title or one sentence description for this manifest.

### Global OPTIONAL Properties
[[back to top](#table-of-contents)]

The following are commonly used properties that the manifest MAY contain:

#### `id`
[[back to top](#table-of-contents)]

A property reserved for globally unique identifiers, typically conforming to some external schema. Examples of identifiers that are unique include UUIDs and DOIs.

While at the level of the specification, global uniqueness cannot be validated, consumers using the `id` property `MUST` ensure identifiers are globally unique.

Because WE1S assumes that manifests will be stored in a MongoDB database, the value of `id` MAY be filled by MongoDB's auto-generated primary key ([ObjectId](https://docs.mongodb.com/manual/reference/method/ObjectId/#ObjectId)). See discussion of the `_id` property below.

#### `_id`
[[back to top](#table-of-contents)]

The `_id` property is generated by MongoDB's [ObjectId](https://docs.mongodb.com/manual/reference/method/ObjectId/#ObjectId) method for all records stored in the database. The 12-byte ObjectId value consists of:

* a 4-byte value representing the seconds since the Unix epoch,
* a 3-byte machine identifier,
* a 2-byte process id, and
* a 3-byte counter, starting with a random value.

In most cases, the `_id` will not be used for database interactions since most queries will be expected to return manifests specified by the `name` property along a specific `metapath`.

Whilst all manifests stored in the database will automatically gain an `_id` value, it may be necessary to keep this separate from the value of `id` if the latter is used to store an external identifier such as a DOI. In these cases, the `_id` may be written to exported manifests files where it will live as a redundant property.

#### `description`
[[back to top](#table-of-contents)]

A description of the package. The description MUST be
[Markdown](http://commonmark.org/) formatted `string` -- this also allows for simple plain text as plain
text is itself valid markdown. The first paragraph (up to the first double
line break) should be usable as summary information for the package.

#### `version`
[[back to top](#table-of-contents)]

A `string` identifying the version of the package. It should conform to the [Semantic Versioning](https://semver.org/) requirements and should roughly follow the [Frictionless Data Data Package Version](https://frictionlessdata.io/specs/patterns/#data-package-version) pattern.

The value of the image property MUST be a `string` pointing to the location of the image. The string must be either a URL or a `metapath` value, typically something like `Corpus,collection_name,Related,image_file`.

#### `shortTitle`
[[back to top](#table-of-contents)]

A `string` providing a shortened or alternative version of the manifest's `title` value.

#### `label`
[[back to top](#table-of-contents)]

A `string` providing an abbreviated or other identifier for the manifest which can be used in graphs and other displays where space is limited.

#### `notes`
[[back to top](#table-of-contents)]

An `array` of text strings which can contain extended prose commentary about the manifest's content. Individual notes MUST be formatted in [Markdown](http://commonmark.org/).

#### `keywords`
[[back to top](#table-of-contents)]

An `array` of `string` keywords to assist users searching for the
manifest using terms from a controlled vocabulary or some other method of classification.

#### `image`
[[back to top](#table-of-contents)]

An image to use when displaying the manifest, for instance, in a list of manifests. The value of the image property MUST be a `string` pointing to the location of the image. The string must be a fully qualified HTTP address, a relative POSIX path, or a `metapath` to a storage location in a database.

#### `updated`
[[back to top](#table-of-contents)]

The `updated` property is used to describe changes made to a manifest after its initial creation. The value of the property MUST be an `array` of `objects`. Each `object` MUST contain the `change` and `date` properties and MAY contain a `contributors` property. The `change` property must be a `string`. The `date` property follows the standard pattern described under **Formatting Dates** and the `contributors` property follows the specifications described under `collection` manifests.

**Important:** The `updated` property describes ONLY changes to the manifest document in which it is include. It does not apply to changes in linked data. For instance, if additional data files are added to an existing `collection`. The `change` property may indicate this, but it may not be possible to implement a procedure to recover the prior state of the data. This may affect the reproducibility of certain processes. Recommended methods of addressing this include creating a project based on the collection prior to the change, creating a separate collection for the changed data, or implementing changes along different `metapath` branches of the original `collection`. The addition of new branches can be described using the `updated` property in the `collection` manifest.

### Source Manifests
[[back to top](#table-of-contents)]

Source manifests contain bibliographical information about the sources (typically publications) of data in the WE1S `Corpus` database. All source manifests are stored in the WE1S `Sources` database and will therefore have the `metapath` value `Sources,source_name`.

#### REQUIRED Properties
[[back to top](#table-of-contents)]

The following globally REQUIRED properties MUST be included in every source manifest: `name`, `title`, `namespace`.

#### OPTIONAL Properties
[[back to top](#table-of-contents)]

The following globally OPTIONAL properties MAY be included in a source manifest: `id`, `_id`, `description`, `version`, `keyword`, `image`, `shortTitle`, `label`, `notes`, `updated`.

The following additional OPTIONAL properties MAY also be included in a source manifest.

##### `publisher`
[[back to top](#table-of-contents)]

A `string` containing the name of the source's publisher.

##### `webpage`
[[back to top](#table-of-contents)]

A `string` containing a URL for the source. This is an alternative for `publisher` since sometimes that information will not be available for web pages.

##### `authors`
[[back to top](#table-of-contents)]

An `array` containing the names of the author(s) of a publication (e.g. a book). The `array` can consist of `string` values or `objects`. In general, `string` values should be standard full representations of authors' names since it is expected that this information will be queried by regex. However, an `object` can be used to indicate collective authorship using the `group` and `organization` properties:

```javascript
"authors": [
    {
        "group": "Summer Research Camp 2018",
        "organization": "UC Santa Barbara"
    }
]
```

`Objects` can also be used to encode specific parts of author names such as `surname` and `forename`. However, WE1S currently has no standard nomenclature for parts of names.

##### `date`
[[back to top](#table-of-contents)]

An `array` containing the date of publication or range of publication dates where known. Dates should be given in ISO 8601 date (`YYYY-MM-DD`) or datetime (e.g. `2017-09-16T12:49:05Z`) format, wherever sufficient information is known. For further information, see the section on **Formatting Dates**.

##### `edition`
[[back to top](#table-of-contents)]

A `string` indicating the edition number (e.g. "2nd") or medium (e.g. "print" or "online") of the publication. WE1S currently has no controlled vocabulary for `edition` values.

##### `contentType`
[[back to top](#table-of-contents)]

A `string` representing the nature or genre of the data (e.g. "newspaper").WE1S does not currently have a controlled vocabulary for the value of this field.

##### `country`
[[back to top](#table-of-contents)]

A `string` value taken from the [ISO 3166-1 ALPHA-2](https://en.wikipedia.org/wiki/ISO_3166-1) country codes.

##### `language`
[[back to top](#table-of-contents)]

A `string` value taken from the [ISO 639-2]((http://www.loc.gov/standards/iso639-2/php/code_list.php) list of language codes. If multiple languages are required, an `array` of `strings` can be supplied.

##### `citation`
[[back to top](#table-of-contents)]

An `object` containing a bibliographic citation for the source, generally one that is intended for display.

Citations MUST contain a `schema` property indicating the style guidelines followed in formatting the citation. This may be either a `string` value like "Chicago, 17th edition" or, preferably, a URL to a schema description website (e.g. "https://github.com/citation-style-language/schema").

A citation MAY contain a `text` property containing a fully-formatted `string` citation. Formatting must be given in [Markdown](http://commonmark.org/).

A citation MAY contain an `object` with field names corresponding to a schema such as the [Citation Style Language](http://citationstyles.org/). For example:

```javascript
{
    "citation": {
    "schema": "https://github.com/citation-style-language/schema",
    "fields": {
        /* A partial citation */
        "title": "The Cambridge Companion to Textual Scholarship",
        "publisher": "Cambridge University Press",
        "ISBN": "978-0-521-60329-4"
        }
    }
}
```

There is no standard JSON schema for citations, but WE1S recommends the Citation Style Language. CSL is used by Zotero, which can export its records as JSON objects that can be inserted in source manifests.

### Data Manifests
[[back to top](#table-of-contents)]

A data manifest is a JSON file which contains inline data or, points to data in another location.

Data manifests containerise data files, generally, but not always textual data. All data manifests are stored in the WE1S `Corpus` database and therefore MUST have  `metapath` values beginning with `Corpus`.

The illustrative example below points to data available at a certain URL:

```javascript
{
    "name": "an_article",
    "title": "Title of the Article",
    "path": "http://example.com/an-article.txt"
}
```

Local data resources are assumed to belong to data sets called `collections`. A data manifest can contain "inline" data by referencing the manifest's location relative to a `collection` in the `metapath` property. The data itself is given in the `data` property.

```javascript
{
    "name": "an_article",
    "title": "An Article",
    "metapath": "Corpus,collection_name,RawData",
    "data": "This is the text of the article."
}
```

A variation of this points to an actual data file using the `path` property:

```javascript
{
    "name": "an_article",
    "title": "An Article",
    "metapath": "Corpus,collection_name,RawData,txt",
    "path": "Corpus,collection_name,RawData,txt,an_article.txt"
}
```

### Data Nodes and Property Inheritance
[[back to top](#table-of-contents)]

The final node of the `metapath` will either be a manifest containing inline data or a pointer to a data file. Parent nodes for this manifest will represent "branches" within the `collection`. Some properties specified by parent nodes are inherited by their children. For instance, the `OCR` property applied to the `RawData` node of a `collection` will apply to all the individual data files classified as `RawData`. This inheritance can be overriden by including the `OCR` property in individual data manifests. In the discussion below, inheritable properties are discussed in the context of manifest types where they are most likely to be used. This does not mean that they are unavailable for use in other types of data manifests.

#### REQUIRED properties
[[back to top](#table-of-contents)]

Data manifests MUST have the following optional properties: `name`, `title`, `namespace`, `metapath`.

#### OPTIONAL properties
[[back to top](#table-of-contents)]

The following globally OPTIONAL properties MAY be included in a data manifest: `id`, `_id`, `authors`, `description`, `version`, `keyword`, `image`, `shortTitle`, `label`, `notes`, `updated`.

A data manifest MAY contain any of the following additional properties:

##### `path`
[[back to top](#table-of-contents)]

A `string` indicating the location of the data file. The `path` value has the following additional constraints:

* It MUST either be a URL or a POSIX path
* URLs MUST be fully qualified. MUST be using either http or https scheme. (Absence of a scheme indicates MUST be a POSIX path)
* POSIX paths (unix-style with `/` as separator) are supported for referencing local files, with the security restraint that they MUST be relative siblings or children of the descriptor. Absolute paths (`/`) and relative parent paths (`../`) MUST NOT be used, and implementations SHOULD NOT support these path types.
* The value of `path` MUST end in a file name.

The `path` property differs from the `metapath` in that the latter indicates the parent container for the data file and does not directly indicate the storage location of the file. The `path` value provides the full path to the storage location.

##### `format`
[[back to top](#table-of-contents)]

A `string` providing the standard file extension for the type of resource (e.g. "csv", "xls", "json", etc.).

##### `mediatype`
[[back to top](#table-of-contents)]

A `string` providing the mediatype/mimetype of the resource, e.g. "text/csv", "application/vnd.ms-excel". A list of common media formats can be found at [http://en.wikipedia.org/wiki/Internet_media_type# List_of_common_media_types](http://en.wikipedia.org/wiki/Internet_media_type# List_of_common_media_types).

##### `encoding`
[[back to top](#table-of-contents)]

A `string` providing the specific character encoding of the resource's data file. The values should be one of the "Preferred MIME Names" for a [character encoding registered with IANA](http://www.iana.org/assignments/character-sets/character-sets.xhtml). If no value for this key is specified then the default is UTF-8.

### `Collection` Manifests
[[back to top](#table-of-contents)]

Data sets are assumed to be stored in the `Corpus` database as `collections`. A `collection` is defined by a manifest containing metadata. Here is an example:

```javascript
{
    "name": "name_of_collection",
    "title": "Collection Name",
    "metapath": "Corpus",
}
```

`Collection` manifests can contain several branch nodes:

* `RawData`: Used for data in its source form
* `ProcessedData`: Used for data that has been transformed by one or more processes
* `Metadata`: Used for metadata files which were collected along with the data.
* `Outputs`: Used for data files produced from analytic processes
* `Related`: Used for files such as documentation associated with the data set

These subcategories are created by placing child nodes along the `collection` `metapath`: `Corpus,collection_name,RawData`, `Corpus,collection_name,ProcessedData`, etc.

It is possible to use the same technique to create sub-branches of data. For instance, `Corpus,collection_name,ProcessedData,lower_case`, `Corpus,collection_name,ProcessedData,stopwords_removed`.

In database storage, `collection` manifests are simply floating manifests which hold metadata relevant to all manifests and data further along the `metapath`. When data is exported from the `Corpus` database, it is assembled into a Data Package with a `datapackage.json` manifest in the containing folder and subfolders corresponding to the branches along the `metapath`. Typically the branch manifest will be placed alongside each subfolder to preserve the metadata relevant to the files in that folder.

The following sections detail the REQUIRED and OPTIONAL metadata for each type of `collection` manifest.

### `Collection` Nodes
[[back to top](#table-of-contents)]

A `collection` is defined by a manifest that serves as the root node of the collection.

#### REQUIRED Properties
[[back to top](#table-of-contents)]

Manifests serving as root nodes of `collections` MUST include the following properties: `name`, `title`, `namespace`, and `metapath`. In addition, `collection` manifests MUST include `created`, `sources`, and `contributors` properties as detailed below.

##### `created`
[[back to top](#table-of-contents)]

An `array` containing the date or dates on which the `collection` was created. Dates should be given in ISO 8601 date (`YYYY-MM-DD`) or datetime (e.g. `2017-09-16T12:49:05Z`) format, wherever sufficient information is known. For further information, see the section on **Formatting Dates**.

##### `sources`
[[back to top](#table-of-contents)]

An `array` containing the published sources for this collection. The value of `sources` MUST be an array of `objects`, typically from the `Sources` database. Each source object MUST have a `title` and `path` properties and MAY have an `email` property. Example:

```javascript
"sources": [
    {
        "title": "World Bank and OECD",
        "path": "http://data.worldbank.org/indicator/NY.GDP.MKTP.CD"
    }
]
```

`title`: title of the source (e.g. document or organization name)
`path`: A url-or-path string, that is a fully qualified HTTP address, or a relative POSIX path.
`email`: An email address

In most cases, the `path` will point to a manifest in the `Sources` database, but other possibilities are allowed for projects not using a database to store sources.

##### `contributors`
[[back to top](#table-of-contents)]

The people or organizations who contributed to the harvesting, downloading, collecting, or assembling the collection. The value of the `contributors` property MUST be an `array`. Each entry is a Contributor and MUST be an `object`. A Contributor MUST have a `title` property and MAY contain `path`, `email`, `role`, `group`, and `organization` properties. An example of the `object` structure is as follows:

```javascript
{
    contributors: [
        {
            "title": "Joe Bloggs",
            "email": "joe@bloggs.com",
            "path": "http://www.bloggs.com",
            "role": "author"
        }
    ]
}
```

* `title`: A `string` containing the name/title of the contributor (name for person, name/title of organization).
* `path`: A `string` containing a fully qualified http URL pointing to a relevant location online for the contributor.
* `email`: A `string` containing an email address.
* `role`: A `string` describing the role of the contributor. It MUST be one of: `author`, `publisher`, `maintainer`, `wrangler`, and `contributor`. Defaults to `contributor`.
* Note on semantics: use of the `author` property does not imply that that person was the original creator of the data in the collection - merely that they created the data.
* `group`: A `string` describing a smaller body of contributors within an `organization`.
* `organization`: A `string` describing the organization to which this contributor is affiliated.

#### OPTIONAL Properties
[[back to top](#table-of-contents)]

The following globally OPTIONAL properties MAY be included in a `collection` manifest: `id`, `_id`, `description`, `version`, `keyword`, `image`, `shortTitle`, `label`, `notes`, `updated`.

The following additional OPTIONAL properties MAY also be included in a `collection` manifest.

##### `workstation`
[[back to top](#table-of-contents)]

A `string` value providing information about the environment in which the data was collected (e.g. "Windows 8.1"). There is currently no controlled vocabulary for this property.

##### `queryTerms`
[[back to top](#table-of-contents)]

An `array` providing keywords used to define the scope of the `collection` (typically used in an API query to collect the data). The value can be used to query the `Corpus` for data matching a particular description.

##### `processes`
[[back to top](#table-of-contents)]

An `array` containing embedded processes or paths to separate `process` manifests. Both types follow the same schema, described under `Processes`.

### `RawData` Nodes
[[back to top](#table-of-contents)]

`RawData` manifests serve as root nodes for all data in the `collection` that has not been transformed by any processing steps after collection.

#### REQUIRED Properties
[[back to top](#table-of-contents)]

`RawData` manifests MUST include the following properties: `name`, `title`, `namespace`, and `metapath`. The `metapath` MUST be `Corpus,collection_name,RawData`.

#### OPTIONAL Properties
[[back to top](#table-of-contents)]

The following globally OPTIONAL properties MAY be included in a `RawData` manifest: `id`, `_id`, `description`, `version`, `keyword`, `image`, `shortTitle`, `label`, `notes`, `updated`.

The following additional OPTIONAL properties MAY also be included in a `RawData` manifest.

##### `documentType`
[[back to top](#table-of-contents)]

A `string` providing a description of the nature of the data accoring to some controlled vocabulary (e.g. "bag of words", "table data). WE1S does not currently have a standard controlled vocabulary for this property.

##### `relationships`
[[back to top](#table-of-contents)]

An `array` of `strings` or `objects`. The schema below uses the relationships property to describe the data as being a part of another collection ("collection1") combined with material from a third collection ("collection2"). Terms from Dublin Core are used in this example, but it is possible to use other terms from any controlled vocabulary.

```javascript
"relationships": [
    {"isPartOf","Corpus,collection1,"},
    {"hasPart","Corpus,collection2"}
]
```

##### `OCR`
[[back to top](#table-of-contents)]

A `Boolean` to indicate whether the data has been digitized using Optical Character Recognition. If omitted, the default value is `false`.

##### `licenses`
[[back to top](#table-of-contents)]
The license(s) under which the package is provided.

**This property is not legally binding and does not guarantee the package is licensed under the terms defined in this property.**

`licenses` MUST be an array. Each item in the array is a License. Each MUST be an `object`. The `object` MUST contain a `name` property and/or a `path` property. It MAY contain a `title` property.

Here is an example:

```javascript
"licenses": [
    {
        "name": "ODC-PDDL-1.0",
        "path": "http://opendatacommons.org/licenses/pddl/",
        "title": "Open Data Commons Public Domain Dedication and License v1.0"
    }
]
```

* `name`: The name MUST be an Open Definition license ID
* `path`: A url-or-path string, that is a fully qualified HTTP address, or a relative POSIX path.
* `title`: A human-readable title.

Omission of the `licenses` property assumes a single value with "Free Culture" as the `name` and an empty `path`.

### `ProcessedData` Nodes
[[back to top](#table-of-contents)]

`ProcessedData` manifests serve as root nodes for all data in the `collection` that has been transformed or processed after it was collected.

#### REQUIRED Properties
[[back to top](#table-of-contents)]

`ProcessedData` manifests MUST include the following properties: `name`, `title`, `namespace`, and `metapath`. The `metapath` MUST be `Corpus,collection_name,ProcessedData`. In addition, `collection` manifests MUST include the `processes` property.

##### `processes`
[[back to top](#table-of-contents)]

An `array` containing processes used in the transformation of the `RawData` source material. The `array` MAY contain a list of paths to separate process manifests OR inline descriptions of the processes. In the latter case, the descriptions MUST be `objects` conforming to the schema described for `process` manifests detailed below.

#### OPTIONAL Properties
[[back to top](#table-of-contents)]

The following globally OPTIONAL properties MAY be included in a `ProcessedData` manifest: `id`, `_id`, `description`, `version`, `keyword`, `image`, `shortTitle`, `label`, `notes`, `updated`.

The following additional properties MAY be included in a `ProcessedData` manifest: `format`, `mediatype`, `encoding`, and `documentType`. These will be inherited by all data along the `ProcessedData` metapath unless overridden in individual data manifests.

### `Metadata` Manifests
[[back to top](#table-of-contents)]

`Metadata` manifests define `metapath` routes for documents containing metadata that may have been acquired along with the raw data.

#### REQUIRED Properties
[[back to top](#table-of-contents)]

`Metadata` manifests MUST include the following properties: `name`, `title`, `namespace`, and `metapath`. The `metapath` MUST be `Corpus,collection_name,Metadata`.

#### OPTIONAL Properties
[[back to top](#table-of-contents)]

The following globally OPTIONAL properties MAY be included in a `Metadata` manifest: `id`, `_id`,`description`, `version`, `keyword`, `image`, `shortTitle`, `label`, `notes`, `updated`.

The following additional properties MAY be included in a `Metadata` manifest: `format`, `mediatype`, `encoding`, and `documentType`. These will be inherited by all data along the `Metadata` metapath unless overridden in individual data manifests.

### `Outputs` Manifests
[[back to top](#table-of-contents)]

`Outputs` manifests define `metapath` routes for data and metadata generated through WE1S analytic processes. It is important to note that storing materials along the `Outputs` metapath makes them a permanent part of the `collection` or `Project`.

#### REQUIRED Properties
[[back to top](#table-of-contents)]

`Outputs` manifests MUST include the following properties: `name`, `title`, `namespace`, and `metapath`. The `metapath` MUST be `Corpus,collection_name,Outputs`.

#### OPTIONAL Properties
[[back to top](#table-of-contents)]

The following globally OPTIONAL properties MAY be included in a `Outputs` manifest: `id`, `_id`,`description`, `version`, `keyword`, `image`, `shortTitle`, `label`, `notes`, `updated`.

The following additional properties MAY be included in a `Outputs` manifest: `format`, `mediatype`, `encoding`, and `documentType`. These will be inherited by all data along the `Outputs` metapath unless overridden in individual data manifests.

### `Related` Manifests
[[back to top](#table-of-contents)]

`Related` manifests define `metapath` routes for documents (typically files) such as documentation which are archived for reference.

#### REQUIRED Properties
[[back to top](#table-of-contents)]

`Related` manifests MUST include the following properties: `name`, `title`, `namespace`, and `metapath`. The `metapath` MUST be `Corpus,collection_name,Related`.

#### OPTIONAL Properties
[[back to top](#table-of-contents)]

The following globally OPTIONAL properties MAY be included in a `Related` manifest: `id`, `_id`,`description`, `version`, `keyword`, `image`, `shortTitle`, `label`, `notes`, `updated`.

The following additional properties MAY be included in a `Related` manifest: `format`, `mediatype`, `encoding`, and `documentType`. These will be inherited by all data along the `Related` metapath unless overridden in individual data manifests.

### Data Packages
[[back to top](#table-of-contents)]

Frictionless Data Data Packages are the default export format for data stored in the WE1S database. Every effort has been made to make the WE1S manifest schema compatible with the [Frictionless Data specification](https://frictionlessdata.io/specs/data-package/). The major difference is that Frictionless Data requires that _all_ resources be listed in the `resources` array found in the `datapackage.json` file. A shorthand is to include only paths to the higher node manifests (e.g. `RawData`, `ProcessedData`) stored in the same directory. An application can then reference data in subfolders using information contained therein. To do this, the application must be able to implement the WE1S schema. Generic Data Package tools may not be able to locate the data out of the box.

### `process` Manifests
[[back to top](#table-of-contents)]

A `process` manifest documents the ways in which data is modified by analytic or other processes. It is primarily a method of recording the steps a user has taken in executing a workflow and is a means by which those steps can be duplicated. All `process` manifests are stored in the WE1S `Processes` database.

#### REQUIRED Properties
[[back to top](#table-of-contents)]

`process` manifests MUST include the following properties: `name`, `title`, `namespace`, and `metapath`. The `metapath` MUST begin with `Processes,process_name`. In addition, `process` manifests MUST include the following properties:

##### `steps`
[[back to top](#table-of-contents)]

An `array` of JSON objects providing each step in the `process` as described under **`step` Manifests**. Alternatively, the value of `steps` can be an `array` of `string` paths to other `process` manifests or `step` manifests.

##### `date`
[[back to top](#table-of-contents)]

An `array` containing a date or dates indicating when the steps detailed in the manifest were implemented. The value should be a `string` containing the date in date (`YYYY-MM-DD`) or datetime (e.g. `2017-09-16T12:49:05Z`) format. See the **Formatting Dates** section for further details.

**Important:** The `date` property is only REQUIRED for inline `processes` in `collection` manuscripts since it would not make sense for re-usable processes in the `Processes` database.

##### `contributors`
[[back to top](#table-of-contents)]

The people or organizations who contributed to the implementing the processes described in the manifest. The value of the `contributors` property MUST be an `array`. Each entry is a Contributor and MUST be an `object`. A Contributor MUST have a `title` property and MAY contain `path`, `email`, `role`, `group`, and `organization` properties. For further discussion of conventions, see the description of the `contributors` under `collection` Manifests.

#### OPTIONAL Properties
[[back to top](#table-of-contents)]

The following globally OPTIONAL properties MAY be included in a `process` manifest: `id`, `_id`, `description`, `version`, `keyword`, `image`, `shortTitle`, `label`, `notes`, `updated`.

The following additional properties MAY be included in a `process` manifest.

##### `created`
[[back to top](#table-of-contents)]

A `string` containing the date when the process was created. The value should be a `string` containing the date in date (`YYYY-MM-DD`) or datetime (e.g. `2017-09-16T12:49:05Z`) format. For further details, see the **Formatting Dates** section.

##### `source`
[[back to top](#table-of-contents)]

If the `process` is dependent on a particular `collection` or other set of source data, the `source` property should be used to indicate the location of the data. The value MUST be a `string` containing a URL, local path, or `metapath` to the data manifest or files. If it does not include the name of the data's `collection`, this should be mentioned in the `process` manifest's `description`. The `source` property is unnecessary for inline `processes` embedded in a `collection` since the `collection` is assumed to be the data source.

### `Step` Manifests
[[back to top](#table-of-contents)]

A `step` manifest describes the workflow parameters of a single step in a `process`. It MUST be an `object`. `step` manifests MAY be embedded within or referenced from a `process` manifest.

#### REQUIRED Properties
[[back to top](#table-of-contents)]

`Step` manifests MUST include the following properties: `name`, `title`, `namespace`, and `metapath`. The `metapath` MUST begin with `Processes,process_name,step_name`. In addition, `step` manifests MUST include the following properties:

##### `description`
[[back to top](#table-of-contents)]

A `string` describing the processing step. Whereas `description` is OPTIONAL for many manifests, it is required for a `step` manifest.

##### `type`
[[back to top](#table-of-contents)]

A `string` describing the means by which the processing step was implemented. There is currently no controlled vocabulary for this property. Possible values are "script", "tool", or "API".

#### OPTIONAL Properties
[[back to top](#table-of-contents)]

The following globally OPTIONAL properties MAY be included in a `step` manifest: `id`, `_id`, `version`, `keyword`, `image`, `shortTitle`, `label`, `notes`, `updated`.

The following additional properties MAY be included in a `step` manifest.

##### `path`
[[back to top](#table-of-contents)]

A `string` providing a reference to the location of the tool or script. If it is a tool, this can be a URL to the tool's website. If the step involves a script, the reference should be a URL to the script's repository or a `metapath` to the script's manifest.

##### `options`
[[back to top](#table-of-contents)]

An `array` containing information about the configuration of the tool or script used in the step. Each `option` MUST be an `object`. The `option` name should be given as the "argument" and the "value" should be the option setting. This structure is ideally suited for command-line tools, but the JSON object can contain fields like the following to record a sample configuration file.

```javascript
{
    "settings.cfg": "Sample config file:..."
}
```

Likewise, you might have

```javascript
{
    "api": "http://api.nytimes.com/svc/search/v2/articlesearch"
}
```

for an API query with further arguments for the query terms.

##### `outputs`
[[back to top](#table-of-contents)]

An `array` of paths to the root node where all the `process`'s outputs are stored.

##### `instructions`
[[back to top](#table-of-contents)]

A `string` containing instructions for implementing the `process`. Although instructions MAY also be put in the `notes` and `description` fields, an explicit `instructions` field may be helpful in some instances.

### `Script` Manifests
[[back to top](#table-of-contents)]

`script` manifests include information about external software and tools, as well as scripts authored by WE1S staff. `script` manifests make extensive use of the `metapath` property to create branching structures for standard types of scripted procedures:

* collecting
* preprocessing
* analysis
* visualization

Whilst these branches are expected in WE1S project, others may be used as necessary.

Each branch MAY have child branches for different tools. However, WE1S expects sub-branches dividing scripts by language (Python and R in the examples below). Hence a possible `metapath` would be `Scripts,preprocessing,python,strip_tags`. If the manifest is for a tool or external program, the last item in the branch will be the manifest containing metadata about the tool or program. If it is a WE1S script, the manifest MAY additionally contain the code of the script itself inline.

#### REQUIRED Properties
[[back to top](#table-of-contents)]

`Script` manifests MUST include the following properties: `name`, `title`, `namespace`, and `metapath`. The `metapath` MUST begin with `Scripts`. In addition, `script` manifests MUST include the following properties:

##### `contributors`
[[back to top](#table-of-contents)]

The people or organizations who contributed to the creation of the tool or script. The value of the `contributors` property MUST be an `array`. Each entry is a Contributor and MUST be an `object`. A Contributor MUST have a `title` property and MAY contain `path`, `email`, `role` and `organization` properties. An example of the `object` structure is as follows:

```javascript
{
contributors: [
        {
            "title": "Joe Bloggs",
            "email": "joe@bloggs.com",
            "path": "http://www.bloggs.com",
            "role": "author"
        }
    ]
}
```

* `title`: A `string` containing the name/title of the contributor (name for person, name/title of organization).
* `path`: A `string` containing a fully qualified http URL pointing to a relevant location online for the contributor
* `email`: A `string` containing an email address.
* `role`: A `string` describing the role of the contributor. It MUST be one of: `author`, `publisher`, `maintainer`, `wrangler`, and `contributor`. Defaults to `contributor`.
* Note on semantics: use of the `author` property does not imply that that person was the original creator of the data in the data package - merely that they created the data.
* `organization`: A `string` describing the organization this to which this contributor is affiliated.

#### OPTIONAL Properties
[[back to top](#table-of-contents)]

The following globally OPTIONAL properties MAY be included in a `script` manifest: `id`, `_id`, `description`, `version`, `keyword`, `image`, `shortTitle`, `label`, `notes`, `updated`.

The following additional properties MAY be included in a `script` manifest.

##### `created`
[[back to top](#table-of-contents)]

The date when the script was authored or last updated. The value should be a `string` containing the date in date (`YYYY-MM-DD`) or datetime (e.g. `2017-09-16T12:49:05Z`) format. See **Formatting Dates** for further information on how to represent the value of the `created` property.

##### `path`
[[back to top](#table-of-contents)]

For external scripts, the URL of the location where the script was accessed for the creation of the manifest.

##### `accessed`
[[back to top](#table-of-contents)]

For external scripts, such as those stored on GitHub, the `accessed` property indicates when the script location was accessed for the creation of the manifest. The value should be a `string` containing the date in date (`YYYY-MM-DD`) or datetime (e.g. `2017-09-16T12:49:05Z`) format. See **Formatting Dates** for further information on how to represent the value of the `accessed` property.

##### `script`
[[back to top](#table-of-contents)]

A `string` copy of the script code. Line breaks in the encode should be given as `\n`, and all quotation marks should be properly escaped.

### Conventions
[[back to top](#table-of-contents)]

#### Formatting Dates
[[back to top](#table-of-contents)]

The `date`, `created`, and `accessed` properties all contain dates which should be given according to the following conventions:

* Individual dates MUST be `strings` in date (`YYYY-MM-DD`) or datetime (e.g. `2017-09-16T12:49:05Z`) format.

```javascript
{
    "date": "2017-09-16"
}
```

* Multiple dates may be given in an `array`.

```javascript
{
    "date": [
        "2017-09-16",
        "2017-09-16T12:49:05Z"
    ]
}
```

* If it is necessary to specify the format, the date may be given as an `object` containing `text` and `format` properties:

```javascript
{
    "date": [
        {
            "text": "2017-09-16",
            "format": "date"
        },
        {
            "text": "2017-09-16T12:49:05Z",
            "format": "datetime"
        }
    ]
}
```

* Date ranges can be specified with an `object` with the keyword `range`. The `object` MUST contain a `start` property and MAY contain an `end` property. Both MUST have `string` values as in the example below:

```javascript
{
    "date": {
        "range": {
            "start": "2017-09-16",
            "end": "2018-09-16"
        }
    }
}
```

* `start` and `end` values may also be expressed as `objects` containing `text` and `format` properties.

### WE1S Projects
[[back to top](#table-of-contents)]

A project is a containerised set of manifests and data that can be stored and manipulated outside the database. They may in turn be stored in a separate `Projects` database for future reference.

In form, a project is a Frictionless Data data package built from the `metapath` contents of its resources. It consists of the following:

* A folder containing a `datapackage.json` file with the following limitation: the `resources` property must contain the paths `Sources`, `Corpus`, `Processes`, and `Scripts` AND _only_ these paths. The folder should also contain subfolders with these same names.
* Each subfolder SHOULD contain at least one manifest file. For instance, the `Corpus` folder might contain a `collection` manifest called `new_york_times.json`. This SHOULD have a corresponding folder called with the same name minus the file extension (e.g. `new_york_times`).
* Additional subfolders and manifests should be created at the next level of the file hierarchy for each resource added to the data package. For instance, if there is a `Corpus,new_york_times,RawData` manifest added, the data package folder should contain a `RawData.json` and a `Corpus/new_york_times/RawData` folder inside the `Corpus/new_york_times` folder.

Note that this does not exactly follow the Frictionless Data specificiation because not all resources are listed in the `datapackage.json` file. However, it is possible to create a complete list of resources programmatically by recursively listing the contents of the folders or querying properties in the manifests contained therein.

#### Project Manifests

The following REQUIRED properties MUST be included in every `project` manifest: `name`, `title`, `namespace`, `content`, `contributors`, `created`.

The `created` and `contributors` properties are the same as found in `collection` manifests. The `content` property MUST contain a [BSON](http://bsonspec.org/)-formatted `.zip` archive, the name of which must the same value as the `name` property. The other properties are globally REQUIRED properties.

In addition, `project` manifests MAY contain the following OPTIONAL properties: `id`, `_id`, `description`, `version`, `keyword`, `image`, `shortTitle`, `label`, `notes`, `updated`, `webpage`, `contentType`, `citation`. The last three are the same as found in `source` manifests.

In general, `project` resources can be reconstructed by iterating through the project's folders and subfolders. However, for some applications this can be an inconvenience, especially if the project is archived as a zip file. In these cases, the `project` manifest MAY contain a `resources` property. This MUST be an array of strings or objects. By default, the array will contain strings corresponding to the paths to the individual resources, whether within the project's file structure or on the internet:

```javascript
"resources": [
    "Corpus/collection_name/RawData",
    "http://example.com/resource-path.csv"
]
```

Paths ending in folders are assumed to be parents of all files and subfolders contained therein. However, it is up to the individual application to parse them recursively or filter the data as necessary.

The example above may alternatively be represented as an array of objects with the `path` property:

```javascript
"resources": [
    {
        "path": "Corpus/collection_name/RawData"
    },
    {
        "path": "http://example.com/resource-path.csv"
    }
]
```

Object representation of resources is most useful when the resources contain other methods of accessing content such as database queries. In this case, the `db_query` property may be used with a `platform` property.

```javascript
"resources": [
    {
        "db_query": "Corpus/collection_name",
        "platform": "MongoDB"
    }
]
```
