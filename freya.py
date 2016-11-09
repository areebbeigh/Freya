"""
Run Freya.

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

import time
import winspeech

from speech import speechutils
from utils.configreader import get_preferences, get_phrases


def main():
    hour = time.localtime().tm_hour
    preferences = get_preferences()
    title = preferences.get_user_title()  # mam? sir?
    print_cmds = preferences.get_print_cmds_on_start()

    if hour < 12:
        greeting = "Good morning {},".format(title)
    else:
        greeting = "Good evening {},".format(title)

    winspeech.say(greeting + " what can I do for you?")
    speechutils.initialize()
    print("Freya is ready to take commands!")

    if print_cmds:
        print("Available commands:\n")
        phrase_dict = get_phrases()
        phrases = []

        for phrase_list in phrase_dict.values():
            phrases.extend(phrase_list)

        phrases.sort()

        for phrase in phrases:
            print("\t" + phrase)

        print()

    while winspeech.is_listening():
        pass


if __name__ == "__main__":
    main()
