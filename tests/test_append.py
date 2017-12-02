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

import pytest

l = Lict()

def test_append_strkey():
    l.append('meta', 0.1)
    assert l == [('meta', 0.1)]

def test_append_kwarg():
    l.append(meta=0.2)
    assert l == [('meta', 0.1), ('meta', 0.2)]

def test_append_hashablekey():
    l.append(0.3)
    assert l == [('meta', 0.1), ('meta', 0.2), (None, 0.3)]

def test_append_unhashablekey():
    with pytest.raises(TypeError) as e:
        l.append([], 0.4)
    assert l == [('meta', 0.1), ('meta', 0.2), (None, 0.3)]
    assert str(e.value) == "unhashable type: 'list'"

def test_append_args():
    with pytest.raises(ValueError) as e:
        l.append(0.4, 0.5, 0.6)
    assert l == [('meta', 0.1), ('meta', 0.2), (None, 0.3)]
    assert str(e.value) == "append() takes exactly one metakey:metadata pair"

def test_append_kwargs():
    with pytest.raises(ValueError) as e:
        l.append(meta4=0.4, meta5=0.5, meta6=0.6)
    assert l == [('meta', 0.1), ('meta', 0.2), (None, 0.3)]
    assert str(e.value) == "append() takes exactly one metakey:metadata pair"
