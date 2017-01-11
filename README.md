# OrderGroove Scraper Exercise

This scraper counts the number of html tags in a given web page and displays the top 5 tags and their count

## Usage
### CLI Usage
Example:
```sh
$ ordergroove-scraper
```

Sinopsis:
```sh
$ ordergroove-scraper [flags] [URL]
```

See ```ordergroove-scraper --help```

### Programatic Usage
Example:
```python
import ordergroove-exercise

scraper = ordergroove-exercise.scraper()

target_url="http://ordergroove.com/company"
(tag_count, top_tags) = scraper.scrape(url=target_url,
                                       max_tags=5)
print("The number of tags in '%s' is %d"%(target_url, tag_count))
print("The top %d tags are:"%(len(top_tags)))
for (tag, count) in top_tags:
   print("\tTag '%s' appeared %d times"%(tag, count))
```
