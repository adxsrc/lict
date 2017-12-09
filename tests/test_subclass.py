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

from lict import *

class Sublict(Lict):
    pass

l = Sublict(0.1, 0.2, meta3=0.3, meta4=0.4)

def test_get():
    g = l.get()
    assert type(g) is Sublict and g == [0.1, 0.2]

    g = l.get('meta3')
    assert type(g) is Sublict and g == [0.3]

    g = l.get('meta4')
    assert type(g) is Sublict and g == [0.4]

    g = l.get('meta5', 0.5)
    assert type(g) is Sublict and g == [0.5]

def test_keys():
    g = l.keys()
    assert type(g) is Sublict and g == [None, 'meta3', 'meta4']

def test_values():
    g = l.values()
    assert type(g) is Sublict and g == [0.1, 0.2, 0.3, 0.4]

def test_items():
    g = l.items()
    assert type(g) is Sublict and g == [(None,   0.1), (None,   0.2), ('meta3',0.3), ('meta4',0.4)]

def test_filter():
    g = l.filter()
    assert type(g) is Sublict and g == [0.1, 0.2]

    g = l.filter('meta3')
    assert type(g) is Sublict and g == [('meta3', 0.3)]

    g = l.filter('meta4')
    assert type(g) is Sublict and g == [('meta4', 0.4)]
