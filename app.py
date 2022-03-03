# IMPORTS
from flask import Flask, render_template, request, json, send_from_directory
import gunicorn

# CONFIG
app = Flask(__name__, static_url_path="", static_folder="static/", template_folder="templates/")




# APP
db_load = open('data.json')
db_prep = json.load(db_load)
db_load.close()

frontend_array = db_prep["frontend"]
backend_array = db_prep["backend"]
documentation_array = db_prep["documentation"]
job_array = db_prep["job"]
useful_array = db_prep["useful"]
social_array = db_prep["social"]

# MAIN ROUTE
@app.route("/")
def index():
  return render_template("index.html", 
  frontend_array=frontend_array, 
  backend_array=backend_array, 
  documentation_array=documentation_array, 
  job_array=job_array,
  useful_array=useful_array,
  social_array=social_array), 200


# ADITIONAL ROUTES
# 404
@app.errorhandler(404)
def page_not_found(error):
  return render_template('404.html'), 404

# robots.txt & humans.txt
@app.route('/robots.txt')
@app.route('/humans.txt')
def static_from_root():
  return send_from_directory("static/global/", request.path[1:])




# INIT
if __name__ == "__main__": app.run()
