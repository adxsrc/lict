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

from metainer import *
import pytest

def test_init_arg():
    m = Metainer(0.1)
    assert m == [(None, 0.1)]

def test_init_args():
    m = Metainer(0.1, 0.2, 0.3)
    assert m == [(None, 0.1), (None, 0.2), (None, 0.3)]

def test_init_kwargs():
    m = Metainer(meta1=0.1, meta2=0.2, meta3=0.3)
    assert m == [('meta1', 0.1), ('meta2', 0.2), ('meta3', 0.3)]

def test_init_mixed():
    m = Metainer(0.1, 0.2, meta3=0.3, meta4=0.4)
    assert m == [(None, 0.1), (None, 0.2), ('meta3', 0.3), ('meta4', 0.4)]
