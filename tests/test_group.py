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

l1 = 0.1
l2 = 0.2
l3 = Lict(0.3, kind='data')
l4 = Lict(0.4, kind='data')
l5 = Lict(0.5, kind='meta')
l6 = Lict(0.6, kind='meta')

def test_group():
    l = Lict(l1, l2, l3, l4, l5, l6)

    g = l.group('kind')
    assert g.keys()   == [None, 'data', 'meta']
    assert g.values() == [l1, l2, l3, l4, l5, l6]

    d = g.filter(None)
    assert d.values() == [l1, l2]

    d = g.filter('data')
    assert d.values() == [l3, l4]

    e = g.filter('meta')
    assert e.values() == [l5, l6]

def test_ungroup():
    l = Lict(l1,b=l2)
    l.append(  l3)
    l.append(d=l4)
    l.append(  l5)
    l.append(f=l6)

    u = l.ungroup('kind')
    assert u == [
         0.1,
        [0.2,                   ('kind', 'b')],
        [0.3, ('kind', 'data')               ],
        [0.4, ('kind', 'data'), ('kind', 'd')],
        [0.5, ('kind', 'meta')               ],
        [0.6, ('kind', 'meta'), ('kind', 'f')],
    ]
    # TODO: make sure that Lict.ungroup() do not modify l1, l2, ..., l6
