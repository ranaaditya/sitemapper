from setuptools import setup

setup(
    name='sitemapper',
    version='1.0',
    py_modules=['sitemapper'],
    install_requires=['requests', 'beautifulsoup4'],
    entry_points={
        'console_scripts': ['sitemapper=sitemapper:sitemapper'],
    },
)