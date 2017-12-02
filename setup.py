#!/usr/bin/env python3
#
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

from setuptools import setup, find_packages

setup(
    name='metainer',
    version='0.1.0',
    url='https://github.com/hallmarksrc/metainer',
    author='Chi-kwan Chan',
    author_email='ckchan@cfa.harvard.edu',
    description='A metadata-based container for building interpolatable python classes',
    packages=find_packages('mod'),
    package_dir={'': 'mod'},
    python_requires='>=3.6', # `metainer` uses python3's f-string and typing
)