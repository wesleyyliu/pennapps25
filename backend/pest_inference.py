from inference_sdk import InferenceHTTPClient
import cv2
import time
from collections import defaultdict
from roboflow import Roboflow
# from dotenv import load_dotenv
import os

def process_results(entry, confidence=.7):
    best_prediction = entry['predictions'][0]
    best_prediction_class = best_prediction['class']
    # correct spelling
    if best_prediction_class == 'catterpillar':
        best_prediction_class = 'caterpillar'
    best_prediction_confidence = best_prediction['confidence']
    return best_prediction_class if best_prediction_confidence > confidence else None
    
def run_with_video_inference(video_file, project_id, model_num, confidence_threshold, fps, api_key):
    run_time = time.time()
    print("hey1")

    rf = Roboflow(api_key=api_key)
    print("hey")
    project = rf.workspace().project(project_id)
    model = project.version(model_num).model
    print(video_file)
    job_id, signed_url, expire_time = model.predict_video(
    video_file,
    fps=fps,
    prediction_type="batch-video",
    )
    print("hey3")

    results = model.poll_until_video_results(job_id)
    results_predictions = results[project_id]
    results_arr = [process_results(res, confidence_threshold) for res in results_predictions]

    pest_detections = defaultdict(list)
    current_pest = None
    start_time = None

    time_offset = results['time_offset']

    for index, pred in enumerate(results_arr):
        timestamp = time_offset[index]
        if pred != None:
            if current_pest is None:
                # New pest detected
                current_pest = pred
                start_time = timestamp
            elif pred != current_pest:
                # Different pest detected
                pest_detections[current_pest].append((start_time, timestamp))
                # pest_detections.append((current_pest, start_time, timestamp))
                current_pest = pred
                start_time = timestamp
        else:
            if current_pest is not None:
                # Pest no longer detected
                pest_detections[current_pest].append((start_time, timestamp))
                # pest_detections.append((current_pest, start_time, timestamp))
                current_pest = None
                start_time = None
    print(f"Time taken: {time.time() - run_time}")
    return pest_detections

def run_with_frame_inference(video_file, project_id, model_num, confidence_threshold, fps, api_key):
    model_id = project_id + '/' + str(model_num)

    CLIENT = InferenceHTTPClient(
        api_url="https://detect.roboflow.com",
        api_key=api_key
    )
    
    cap = cv2.VideoCapture(video_file)
    fps_of_vid = cap.get(cv2.CAP_PROP_FPS)
    frame_interval = fps_of_vid // fps

    frame_id = 0
    start = time.time()
    pest_detections = defaultdict(list)
    current_pest = None
    start_time = None

    while cap.isOpened():
        ret, frame = cap.read()
        
        if not ret:
            break
        
        if frame_id % frame_interval == 0:
            prediction = CLIENT.infer(frame, model_id=model_id)
            best_class = prediction['top']
            best_confidence = prediction['confidence']
            
            timestamp = cap.get(cv2.CAP_PROP_POS_MSEC) / 1000  # Convert to seconds
            
            if best_confidence > confidence_threshold:
                if current_pest is None:
                    # New pest detected
                    current_pest = best_class
                    start_time = timestamp
                elif best_class != current_pest:
                    # Different pest detected
                    pest_detections[current_pest].append((start_time, timestamp))
                    # pest_detections.append((current_pest, start_time, timestamp))
                    current_pest = best_class
                    start_time = timestamp
            else:
                if current_pest is not None:
                    # Pest no longer detected
                    pest_detections[current_pest].append((start_time, timestamp))
                    # pest_detections.append((current_pest, start_time, timestamp))
                    current_pest = None
                    start_time = None
        
        frame_id += 1

    # Handle case where video ends while a pest is still being detected
    if current_pest is not None:
        pest_detections[current_pest].append((start_time, cap.get(cv2.CAP_PROP_POS_MSEC) / 1000))
        # pest_detections.append((current_pest, start_time, cap.get(cv2.CAP_PROP_POS_MSEC) / 1000))

    cap.release()

    print(f"Total time elapsed: {time.time() - start}")

    return pest_detections

# if __name__ == '__main__':
def run_everything(filepath):
    # load env for roboflow api
    # load_dotenv()
    # api_key = os.environ["ROBOFLOW_API_KEY"]
    api_key="Jar5MhgJ8robnyIGUmrW"
    print(api_key)
    # video_file = 'testvideo2.mp4'
    video_file = filepath
    print(filepath)
    # video_file = './demo.mp4'
    project_id = "pestnet-i2j4d"
    confidence_threshold = 0.8
    model_num = 2
    fps = 2
    print("asdfasdf")

    return(run_with_video_inference(video_file, project_id, model_num, confidence_threshold, fps, api_key))

    

    

    

