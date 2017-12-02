# Copyright 2017 Chi-kwan Chan
# Copyright 2017 Harvard-Smithsonian Center for Astrophysics
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

class Lict(list):
    """Lict

    `Lict` is a hybrid list-dict container.  It supports
    metadata-based object management by allowing its keys/names to be
    transformed seamlessly among hierarchical, flat, and mixed
    structures.  Its simple, flexible, and transformable design is
    ideal for building interpolatable python classes.

    """

    #==========================================================================
    class _Pair(tuple):
        """_Pair

        Because lict's metakey-metadata pairs (MKDPs) are never needed
        outside lict's own algorithm, we introduce this nested `_Pair`
        class inside the `Lict` class to track all the MKDPs.  We can
        perform the isinstance() check against `Lict` and `_Pair` to
        distinguish the nature of the items in `Lict`.

        """
        def __new__(cls, item):
            hash(item[0]) # raise a TypeError if unhashable
            return super().__new__(cls, item)

    #==========================================================================
    def __init__(self, *args, **kwargs):
        for arg in args:
            self.append(arg)
        for k, v in kwargs.items():
            self.append(k, v)

    def append(self, *args, **kwargs):
        lens = len(args), len(kwargs)

        # Handle unkeyed value
        if   lens == (1, 0):
            item = args[0]
        elif lens == (2, 0) and args[0] is None:
            item = args[1]

        # Handle keyed value
        elif lens == (2, 0):
            item = self._Pair(args)
        elif lens == (0, 1):
            item = self._Pair(*kwargs.items())

        # Invalid input
        else:
            raise ValueError("append() takes exactly one metakey:metadata pair")

        # Really append
        super().append(item)
