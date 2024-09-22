from fastapi import FastAPI, File, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from tempfile import NamedTemporaryFile
from pydantic import BaseModel
import pests, os, json, pest_inference

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
    # temp = NamedTemporaryFile(delete=False)
    # try:
    #     try:
    #         contents = video.file.read()
    #         with open(temp.filename, "wb") as f:
    #             f.write(contents);
    #     except Exception:
    #         return {"message": "There was an error uploading the file"}
    #     finally:
    #         video.file.close()
        
    #     # res = process_video(temp.name)  # Pass temp.name to VideoCapture()
    # except Exception:
    #     return {"message": "There was an error processing the file"}
    # finally:
    #     #temp.close()  # the `with` statement above takes care of closing the file
    #     os.remove(temp.name)
        
    return {"message":"sup"}
   
@app.get("/pests")
def get_bugs():
    analysis = pest_inference.run_with_video_inference
    (os.getenv("ROBOFLOW_API_KEY"), 'testvideo2.mp4', "pestnet-i2j4d", 0.8, 2, 2)
    jsonData = json.dumps(pests.compileBugs({"caterpillar": [(13.12, 15.17), (23.47, 79.5)]}))
    print(jsonData)
    with open('data.json', 'w') as json_file:
        json.dump(pests.compileBugs({"caterpillar": [(13.12, 15.17), (23.47, 79.5)], "beetle": [(12.1, 13)]}), json_file)

get_bugs()