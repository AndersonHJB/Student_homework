from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from urllib.parse import quote  #quote是用来编码转码，把中文转化成浏览器看懂的文字
from pyquery import PyQuery  #pyquery是解析包，用来获取页面HTML

KEYWORD='ipad'
browser=webdriver.Chrome('C:\\chromedriver_win32\\chromedriver.exe')
wait=WebDriverWait(browser,10)

def crawl_page():
	try:
		url='https://s.taobao.com/search?q='+quote(KEYWORD)
		browser.get(url)

		if page>1:
			page_box=wait.until(
				EC.presence_of_element_located(
					(by.css.SELECTOR,'.input J_Input')))
			subimit_button=wait.until(
				EC.presence_of_element_located(
					(by.css.SELECTOR,'.btn.J_Submit')))
			page_box.clear()
			page_box.send_keys(page)
			subimit_button.clilk()

		wait.until(
			EC.presence_of_element_located(
				(by.css.SELECTOR,'.m-itemlist .items .item')))

		get_products()

	except:
		crawl_page(page)

def get_products():
	html=browser.page_source
	doc=pyQuery(html)
	items=doc('.m-itemlist .items .item').items()
	for item in items:
		product={
		'title':item.find('.title').text(),
		'price':item.find('.price').text(),
		'image':item.find('.img').attr('alt')
		}
	print(product)

	with open('item.txt','a+',encoding='utf-8')as f:
		f.write(product)
		f.write('\n')    #换行

crawl_page(1)