import requests 
from bs4 import BeautifulSoup


def extract_job(html):
  title = html.find("span",{"class":"title"}).get_text()
  company = html.find("span",{"class":"company"}).get_text()
  location = html.find("span",{"class":"region"})
  if location:
    location = location.get_text()
  link = html.find("a")["href"]
  link = f"https://weworkremotely.com{link}"
  print(link)

  return {"title":title,"company":company,"location":location, "link" : link}

def extract_jobs(URL):
  jobs = []
  result = requests.get(f"{URL}")
  print(result)
  soup = BeautifulSoup(result.text, "html.parser")
  results = soup.find_all("li",{"class":"feature"})
  for result in results:
    job = extract_job(result)
    jobs.append(job)
  return jobs

def get_jobs(keyword):
  URL= f"https://weworkremotely.com/remote-jobs/search?term={keyword}"
  print(URL)
  jobs = extract_jobs(URL)
  return jobs
