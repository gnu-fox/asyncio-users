import httpx
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount('/static', StaticFiles(directory="src/static"), name='static')
templates = Jinja2Templates(directory="src/templates")

@app.get('/sign-in', response_class=HTMLResponse)
async def login(request: Request):
    return templates.TemplateResponse("login.html", {'request': request})

@app.get('/sign-up', response_class=HTMLResponse)
async def register(request: Request):
    return templates.TemplateResponse("register.html", {'request': request})

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=4000)