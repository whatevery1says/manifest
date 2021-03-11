# `Project` Manifests

# DRAFT

`Project` manifests consist of metadata and resource information. The schema requirements are based on the [Frictionless Data](http://frictionlessdata.io/) specification for data packages and should be largely compatible with it.

## Metadata

### `_id` (required)

A short url-usable (and preferably human-readable) name of the project. This must be lower-case and contain only alphanumeric characters along with ".", "_" or "-" characters. It will function as a unique identifier and therefore should be unique in relation to any registry in which this package will be deposited (and preferably globally unique).

The `_id` should be invariant, meaning that it should not change when a project is updated. Version distinction should be left to the version property. As a corollary, the name also should not include an indication of time range covered.

_Note: The `_id` property corresponds to the Frictionless Data `name` property. The formatting requirements specified in Frictionless Data may be worth adopting for the WE1S `_id` property generally._

### `identifier` (optional)

A property reserved for globally unique identifiers. Examples of identifiers that are unique include UUIDs and DOIs.

_Note: This is a version of the Frictionless Data `id` property, renamed so that it is not easily confused with the WE1S `_id` property. Perhaps it should be renamed `unique_identifier`, `permanent_id`, or something like that._

### `licenses` (optional)

An array containing the license(s) under which the project is provided.

**This property is not legally binding and does not guarantee the package is licensed under the terms defined in this property.**

Each item in the array is a License. Each must be an `object` containing a `name` property and/or a `path` property. It may contain a `title` property.

Here is an example:

```json
"licenses": [{
  "name": "ODC-PDDL-1.0",
  "path": "http://opendatacommons.org/licenses/pddl/",
  "title": "Open Data Commons Public Domain Dedication and License v1.0"
}]
```

* `name`: The `name` must be an [Open Definition license ID](http://licenses.opendefinition.org/)
* `path`: A url or file path string.
* `title`: A human-readable title.

#### `title` (optional)

A `string` providing a title or one sentence description for this project. For WE1S, it might typically be the name of the git repo containing the project zip archive.

### `description` (required)

A prose description of the package.

### `version` (optional)

A version string identifying the version of the package. It should conform to the [Semantic Versioning](http://semver.org) requirements.

### `contributors` (required)

An array containing the people or organizations who contributed to this project. Each Contributor is an object containing a `title` property and, optionally, `path`, `email`, `role` and `organization` properties. An example of the object structure is as follows:

```json
contributors: [{
  "title": "Joe Bloggs",
  "email": "joe@bloggs.com",
  "path": "http://www.bloggs.com",
  "role": "author"
}]
```

* `title` (required): name/title of the contributor (name for person, name/title of organization)
* `path`: a fully qualified http URL pointing to a relevant location online for the contributor
* `email`: An email address
* `role`: a string describing the role of the contributor. It must be one of: `author`, `publisher`, `maintainer`, `wrangler`, and `contributor`. Defaults to `contributor`.
* `organization`: a string describing the organization this contributor is affiliated to.

### `keywords` (optional)

An array of string keywords to assist users searching for the project.

### `created` (required)

The datetime on which this project was created. The datetime must conform to [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.

## Resource Information

Packaged data resources are described in the required `resources` property of the `Project` manifest. This property must be an array of `objects` with the following properties:

`name` (required)

A simple name or identifier to be used for this resource. The name must be unique amongst all resources in the project. It MUST consist only of lowercase alphanumeric characters plus ".", "-" and "_". It would be usual for the name to correspond to the _id value of a workflow produce by the Virtual Workspace.

`path` (required)

Must be a string or array of strings representing a URL or file path. In WE1S, this will typically be a URL to a specific commit to a GitHub repo containing a zip archive produced by the Virtual Workspace. Otherwise, the `path` property should include a pointer to a `collection` or `process` manifest (these manifests can then point to other resources as needed).

`title` (optional)

A title or label for the resource.

`description` (optional)

A prose description of the resource.

## Discussion

A minimal Project manifest will look like this:

```json
"id": "project_name",
"contributors": [{
  "title": "Mickey Mouse"
}],
"created": "2017-10-06",
"resources": [{
  "name": "collection_id",
  "path": "path_to_collection_manifest"
}]
```

The properties `title`, `name`, and `path` are all borrowed from Frictionless Data and may be a little confusing in the context of the WE1S schema. Perhaps they should be changed?