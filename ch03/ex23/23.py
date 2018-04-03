import re
import britainWiki

article = britainWiki.citeBritainArticle()
matcher1 = re.compile('^==([^=]).*==$')
matcher2 = re.compile('^===([^=]).*===$')
matcher3 = re.compile('^===([^=]).*===$')
for line in article.splitlines():
    match1 = matcher1.search(line)
    match2 = matcher2.search(line)
    match3 = matcher3.search(line)
    if match1 != None:
        print("{0}:{1}".format(match1.group(0), 1))
    elif match2 != None:
        print("{0}:{1}".format(match2.group(0), 2))
    elif match3 != None:
        print("{0}:{1}".format(match3.group(0), 3))
