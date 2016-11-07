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


class PreferenceObject:
    """ A read-only preference object with the configuration preferences. """

    def __init__(self, preference_dict):
        self.preferences = preference_dict

    def get_trigger_keyword(self):
        return self.preferences["TRIGGER_KEYWORD"]

    def get_music_dir(self):
        return self.preferences["MUSIC_DIRECTORY"]

    def get_search_engine(self):
        return self.preferences["SEARCH_ENGINE"]

    # TODO: Intended for getting weather updates from an online API, haven't implemented it yet.
    '''
    def get_zipcode(self):
        return self.preferences["ZIPCODE"]
    '''

    def get_print_cmds_on_start(self):
        return True if self.preferences["PRINT_COMMANDS_ON_START"] == "true" else False

    def get_print_subtitle(self):
        return True if self.preferences["PRINT_SUBTITLES"] == "true" else False

    def get_news_feed_urls(self):
        return self.preferences["NEWS_FEED"]

    def get_user_gender(self):
        return self.preferences["GENDER"]

    def get_user_title(self):
        """ Determine the user title - mam or sir :) """
        return "mam" if self.get_user_gender() == "female" else "sir"
