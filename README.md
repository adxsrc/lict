# `Lict`

`Lict` is a hybrid list-dict container.
It supports metadata-based object management by allowing its
keys/names to be transformed seamlessly among hierarchical, flat, and
mixed structures.
Its simple, flexible, and transformable design is ideal for building
interpolatable python classes.


## Basic Licts

A trivial lict does not have any metadata.
Logically, it is simply a boxed python data object:

    trivial = [data]                                                        (1)

A simple (non-trivial) lict contains multiple data objects and
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
`'meta'`, can be used as lict's metakey; any python object `meta1`,
..., including another lict, can be used as lict's metadata.


## Hierarchical Licts

`Lict` is designed for hierarchical origination of data and metadata.
Its power comes from nesting different levels of licts together.

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
lict hierarchy.

Alternatively, We are also free to use licts for data and metadata:

    hierarchical = [                                                        (4)
        data1,
        [data2, kkey2:keyd1],
        ...,
        mkey1:meta1,
        mkey2:[meta2, kkey2:keyd2, ...],
        ...,
    ]


## Flattening and Grouping

If we turn `hierarchical`'s KMPs into licts, we obtain

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

Conversely, we may "group" this lict according to `kkey2`, which
results:

    hierarchical -> [                                                       (7)
        data1,
        keyd1:data2,
        ...,
        [meta1, kkey1:mkey1],
        keyd2:[meta2, kkey1:mkey2, ...],
        ...,
    ]

This lict is very similar to the original definition of
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


## Default Grouping/Mount and Behaviors

Form (8) demonstrates that the default values of `hierarchical`
depends on how its metadata are grouped.
In general, even the number of default data objects can depends on the
grouping.

Licts has three features to address this.

1. It is possible to set the default grouping/mount.
   This allows users to adjust the view of a lict according to its
   application.

2. There are use cases that we need multiple views of the same lict.
   It is possible to create additional views based on a different
   default grouping/mount.

3. Because the default values and/or a key may return multiple data
   objects, lict data access always return a new lict that contains
   the proper data objects.

A lict propagates its method calls to its data but not its metadata.
Hence,

    simple.method() -> simple.data1.method(); simple.data2.method()

This is similar to applying a function to a numpy array---the function
is applied on the array itself but but not metadata.
It is also possible to use descriptors as metakeys, so the metadata
can be derived dynamically from the data.


## Implementation

There are multiple ways to implement lict.
In fact, form (6) suggests that it is possible to track all the
metakeys and metadata in a numpy record array or a pandas dataframe.
Nevertheless, to maximize portability, we provide a simple
implementation that only uses python's built-in data structures.
Although some of the operations may scales as O(N^2), we do not expect
lict to be a performance bottleneck because the number of fields in a
python object should be relatively small.

The hierarchical examples above demostrate that licts are lists of
three things: 1) data objects, 2) KMPs, and 3) another licts.
This leads to two natural ways to implement licts.

Since KMPs is never needed outside lict's own algorithm, we may
introduce a nested `Pair` class insider the `Lict` class to track all
the KMPs.
We can perform the `isinstance()` check against `Lict` and `Pair` to
distinglish the multiple cases.

Alternatively, we may simply define a `Lict` as a list of two-tuple,
and introduce a special key, e.g., `None`, to track the unkeyed data
object.
I.e.,

    normalized = [
        (None, unkeyed_object),
        ...
        (key,  keyed_object),
        ...
    ]

While this second approach is more uniform, and hence easier to
implement, it makes returning a grouping result more tricky.
Should we return a normal python list?
Or should we return a `Lict` and pay the price that the returned list
contains pairs instead of the objects themselves.
