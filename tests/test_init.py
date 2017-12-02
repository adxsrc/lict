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

def test_init_arg():
    l = Lict(0.1)
    assert l == [0.1]

def test_init_args():
    l = Lict(0.1, 0.2, 0.3)
    assert l == [0.1, 0.2, 0.3]

def test_init_kwargs():
    l = Lict(meta1=0.1, meta2=0.2, meta3=0.3)
    assert l == [('meta1', 0.1), ('meta2', 0.2), ('meta3', 0.3)]

def test_init_mixed():
    l = Lict(0.1, 0.2, meta3=0.3, meta4=0.4)
    assert l == [0.1, 0.2, ('meta3', 0.3), ('meta4', 0.4)]

def test_init_unboxing():
    l = Lict(0.1, 0.2, Lict(0.3, 0.4, Lict(0.5, 0.6)))
    assert l == [0.1, 0.2, 0.3, 0.4, 0.5, 0.6]
