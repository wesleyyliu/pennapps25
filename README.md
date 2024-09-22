# pennapps25

## Project Idea: PestNet

We are developing an agricultural pest detector. Gardeners can monitor their plants with a camera, and our model will take in an image/video and identify which pests have been causing problems to the plant. This will help farmers monitort their plant health and give the proper treatment/sprays to protect their plants.

TLDR: Used for garden plants, finding out which pests have been eating your produce

- Train model on bugs (using this [Kaggle Dataset](https://www.kaggle.com/datasets/vencerlanz09/agricultural-pests-image-dataset/data?select=earwig))
- Use object detection to find the bug on the image
- Classify the bug on the image
- Return results 
  - When did the bug appear in the image (time stamp)?
  - What bug appeared?
  - How do you prevent the bug, or what are ways to deal with it?

## Frontend
First, download node.
Then, while in the frontend folder:  
```npm i``` <-- Only need to do this the first time  
```npm run dev``` <-- Do this every time you want start up the frontend

## Backend
First, install poetry and python (greater than 3.12).  
Then, while in backend folder:  
```poetry shell```  
```poetry install```  
```fastapi dev main.py```