import requests
import scrapy
import unittest

# Set the target webpage
url = 'http://172.18.58.238/spicyx/'
r = requests.get(url)
print(r.text)

print("Status Code:")
print("\t*", r.status_code)

h = requests.head(url)
print("Header:")
print("**********")

for x in h.headers:
    print("\t", x, ":", h.headers[x])
    print("**********")

#Modify headers user-agent
headers = {
    'User-Agent': 'Mobile'
}

url2 = 'http://172.18.58.238/headers.php'
rh = requests.get(url2, headers=headers)
print(rh.text)


class NewSpider(scrapy.Spider):
    name = "new_spider"
    start_urls = ['http://172.18.58.238/spicyx/']

    def parse(self, response):
        css_selector = 'img'
        for jpg in response.css(css_selector):
            newsel = '@src'
            yield {
                'Image Link': jpg.xpath(newsel).extract(),
            }

class Project(unittest.TestCase):

    def test_EngineType(self):
        print("Test Complete")

if __name__ == '__main__':
    unittest.main()

