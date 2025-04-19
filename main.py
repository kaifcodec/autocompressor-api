from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
import shutil
import os

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to AutoCompressor API"}

@app.post("/compress/image")
async def compress_image(file: UploadFile = File(...)):
    from PIL import Image

    # Save uploaded image temporarily
    input_path = f"temp_{file.filename}"
    with open(input_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Compress image
    compressed_path = f"compressed_{file.filename}"
    image = Image.open(input_path)
    image.save(compressed_path, optimize=True, quality=50)

    # Clean up original
    os.remove(input_path)

    return FileResponse(compressed_path, media_type="image/jpeg", filename=compressed_path)
