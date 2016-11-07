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

from html.parser import HTMLParser


class NewsFeedParser(HTMLParser):
    def __init__(self, target_list):
        """
         A parser for the news feeds, currently only removes tags from the content to read aloud
         Parameters:
                target_list: Reference to a list object to load the non-html data into.
        """
        super().__init__()
        self.data_list = target_list

    def error(self, message):
        pass

    def handle_data(self, data):
        self.data_list.append(data.strip())
