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

l = Lict(
    a=0.1,
    b=0.2,
    c=0.3,
    d=0.4,
)

def test_ungroup():
    u = l.ungroup('kind')
    assert u == [
        [0.1, ('kind', 'a')],
        [0.2, ('kind', 'b')],
        [0.3, ('kind', 'c')],
        [0.4, ('kind', 'd')],
    ]
