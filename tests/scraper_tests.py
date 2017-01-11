import os
import sys
import unittest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import ordergroove_scraper

class ScraperTests(unittest.TestCase):
  def test_unreachable_url(self):
    scraper = ordergroove_scraper.scraper()
    (tag_count, top_tags) = scraper.scrape(url="http://non-existing-url.com")
    assert tag_count == 0
    assert top_tags == []

  def test_valid_html(self):
    scraper = ordergroove_scraper.scraper()
    test_html_file = "file://%s/test.html"%(os.path.abspath(os.path.dirname(__file__)))
    (tag_count, top_tags) = scraper.scrape(url=test_html_file)
    assert tag_count == 8
    assert len(top_tags) == 5
    assert top_tags[0] == ("li", 5)
    assert top_tags[1] == ("p", 4)
    assert top_tags[2] == ("div", 3)
    assert top_tags[3] == ("img", 2)
    assert top_tags[4] == ("body", 1)


if __name__ == "__main__":
  unittest.main()
