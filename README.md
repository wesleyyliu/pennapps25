# pennapps25

## Project Idea: PestNet

We are developing an agricultural pest detector. Gardeners and farmers can monitor their plants with a camera, and our model will take in a video and identify which pests have been causing problems to the plant. This will help gardeners and farmers monitor their plant health and respond appropriately to protect their plants.

TLDR: Used for garden plants, finding out which pests have been eating your produce

- Trained model on bugs (using the [Agricultural Pests Image Dataset on Kaggle](https://www.kaggle.com/datasets/vencerlanz09/agricultural-pests-image-dataset/data) and the [Pest Dataset on Kaggle](https://www.kaggle.com/datasets/simranvolunesia/pest-dataset/data)
- Classified the bug in the image
- Returned results to the user through the webapp
  - When did the bug appear in the image (time stamp)?
  - What bug appeared?
  - How do you prevent the bug, or what are ways to deal with it?

## Frontend
First, download node.
Then, while in the frontend folder:  
```npm i``` <-- Only need to do this the first time  
```npm run dev``` <-- Do this every time you want start up the frontend

Technologies used:
- Javascript/Typescript
- React
- Tailwind
- Vite
- Toastify
- Figma
- Poetry
- node.js

## Backend
First, install poetry and python (greater than 3.12).  
Then, while in backend folder:  
```poetry shell```  
```poetry install```  
```fastapi dev main.py```

Technologies used:
- FastAPI
- Python
- OpenCV
- Roboflow

## Team Info
David Fu: davidcfu@sas.upenn.edu
Alice Liu: aliu17@seas.upenn.edu
Wesley Liu: wesliu@seas.upenn.edu
Maxwell Ye: maxwelly@seas.upenn.edu
