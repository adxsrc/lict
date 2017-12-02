# `Metainer`

`Metainer` is a simple, flexible, and transformable metadata-based
container for building interpolate data classes.
It is similar to a python dictionary or namedtuple, except its
keys/names can be transformed seamlessly among hierarchical, flat, and
mixed structures.

## Basic Metainers

A trivial metainer does not have any metadata.
Logically, it is simply a boxed python data object:

    trivial ~ [data]

A simple (non-trivial) metainer contains multiple data objects and
metakey-metadata pairs:

    simple ~ [
        data1,
        data2,
        ...
        mkey1:meta1,
        mkey2:meta2,
        ...,
    ]

Any hashable python object `mkey1`, ..., which may be a string like
`'meta'`, can be used as metainer's metakey; any python object
`meta1`, ..., including another metainer, can be used as metainer's
metadata.
