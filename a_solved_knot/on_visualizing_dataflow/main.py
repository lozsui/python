from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse
import json
import os

app = FastAPI()

# Serve static files (like script.js)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Template directory (you already had this)
templates = Jinja2Templates(directory="templates")

# Path where the diagram JSON is stored
DIAGRAM_PATH = "diagram.json"


# ---------------------------
# Serve the index page
# ---------------------------
@app.get("/")
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


# ---------------------------
# Load diagram from disk
# ---------------------------
@app.get("/diagram")
def load_diagram():
    if not os.path.exists(DIAGRAM_PATH):
        return JSONResponse(content={})

    try:
        with open(DIAGRAM_PATH, "r") as f:
            data = json.load(f)
            return JSONResponse(content=data)
    except Exception:
        # Return empty if file is corrupted or unreadable
        return JSONResponse(content={})


# ---------------------------
# Save diagram to disk
# ---------------------------
@app.post("/diagram")
async def save_diagram(data: dict):
    try:
        with open(DIAGRAM_PATH, "w") as f:
            json.dump(data, f, indent=4)
        return {"status": "saved"}
    except Exception as e:
        return {"status": "error", "message": str(e)}
