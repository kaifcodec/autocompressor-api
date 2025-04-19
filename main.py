from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
import os
import uvicorn

app = FastAPI()

@app.get("/")
def root():
    return {"status": "Kaif's compressor is awake!"}

@app.post("/compress/image")
async def compress_image(file: UploadFile = File(...)):
    return JSONResponse(content={"filename": file.filename, "message": "File received!"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port)
