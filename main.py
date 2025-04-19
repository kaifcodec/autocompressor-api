from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
import shutil
import os
from PIL import Image
from pydub import AudioSegment

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to AutoCompressor API"}

@app.post("/compress/image")
async def compress_image(file: UploadFile = File(...)):
    input_path = f"temp_{file.filename}"
    with open(input_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    compressed_path = f"compressed_{file.filename}"
    image = Image.open(input_path)
    image.save(compressed_path, optimize=True, quality=50)
    os.remove(input_path)

    return FileResponse(compressed_path, media_type="image/jpeg", filename=compressed_path)

@app.post("/compress/audio")
async def compress_audio(file: UploadFile = File(...), bitrate: int = 128):
    input_path = f"temp_{file.filename}"
    with open(input_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    output_path = f"compressed_{file.filename}"
    audio = AudioSegment.from_file(input_path)
    audio.export(output_path, bitrate=f"{bitrate}k", format="mp3")
    os.remove(input_path)

    return FileResponse(output_path, media_type="audio/mpeg", filename=output_path)
