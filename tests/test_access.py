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

def test_keys():
    l = Lict(0.1, 0.2, meta3=0.3, meta4=0.4)
    assert l.keys() == [None, 'meta3', 'meta4']

def test_values():
    l = Lict(0.1, 0.2, meta3=0.3, meta4=0.4)
    assert l.values() == [0.1, 0.2, 0.3, 0.4]

def test_items():
    l = Lict(0.1, 0.2, meta3=0.3, meta4=0.4)
    assert l.items() == [(None,0.1), (None,0.2), ('meta3',0.3), ('meta4',0.4)]

def test_select():
    l = Lict(0.1, 0.2, meta3=0.3, meta4=0.4)
    assert l.select()        == [0.1, 0.2]
    assert l.select('meta3') == [('meta3', 0.3)]
    assert l.select('meta4') == [('meta4', 0.4)]
