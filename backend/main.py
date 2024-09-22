from fastapi import FastAPI, File, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from tempfile import NamedTemporaryFile
from pydantic import BaseModel
import os

app = FastAPI()

origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class FileBody(BaseModel):
    # pylint: disable=missing-docstring
    name: UploadFile

@app.post("/upload")
def detect_faces(cow: str = Form(...), video: UploadFile = File(...)):
    temp = NamedTemporaryFile(delete=False)
    try:
        try:
            contents = video.file.read()
            with temp as f:
                f.write(contents);
        except Exception:
            return {"message": "There was an error uploading the file"}
        finally:
            video.file.close()
        
        res = temp.name  # Pass temp.name to VideoCapture()
    except Exception:
        return {"message": "There was an error processing the file"}
    finally:
        #temp.close()  # the `with` statement above takes care of closing the file
        os.remove(temp.name)
        
    return {"message":[res]}
   
