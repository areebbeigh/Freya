from utils.htmlparsers import NewsFeedParser

import unittest


class NewsFeedParserTestCase(unittest.TestCase):
    def test_parser(self):
        raw_clean_html = {
            "this is a <h2>simple</h2><p>html string</p>": "this is a simple html string",
            "<p><h2></h2></p>": "",
            "hello world! <img src=\"hello_word.png\" alt=\"yo\">": "hello world!",
            "<!DOCTYPE html><html><body><h2>kinetic theory of gases</h2></body></html>": "kinetic theory of gases"
        }

        for raw_html, clean_value in raw_clean_html.items():
            data = []
            NewsFeedParser(data).feed(raw_html)
            self.assertEqual(" ".join(data), clean_value)


if __name__ == "__main__":
    unittest.main()
