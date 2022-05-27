import requests
from bs4 import BeautifulSoup

URL = f'https://stackoverflow.com/jobs/companies'

# 회사 이름 추출 함수
def extract_company_name():
  company_names = []

  result = requests.get(URL)
  # print(result)
  
  soup = BeautifulSoup(result.text, 'html.parser')
  # print(soup)
  
  every_job_card = soup.find_all("div",{"class":"dismissable-company"})
  # print(each_card)
  


  for each_job_card in every_job_card:
    head = each_job_card.find("h2", {"class":"fs-body2 mb4"})
    company_name = head.find("a", {"class":"s-link"}).text
    company_names.append(company_name)

  return company_names

  



  
    