import requests
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
from datetime import datetime

def generate_sitemap(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        urls = []

        for link in soup.find_all('a'):
            href = link.get('href')
            if href and href.startswith('/'):
                urls.append(url + href)
            elif href and href.startswith('http'):
                urls.append(href)

        root = ET.Element("urlset")
        root.set("xmlns", "http://www.sitemaps.org/schemas/sitemap/0.9")
        root.set("xmlns:xhtml", "http://www.w3.org/1999/xhtml")

        for url in urls:
            doc = ET.SubElement(root, "url")
            ET.SubElement(doc, "loc").text = url
            ET.SubElement(doc, "lastmod").text = datetime.now().strftime("%Y-%m-%dT%H:%M:%S+00:00")
            ET.SubElement(doc, "changefreq").text = "monthly"
            ET.SubElement(doc, "priority").text = "0.5"

        return ET.tostring(root, encoding="unicode")
    except Exception as e:
        print(f"Error generating sitemap: {e}")