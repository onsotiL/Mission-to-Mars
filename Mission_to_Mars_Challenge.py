#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


# In[3]:


#set the executable path, then set up the URL
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[4]:


# Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[5]:


#assign the url and instruct the browser to visit it.
# Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)
# Optional delay for loading the page
# searching for elements with a specific combination of tag (div) and attribute (list_text).
# tells the browser to wait one second before searching for components.
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[6]:


#set up the HTML parser:
html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')


# In[7]:


# add .find to the previously assigned variable, slide_elem.
# we're saying, "This variable holds a ton of information, so look inside of that information to find this specific data." 

slide_elem.find('div', class_='content_title')


# In[8]:


# to get just the text, and get rid of the extra HTML stuff .get_text()
# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[9]:


# scape the summary text: 10.3.3 ASK IRENE
# We’ll need to change the class to “article_teaser_body.” 
# this is unique class associated with the summary.
slide_elem.find('div', class_='content_title').get_text()


# In[10]:


##### find tags and attributes with BeautifulSoup:
###### .find() is used when we want only the first class and attribute we've specified.
###### .find_all() is used when we want to retrieve all of the tags and attributes.


# In[11]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ### Featured Images 

# In[12]:


# set up/Visit the URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[13]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[14]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')


# In[15]:


# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel
# the result is just a partial url, include the the base URL to create an absolute url


# In[16]:


# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# In[17]:


df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df


# In[18]:


browser.quit()


# #### Challenge: Deliverable 1

# In[3]:


# Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager


# In[4]:


# Set the executable path and initialize Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# ##### Visit the NASA Mars News Site

# In[8]:


# Visit the mars nasa news site
url = 'https://redplanetscience.com/'
browser.visit(url)

# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[9]:


# Convert the browser html to a soup object and then quit the browser
html = browser.html
news_soup = soup(html, 'html.parser')

slide_elem = news_soup.select_one('div.list_text')


# In[13]:


slide_elem.find('div', class_='content_title')


# In[14]:


# Use the parent element to find the first a tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[15]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# JPL Space Images Featured Image¶

# In[16]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[17]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[18]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')
img_soup


# In[19]:


# find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[20]:


# Use the base url to create an absolute url
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# Mars Facts

# In[21]:


df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.head()


# In[22]:


df.columns=['Description', 'Mars', 'Earth']
df.set_index('Description', inplace=True)
df


# In[23]:


df.to_html()


# D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles¶

# Hemispheres

# In[24]:


# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'

browser.visit(url)


# In[28]:


# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

# 3. Write code to retrieve the image urls and titles for each hemisphere.
for i in range(4):
    hemispheres = {}
    browser.find_by_css('a.product-item h3')[i].click()
    element = browser.links.find_by_text('Sample').first
    img_url = element['href']
    title = browser.find_by_css("h2.title").text
    hemispheres["img_url"] = img_url
    hemispheres["title"] = title
    hemisphere_image_urls.append(hemispheres)
    browser.back()


# In[29]:


# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls


# In[30]:


# 5. Quit the browser
browser.quit()


# In[ ]:





# In[ ]:




