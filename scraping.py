#!/usr/bin/env python
# coding: utf-8

# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


#set the executable path, then set up the URL
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


#assign the url and instruct the browser to visit it.
# Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)
# Optional delay for loading the page
# searching for elements with a specific combination of tag (div) and attribute (list_text).
# tells the browser to wait one second before searching for components.
browser.is_element_present_by_css('div.list_text', wait_time=1)


#set up the HTML parser:
html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')

# add .find to the previously assigned variable, slide_elem.
# we're saying, "This variable holds a ton of information, so look inside of that information to find this specific data." 

slide_elem.find('div', class_='content_title')

# to get just the text, and get rid of the extra HTML stuff .get_text()
# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# scape the summary text: 10.3.3 ASK IRENE
# We’ll need to change the class to “article_teaser_body.” 
# this is unique class associated with the summary.
slide_elem.find('div', class_='content_title').get_text()



##### find tags and attributes with BeautifulSoup:
###### .find() is used when we want only the first class and attribute we've specified.
###### .find_all() is used when we want to retrieve all of the tags and attributes.


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ### Featured Images 

# set up/Visit the URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')


# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel
# the result is just a partial url, include the the base URL to create an absolute url


# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url

# ## Mars Facts

df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.head()

df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df

df.to_html()

browser.quit()



