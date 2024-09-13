def print_sitemap(sitemap):
    print(sitemap)

def save_sitemap(sitemap, filename):
    with open(filename, 'w') as f:
        f.write(sitemap)