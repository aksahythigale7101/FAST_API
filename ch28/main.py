from fastapi import FastAPI, Form, File, UploadFile, HTTPException
import os
from pathlib import Path
from typing import Annotated, List

from pydantic import BaseModel
app = FastAPI()



#using From Feilds With Upload File-----------------------
# @app.post("/profile")
# async def upload_profile(
#     username: str = Form(),
#     photo: UploadFile = File()
# ):
#     return {
#         "username": username,
#         "filename": photo.filename
#     }

#using From Feilds With Upload File------------------
# @app.post("/profile")
# async def upload_profile(
#     username: str = Form(),
#     email: str = Form(),
#     photo: UploadFile = File()
# ):
#     return {
#         "username": username,
#         "email": email,
#         "filename": photo.filename,
#         "content_type": photo.content_type
#     }


#File Size Validations-----------------------
# @app.post("/upload")
# async def upload_file(
#     file: UploadFile = File()
# ):

#     content = await file.read()

#     max_size = 5 * 1024 * 1024  # 5 MB

#     if len(content) > max_size:
#         raise HTTPException(
#             status_code=400,
#             detail="File size must be less than 5 MB"
#         )

#     return {
#         "filename": file.filename,
#         "size": len(content)
#     }


#File upload and Save----------------------------

UPLOAD_DIR = Path("upload")
UPLOAD_DIR.mkdir(exist_ok=True)

# @app.post("/upload")
# async def upload_file(file: UploadFile = File()):
#     # Sanitize: keep only the filename part, strip any path info
#     safe_filename = os.path.basename(file.filename)
#     file_path = UPLOAD_DIR / safe_filename

#     with open(file_path, "wb") as f:
#         f.write(await file.read())

#     return {
#         "message": "File uploaded successfully",
#         "filename": safe_filename
#     }


#using multiple file upload  and some error while multiple file uploading
# @app.post("/test-upload")
# async def upload_files(files: List[UploadFile] = File(...)):
#     saved_files = []

#     for file in files:
#         safe_filename = os.path.basename(file.filename)
#         file_path = UPLOAD_DIR / safe_filename

#         with open(file_path, "wb") as f:
#             f.write(await file.read())

#         saved_files.append(safe_filename)

#     return {
#         "message": f"{len(saved_files)} file(s) uploaded successfully",
#         "filenames": saved_files
#     }


# Byte Read---------------------------
# @app.post("/upload")
# async def upload(
#     file: bytes = File()
# ):
#     return {
#         "size": len(file)
#     }


#Validation with Form + File----------------
# @app.post("/profile")
# async def profile(
#     username: Annotated[str, Form(min_length=3)],
#     photo: UploadFile = File()
# ):
#     return {
#         "username": username,
#         "filename": photo.filename
#     }




#Pydantic model + multipart
class UserForm(BaseModel):
    name: str
    age: int
    email: str


@app.post("/user")
async def create_user(
    name: Annotated[str, Form()],
    age: Annotated[int, Form()],
    email: Annotated[str, Form()],
    photo: UploadFile = File()
):
    user = UserForm(name=name, age=age, email=email)
    return {
        "name": user.name,
        "age": user.age,
        "email": user.email,
        "photo": photo.filename
    }