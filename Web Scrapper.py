import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:/Users/Jordy/Documents/chromedriver.exe')
driver.get('http://oxylabs.io/blog')
results = []
other_results = []
content = driver.page_source
soup = BeautifulSoup(content, features="html.parser")
driver.quit()

for a in soup.findAll(attrs='blog-cardcontent-wrapper'):
    name = a.find('h2')
    if name not in results:
        results.append(name.text)

for b in soup.findAll(attrs='blog-carddate-wrapper'):
    date = b.find('p')
    if date not in results:
        other_results.append(date.text)

df = pd.DataFrame({'Names': results, 'Dates': other_results})
df.to_csv('names.csv', index=False, encoding='utf-8')