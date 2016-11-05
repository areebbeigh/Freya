"""
   Copyright 2016 Areeb Beigh

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""

import json
import os

from .PreferenceObject import PreferenceObject

BASE_DIRECTORY = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

with open(os.path.join(BASE_DIRECTORY, "config.json"), "r") as f:
    _config_object = json.load(f)

for key, value in _config_object.items():
    # An attempt to keep the values in the lower case
    try:
        for k, v in value.items():
            if isinstance(v, str):
                _config_object[key][k] = v.lower()
            if isinstance(v, list):
                for string in v:
                    if isinstance(string, str):
                        v[v.index(string)] = string.lower()
    except Exception as e:
        pass


def get_phrases():
    """ Returns a phrases dictionary of the form <callback>:<list of phrases> """
    return _config_object["phrases"]


def get_preferences():
    """ Returns a preference object with the preferences """
    return PreferenceObject(_config_object["preferences"])
