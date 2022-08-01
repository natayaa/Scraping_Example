import requests
import csv

from bs4 import BeautifulSoup

def gather_info():
	url = "#Insert URL"
	headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
	result = requests.get(url, headers=headers).text
	supbasah = BeautifulSoup(result, 'html.parser')
	all_pages = supbasah.find(class_="#Insert the class you want to search for")
	pages_count = all_pages.text
	
	results = supbasah.find(class_="content")
	for content in results:
		parent = content.parent
		if parent.name != 'a':
			continue

		link = parent['href']
		next_parent = content.find_parent(class_="result")
		try:
			judul = next_parent.find(class_="")

if __name__ == '__main__':
	gather_info()
  
