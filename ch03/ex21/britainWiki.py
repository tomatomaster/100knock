import json


def citeBritainArticle():
    for row in open('/Users/ono/dev/100knock/ch03/jawiki-country.json', 'r'):
        article = json.loads(row)
        if "イギリス" == article["title"]:
            return article["text"]
