import unittest
from render import render
from html.parser import HTMLParser
class Links(HTMLParser):
    def __init__(self):
        super().__init__(); self.links = []
    def handle_starttag(self, tag, attrs):
        if tag == 'a': self.links.append(dict(attrs)['href'])
class Tests(unittest.TestCase):
    def test_same_destination_and_escaping(self):
        url = 'https://example.com/reset?token=a&next="quoted"'
        html, text = render(url, 15)
        parser = Links(); parser.feed(html)
        self.assertEqual(parser.links, [url, url])
        self.assertIn('&amp;', html); self.assertIn('&quot;', html)
        self.assertIn(url, text)
        for body in (html, text):
            self.assertIn('15 minutes', body); self.assertNotIn('{{', body)
    def test_invalid_urls(self):
        for url in ['javascript:alert(1)', 'http://example.com', '//example.com', 'https://u:p@example.com', 'https://example.com/\nInjected']:
            with self.assertRaises(ValueError): render(url)
    def test_expiry(self):
        for value in [0, 1441, '30', True]:
            with self.assertRaises(ValueError): render('https://example.com', value)
if __name__ == '__main__': unittest.main()
