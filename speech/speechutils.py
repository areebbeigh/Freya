"""
Speech recognition and synthesis related stuff

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

from callbacks.callbacks import *

import winspeech
from utils import configreader

TRIGGER_KEYWORD = configreader.get_preferences().get_trigger_keyword()
raw_phrases = configreader.get_phrases()
reverse = {tuple(value): key for key, value in raw_phrases.items()}
phrases = {}  # {<phrases>:<callback function name string>}


def _prepend_trigger_keyword(phrase):
    return TRIGGER_KEYWORD + " " + phrase


def initialize():
    """ Start listening for phrases """
    for phrase_tuple in raw_phrases.values():
        new_phrase_list = []
        for phrase in phrase_tuple:
            if phrase[0] != "*":
                new_phrase_list.append(phrase)
            else:
                # If the command has a wild card we'll append both versions i.e the command on its own
                # and the command prepended by the trigger keyword
                new_phrase_list.append(phrase[1:])
                new_phrase_list.append(_prepend_trigger_keyword(phrase[1:]))

        phrases[tuple(new_phrase_list)] = reverse[tuple(phrase_tuple)]

    for phrase_list in phrases.keys():
        winspeech.listen_for(phrase_list, eval(phrases[phrase_list]))
        #print(phrase_list)

    winspeech.listen_for_anything(default_listener)
