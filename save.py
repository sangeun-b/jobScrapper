import csv 

def save_to_file(jobs,keyword):
  file = open(f"{keyword}.csv", mode="w")
  writer = csv.writer(file)
  writer.writerow(["title","company","loaction","link"])
  for job in jobs:
    writer.writerow(list(job.values()))
  return