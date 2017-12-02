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

def test_match_obj():
    d = 1
    assert     Lict._matchkey(d, None)
    assert not Lict._matchkey(d, 'x')
    assert not Lict._matchkey(d, 'y')

def test_match_Pair():
    p = Lict._Pair(('x', 1))
    assert not Lict._matchkey(p, None)
    assert     Lict._matchkey(p, 'x')
    assert not Lict._matchkey(p, 'y')

def test_match_Lict():
    l = Lict(1)
    assert     Lict._matchkey(l, None)
    assert not Lict._matchkey(l, 'x')
    assert not Lict._matchkey(l, 'y')
