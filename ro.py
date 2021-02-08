import requests 
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}


def extract_job(html):
  title = html.find("h2",{"itemprop":"title"}).get_text()
  company = html.find("h3",{"itemprop":"name"}).get_text()
  location = html.find("div",{"class":"location"})
  if location:
    location = location.get_text()
  link = html.find("a",{"class":"preventLink"})["href"]
  link = f"http://remoteok.io{link}"
  

  return {"title":title,"company":company,"location":location, "link" : link}

def extract_jobs(URL):
  jobs = []
  result = requests.get(f"{URL}",headers=headers)
  print(result)
  soup = BeautifulSoup(result.text, "html.parser")
  results = soup.find_all("tr",{"class":"job"})
  for result in results:
    job = extract_job(result)
    jobs.append(job)
  return jobs

def get_jobs(keyword):
  URL= f"https://remoteok.io/remote-dev+{keyword}-jobs"
  print(URL)
  jobs = extract_jobs(URL)
  return jobs