from fastapi import APIRouter, UploadFile, File
import os, shutil

router = APIRouter(prefix="/upload", tags=["Uploads"])

@router.post("/")
def upload_file(file: UploadFile = File(...)):
    upload_dir = "static/uploads/"
    os.makedirs(upload_dir, exist_ok=True)
    file_path = os.path.join(upload_dir, file.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"filename": file.filename, "path": file_path}
