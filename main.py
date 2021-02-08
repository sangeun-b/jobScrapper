from flask import Flask, render_template, request, redirect, send_file
from ro import get_jobs as get_ro_jobs
from so import get_jobs as get_so_jobs
from wwr import get_jobs as get_wwr_jobs
from save import save_to_file

"""
These are the URLs that will give you remote jobs for the word 'python'

https://stackoverflow.com/jobs?r=true&q=python
https://weworkremotely.com/remote-jobs/search?term=python
https://remoteok.io/remote-dev+python-jobs

Good luck!
"""
app = Flask("Last_Challenge")
db = {}
@app.route("/")
def home():
  return render_template("home.html")

@app.route("/report")
def report():
  keyword = request.args.get("keyword")
  if keyword:
    keyword=keyword.lower()
    existedDb = db.get(keyword)
    if existedDb:
      jobs = existedDb
    else:
      jobs = get_ro_jobs(keyword) + get_so_jobs(keyword)+get_wwr_jobs(keyword)
      db[keyword] = jobs
  else:
    return redirect("/")

  return render_template("index.html",keyword = keyword, jobs=jobs,resultsNumber=len(jobs))

@app.route('/export')
def export():
  keyword = request.args.get("keyword")
  if keyword:
    keyword=keyword.lower()
    jobs=db.get(keyword)
  else: 
    return redirect("/")
  if not jobs:
    return redirect("/")
  save_to_file(jobs,keyword)
  
  return send_file(f"{keyword}.csv", as_attachment=True)

app.run(host="127.0.0.1")