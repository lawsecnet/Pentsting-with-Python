#
# Tool for downloading webpages' source code using mechanize
#

import mechanize

def main():

    url = raw_input("Provide page address:")
    browser = mechanize.Browser()
    page = browser.open('http://' +url)
    source_code = page.read()
    print source_code
