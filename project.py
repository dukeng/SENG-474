from lxml import html
import requests, json
import re, csv
from bs4 import BeautifulSoup

# page = requests.get('https://api.diffbot.com/v3/article', params = parameter)
# json_data = json.loads(page.text)
# objects = json_data["objects"]

# parsed = json.loads(page.text)

# print (json.dumps(parsed, indent=4, sort_keys=True))

# print(objects[0]["text"])

# with open('out.txt', 'w') as output:
#     output.write(objects[0]["text"])



def write_data(url, writeToFile):
	parameter = {'url': url,  
		'token':'b261e10466c562a240b0751db22c4378'}
	page = requests.get('https://api.diffbot.com/v3/article', params = parameter)
	json_data = json.loads(page.text)
	check = "objects"
	if check in json_data.keys():
		objects = json_data["objects"]
		print("Getting info from", url)
		text = objects[0]["text"]
		text = text.replace('\n', ' ').replace('\r', '')
		title = objects[0]["title"]
		# print(title)
		if len(text) > 150:
			writeToFile.writerow({'title': title, 'text': text, 'type': 'fake'})
	else:
		print("url is invalid", url)


if __name__ == '__main__':
	urlFileName = 'fakenewsurl.txt'
	with open(urlFileName, 'r') as output, open('result4_fake_news.txt', 'w', encoding='utf-8') as result:
		content = output.readlines()
		fieldnames = ['title', 'text', 'type']
		writer = csv.DictWriter(result, fieldnames=fieldnames)
		writer.writeheader()
		count = 0
		for url in content:
			count += 1
			if count < 2000 and count > 0:
				print (count)
				write_data(url, writer)

def find_matching_links(html):
	return re.findall('href="http://www.cnn.com/([^#:"]*)"', html)

def get_page_html(url):
	page = requests.get(url)
	print (url)
	return page.content.decode('utf-8')




