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

l1 = Lict()
l2 = Lict(0.1, 0.2, 0.3, 0.4)
l3 = Lict(0.1, 0.2, meta3=0.3, meta4=0.4)
l4 = Lict(meta1=0.1, meta2=0.2, meta3=0.3, meta4=0.4)

def test_keys():
    assert l1.keys() == []
    assert l2.keys() == [None]
    assert l3.keys() == [None, 'meta3', 'meta4']
    assert l4.keys() == ['meta1', 'meta2', 'meta3', 'meta4']

def test_values():
    assert l1.values() == []
    assert l2.values() == [0.1, 0.2, 0.3, 0.4]
    assert l3.values() == [0.1, 0.2, 0.3, 0.4]
    assert l4.values() == [0.1, 0.2, 0.3, 0.4]

def test_items():
    assert l1.items() == []
    assert l2.items() == [(None,   0.1), (None,   0.2), (None,   0.3), (None,   0.4)]
    assert l3.items() == [(None,   0.1), (None,   0.2), ('meta3',0.3), ('meta4',0.4)]
    assert l4.items() == [('meta1',0.1), ('meta2',0.2), ('meta3',0.3), ('meta4',0.4)]

def test_select():
    assert l1.select()        == []
    assert l1.select('meta3') == []
    assert l1.select('meta4') == []

    assert l2.select()        == [0.1, 0.2, 0.3, 0.4]
    assert l2.select('meta3') == []
    assert l2.select('meta4') == []

    assert l3.select()        == [0.1, 0.2]
    assert l3.select('meta3') == [('meta3', 0.3)]
    assert l3.select('meta4') == [('meta4', 0.4)]

    assert l4.select()        == []
    assert l4.select('meta3') == [('meta3', 0.3)]
    assert l4.select('meta4') == [('meta4', 0.4)]
