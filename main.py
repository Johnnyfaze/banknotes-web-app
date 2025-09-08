# library imports
import pickle
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
import numpy as np
import uvicorn

app = FastAPI()

# If your index.html is inside the 'templates' folder, update your root endpoint:
@app.get("/", response_class=HTMLResponse)
async def root():
    return FileResponse("templates/index.html")

# Load the trained model
with open('heart_disease_model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.post("/predict")
async def predict(request: Request):
    data = await request.json()
    features = np.array(data["data"]).reshape(1, -1)
    prediction = model.predict(features)
    return {"prediction": prediction.tolist()}

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)



