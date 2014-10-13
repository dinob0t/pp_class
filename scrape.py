import time
import random
import csv

import numpy as np

import Image as im

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from bs4 import BeautifulSoup
import urllib

browser = webdriver.Chrome()

total_images = 1

for page in range(1,37):

	browser.get("https://www.paperlesspost.com/cards?page=" + str(page))
	time.sleep(2*random.random())

	soup = BeautifulSoup(browser.page_source)
	thumbs = soup.findAll('img')

	image_list = []
	count = 0
	while count < len(thumbs):
		cur_thumbs_href = thumbs[count]['src']
		cur_thumbs_href_str = str(cur_thumbs_href)
		if 'media' in cur_thumbs_href_str or 'grid' in cur_thumbs_href_str:
			image_list.append(cur_thumbs_href_str)
			print cur_thumbs_href	
		count +=1

	for img_str in image_list:
		success = 0
		try:
			dl = urllib.urlopen(img_str).read()
			success = 1

		except:

			pass

		if success == 1:
			f = open('data/' + str(total_images) + '.jpg','wb')
			f.write(dl)
			f.close()
			total_images +=1

browser.quit()