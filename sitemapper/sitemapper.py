import argparse
import sys
from sitemap import generate_sitemap
from utils import print_sitemap, save_sitemap

def sitemapper():
    parser = argparse.ArgumentParser(description="Sitemap generator")
    parser.add_argument('url', help='URL to generate sitemap for')
    parser.add_argument('-g', '--generate', help='Generate sitemap and save to file', action='store_true')
    parser.add_argument('-s', '--stdout', help='Print sitemap to stdout', action='store_true')
    parser.add_argument('-i', '--info', help='Print information about the sitemap generator', action='store_true')
    parser.add_argument('-h', '--help', help='Print help message', action='help')
    parser.add_argument('-o', '--output', help='Output file name', default='sitemap.xml')

    args = parser.parse_args()

    if args.generate:
        sitemap = generate_sitemap(args.url)
        save_sitemap(sitemap, args.output)
        print(f"Sitemap generated and saved to {args.output}")
    elif args.stdout:
        sitemap = generate_sitemap(args.url)
        print_sitemap(sitemap)
    elif args.info:
        print("Sitemap generator version 1.0")
        print("Copyright 2023")
    else:
        parser.print_help()

if __name__ == "__main__":
    sitemapper()