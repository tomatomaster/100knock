import re
import britainWiki

article = britainWiki.citeBritainArticle()
matcher = re.compile('Category:.*')
for line in article.splitlines():
    match = matcher.search(line)
    if match != None:
        g = match.group(0)
        g = g.replace(']]', '')
        g = g.replace('Category:', '')
        # print(g)

# ^先頭
# \[\[
# Category:
# (.*?)
# (\|.*)
# \]\]
# $終端
article = britainWiki.citeBritainArticle()
matcher = re.compile("^\[\[Category:(.*?)(\|.*)*\]\]$")
for line in article.splitlines():
    print(line)
    match = matcher.search(line)
    if match is not None:
        g = match.group(1)
        print(g)
