from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, FileResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")




class Website():
  name: str
  url: str

  def __init__(self, name, url):
    self.name = name
    self.url = url


def ReadDataFromFile(file, array):
  file = open(file, "rt")
  lines = file.readlines()
  for i in range(0, len(lines), 3):
    website = Website(lines[i].strip("\n"), lines[i + 1].strip("\n"))
    array.append(website)
  file.close()

def ReadData():
  for i in range(0, 6):
    if(i == 0):
      ReadDataFromFile("data/frontend.txt", frontend)
    if(i == 1):
      ReadDataFromFile("data/documentation.txt", documentation)
    if(i == 2):
      ReadDataFromFile("data/backend.txt", backend)
    if(i == 3):
      ReadDataFromFile("data/job.txt", job)
    if(i == 4):
      ReadDataFromFile("data/useful.txt", useful)
    if(i == 5):
      ReadDataFromFile("data/social.txt", social)


frontend = []
documentation = []
backend = []
job = []
useful = []
social = []

ReadData()


@app.get("/", response_class=HTMLResponse, status_code=200)
async def index(request: Request):
  return templates.TemplateResponse(
    "index.html",
      {"request": request,
      "frontend": frontend,
      "documentation": documentation,
      "backend": backend,
      "job": job,
      "useful": useful,
      "social": social}
  )

@app.get('/{file}', response_class=FileResponse, status_code=200)
async def serve_static(file: str):
  if file == "robots.txt" or file == "humans.txt":
    path = "static/global/" + file
    return FileResponse(path=path)
  else:
    return RedirectResponse("https://windwalks-interface.herokuapp.com/")

""" Not working... every bad request will redirect user to index page.
@app.get("/404", response_class=HTMLResponse, status_code=404)
async def raise_404(request: Request):
  return templates.TemplateResponse('404.html', {"request": request})
"""




if __name__ == '__main__':
  uvicorn.run('app:app')
