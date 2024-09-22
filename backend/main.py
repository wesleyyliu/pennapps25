from fastapi import FastAPI, File, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from tempfile import NamedTemporaryFile
from pydantic import BaseModel
import pests, os, json, pest_inference
import shutil

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
    try:
        with open(video.filename, 'wb') as f:
            shutil.copyfileobj(video.file, f)
            tmp_path = f.name
            print(tmp_path)
            wesley_res = pest_inference.run_everything(tmp_path)
            print(dict(wesley_res))
            david_res = pests.compileBugs(dict(wesley_res))
            print(david_res)
    except Exception:
        return {"message": "There was an error uploading the file"}
    finally:
        video.file.close()
    # temp = NamedTemporaryFile(delete=False)
    # try:
    #     # try:
    #     #     contents = video.file.read()
    #     #     with temp as f:
    #     #         f.write(contents);
    #     # except Exception:
    #     #     return {"message": "There was an error uploading the file"}
    #     # finally:
    #     #     video.file.close()
        
    #     # res = temp.name  # Pass temp.name to VideoCapture()
    #     wesley_res = pest_inference.run_everything(cow)
    #     print(dict(wesley_res))
    #     david_res = pests.compileBugs(dict(wesley_res))
    #     print(david_res)
        
    # except Exception as e:
    #     return {"message": "There was an error processing the file" + str(e)}
    # finally:
    #   # the `with` statement above takes care of closing the file
    #     os.remove(temp.name)

    return(david_res)
        
    # return {"insects": [{"bug": "Bee", "timestamp": ["0:00-0:01"], "description": "hire a beekeeper to relocate the bee nest; spray insecticide or soapy water at beehive during night from a safe distance. Note: bees are considered pests when they set up a nest near you or your plants"}, {"bug": "Caterpillar", "timestamp": ["0:01-0:02", "0:32-0:32-0:32", "0:36-0:39-0:39"], "description": "remove caterpillars and eggs where discovered and put them in soapy water; spray at them directly with soapy water, vinegar mixture, or insecticide"}, {"bug": "Aphid", "timestamp": ["0:02-0:02", "0:21-0:31-0:31", "0:34-0:36-0:36"], "description": "spray water, neem oil, or water-soap solution forcefully; use insecticide if severe"}, {"bug": "Earwig", "timestamp": ["0:03-0:03"], "description": "use fish or vegetable oil to attract earwigs into traps; mix rubbing alcohol with water and spray"}, {"bug": "Grasshopper", "timestamp": ["0:03-0:05", "0:07-0:07"], "description": "collaborate with others to control population when they\u2019re small nymphs; apply insecticide to green plants that they are attracted to"}, {"bug": "Ant", "timestamp": ["0:05-0:07", "0:19-0:21-0:21", "0:39-0:41-0:41"], "description": "spray vinegar on soil; mix borax, sugar, and water and place near plant;use diatomaceous earth (keep soil dry); pour boiling water"}, {"bug": "Slug", "timestamp": ["0:09-0:11"], "description": "use traps that contain bear or a water and yeast mixture that attract slugs and cause them to fall; create drier conditions in garden"}, {"bug": "Wasp", "timestamp": ["0:12-0:12-0:12"], "description": "spray at late evening or early morning with a mixture soap and water or just with pesticide"}, {"bug": "Beetle", "timestamp": ["0:13-0:16-0:16", "0:17-0:19-0:19"], "description": "sprinkle Diatomaceous earth (keep soil dry); spray or pour soapy water, vinegar water, or boiling water"}]}
   
@app.get("/pests")
def get_bugs():
    analysis = pest_inference.run_with_video_inference
    (os.getenv("ROBOFLOW_API_KEY"), 'testvideo2.mp4', "pestnet-i2j4d", 0.8, 2, 2)
    jsonData = json.dumps(pests.compileBugs({"caterpillar": [(13.12, 15.17), (23.47, 79.5)]}))
    print(jsonData)
    with open('data.json', 'w') as json_file:
        json.dump(pests.compileBugs({"caterpillar": [(13.12, 15.17), (23.47, 79.5)], "beetle": [(12.1, 13)]}), json_file)

get_bugs()