from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
ChromeDriverManager().install()
from selenium.webdriver.common.by import By
import pymysql
import re
from datetime import datetime
from selenium.common.exceptions import NoSuchElementException

browser = webdriver.Chrome()

conn = pymysql.connect(
    host='localhost',  
    user='root',       
    password='1234',  
    db='yes24',       
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

link_list = []

for i in range(1,4):
    url = f"https://www.yes24.com/Product/Category/BestSeller?categoryNumber=001&pageNumber={i}&pageSize=24"
    browser.get(url)

    datas = browser.find_elements(By.CLASS_NAME,'gd_name')

    for i in datas:
        link = i.get_attribute('href')
        link_list.append(link)


for link in link_list:
    
    browser.get(link)

    title = browser.find_element(By.CLASS_NAME,'gd_name').text
    author = browser.find_element(By.CLASS_NAME,'gd_auth').text
    publisher= browser.find_element(By.CLASS_NAME,'gd_pub').text

    #[publishing]
    publishing= browser.find_element(By.CLASS_NAME,'gd_date').text
    match = re.search(r'(\d+)년 (\d+)월 (\d+)일',publishing)
        
    if match:
        year, month, day = match.groups()
        data_obj = datetime(int(year),int(month),int(day))
        publishing = data_obj.strftime("%Y-%m-%d")
    else:
        publishing = "0000-00-00"

    #[rating]
    try:
        rating_element = browser.find_element(By.CLASS_NAME, "yes_b").text
        try:
            rating = float(rating_element)
        except ValueError:
            rating = 0
    except NoSuchElementException:
        rating = 0

    #[review]
    try:
        review = int(browser.find_element(By.CLASS_NAME,'txC_blue').text.replace(",", ""))
    except NoSuchElementException:
        review = 0
    except (ValueError, TypeError):
        review = 0

    sales = int(browser.find_element(By.CLASS_NAME,'gd_sellNum').text.split(" ")[2].replace(",", ""))
    prices = int(browser.find_element(By.CLASS_NAME,'yes_m').text[:-1].replace(",", ""))
    ranking = int(browser.find_element(By.CLASS_NAME,'gd_best').find_element(By.TAG_NAME,'dd').text.split(" ")[1][:-1])

    #[ranking_weeks]
    try:
        ranking_weeks = int(browser.find_element(By.CLASS_NAME,'gd_best').find_element(By.TAG_NAME,'dd').text.split(" ")[-1][:-1])
    except IndexError:
        ranking_weeks = 0

    with conn.cursor() as cur:
        sql = """INSERT INTO Books(title, author, publisher, publishing, rating, review, sales, price, ranking, ranking_weeks) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

        cur.execute(sql,(title, author, publisher, publishing, rating, review, sales, prices, ranking, ranking_weeks))
        conn.commit()

