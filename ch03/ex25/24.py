import re
import britainWiki

article = britainWiki.citeBritainArticle()
matcher = re.compile('^ファイル:(.*)\|\[\[(.*)\]\]$')
for line in article.splitlines():
    match = matcher.search(line)
    if match != None:
        print(match.group(1))
