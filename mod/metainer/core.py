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

class Metainer(list):
    """Metainer

    A simple, flexible, and transformable metadata-based container for
    building interpolate data classes.  It is similar to a python
    dictionary or namedtuple, except its keys/names can be transformed
    seamlessly among hierarchical, flat, and mixed structures.

    """

    def append(self, key, value):
        hash(key)
        super().append((key, value))
