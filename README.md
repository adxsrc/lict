# `Metainer`

`Metainer` is a simple, flexible, and transformable metadata-based
container for building interpolate data classes.
It is similar to a python dictionary or namedtuple, except its
keys/names can be transformed seamlessly among hierarchical, flat, and
mixed structures.


## Basic Metainers

A trivial metainer does not have any metadata.
Logically, it is simply a boxed python data object:

    trivial = [data]                                                        (1)

A simple (non-trivial) metainer contains multiple data objects and
key-metadata pairs (KMPs):

    simple = [                                                              (2)
        data1,
        data2,
        ...,
        mkey1:meta1,
        mkey2:meta2,
        ...,
    ]

Any hashable python object `mkey1`, ..., which may be a string like
`'meta'`, can be used as metainer's metakey; any python object
`meta1`, ..., including another metainer, can be used as metainer's
metadata.


## Hierarchical Metainers

`Metainer` is designed for hierarchical origination of data and
metadata.
Its power comes from nesting different levels of metainers together.

In the above example, the metakeys themselves can be seen as metadata
of the metadata.
By giving them a new name, e.g., "kind key" `kkey1`, we can "deepen"
the hierarchy as:

    simple -> [                                                             (3)
        data1,
        data2,
        ...,
        [meta1, kkey1:mkey1],
        [meta2, kkey1:mkey2],
        ...,
    ]

The metadata `meta1` and `meta2` now are simply data nested in deeper
metainer hierarchy.

Alternatively, We are also free to use metainers for data and
metadata:

    hierarchical = [                                                        (4)
        data1,
        [data2, kkey2:keyd1],
        ...,
        mkey1:meta1,
        mkey2:[meta2, kkey2:keyd2, ...],
        ...,
    ]


## Flattening and Grouping

If we turn `hierarchical`'s KMPs into metainers, we obtain

    hierarchical -> [                                                       (5)
        data1,
        [data2, kkey2:keyd1],
        ...,
        [meta1, kkey1:mkey1],
        [[meta2, kkey2:keyd2, ...], kkey1:mkey2],
        ...,
    ]

We can then "flatten" the hierarchical as `kkey1:mkey2`,
`kkey2:keyd2`, ..., are all KMPs associated with `meta2`:

    hierarchical -> [                                                       (6)
        data1,
        [data2, kkey2:keyd1],
        ...,
        [meta1, kkey1:mkey1],
        [meta2, kkey1:mkey2, kkey2:keyd2, ...],
        ...,
    ]

Conversely, we may "group" this metainer according to `kkey2`, which
results:

    hierarchical -> [                                                       (7)
        data1,
        keyd1:data2,
        ...,
        [meta1, kkey1:mkey1],
        keyd2:[meta2, kkey1:mkey2, ...],
        ...,
    ]

This metainer is very similar to the original definition of
`hierarchical`.
If we reorder the content in the above form and compare it
side-by-side with the original definition, they become

    hierarchical = [                     ~~> [                              (8)
        data1,                               data1,
        [data2, kkey2:keyd1],                [meta1, kkey1:mkey1],
        ...,                                 ...,
        mkey1:meta1,                         keyd1:data2,
        mkey2:[meta2, kkey2:keyd2, ...],     keyd2:[meta2, kkey1:mkey2, ...],
        ...,                                 ...,
    ]                                    ]


## Behaviors

A metainer propagates its method calls to its data but not its
metadata.
Hence,

    simple.method() -> simple.data1.method(); simple.data2.method()

This is similar to applying a function to a numpy array---the function
is applied on the array itself but but not metadata.
It is also possible to use descriptors as metakeys, so the metadata
can be derived dynamically from the data.
