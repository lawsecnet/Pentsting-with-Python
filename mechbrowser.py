#
# Tool for downloading webpages' source code using mechanize
#

import mechanize

page_url = raw_input("provide page address (without 'http://'):")

def viewPage(url):
  browser = mechanize.Browser()
  page = browser.open(url)
  source_code = page.read()
  print source_code

viewPage("http://" + page_url)
