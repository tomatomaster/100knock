import britainWiki
import json
import re

pattern = r".*Category.*"
repattern = re.compile(pattern)
article = britainWiki.citeBritainArticle()
for line in article.splitlines():
    matcher = repattern.search(line)
    if matcher:
        print(matcher.group())
