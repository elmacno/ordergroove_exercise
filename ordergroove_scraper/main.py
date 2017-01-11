import operator
import urllib2
import sys
from HTMLParser import HTMLParser

class HtmlTagCounter(HTMLParser):
  def __init__(self):
    HTMLParser.__init__(self)
    self.tags = {}

  def handle_starttag(self, tag, attrs):
    if not tag in self.tags:
      self.tags[tag] = 1
    else:
      self.tags[tag] = self.tags[tag] + 1

  def metrics(self):
    return self.tags

class Scraper:
  def scrape(self, url="http://ordergroove.com/company", max_tags=5):
    page_contents = ""
    try:
      response = urllib2.urlopen(url)
      page_contents = response.read()
    except:
      sys.stderr.write("An error occurred fetching %s"%(url))
    tag_counter = HtmlTagCounter()
    tag_counter.feed(page_contents)
    metrics = tag_counter.metrics()

    tag_count = len(metrics)
    top_tags = sorted(metrics.items(), key=operator.itemgetter(1), reverse=True)[:max_tags]
    return tag_count, top_tags

def scraper():
    return Scraper()
