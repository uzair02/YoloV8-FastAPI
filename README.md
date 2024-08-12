# YOLO v8 Integration with FastAPI and Frontend

## Overview
This project integrates a custom-trained YOLO v8 model with FastAPI for backend processing and features a basic frontend for user interaction. Users can upload images, which are processed by the YOLO v8 model to identify products. The results are displayed in a user-friendly manner on the frontend.

## Features
Custom-trained YOLO v8 model for object detection.
FastAPI backend to handle image uploads and processing.
Basic frontend developed with React for user interactions.
Display of search results with product names, links, and timestamps.

## Prerequisites
Python (for backend development)
Node.js (for frontend development)
PostgreSQL (for the database)

## Setup
### Backend Setup

1. **Clone the Repository**

   ```bash
   git clone https://github.com/uzair02/YoloV8-FastAPI.git

2. **Navigate to Backend Directory:**
   
   ```windows
      cd backend
   
3. **Create a Virtual Environment:**
   ```bash
   python -m venv env

4. **Activate the Virtual Environment:**
   ```bash
   #windows
   .\env\Scripts\activate

   #linux
   source env/bin/activate

5. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt

6. **Set Up the Database:**
  - Create a .env file in the backend directory with the necessary database credentials.
   
7. **Start the Backend Server:**
   ```bash
   uvicorn main:app --reload

### Frontend Setup

1. **Navigate to Frontend Directory:**
   ```bash
   cd ../frontend

2. **Install Dependencies:**
   
   ```windows
   npm install
   
3. **Start the Frontend Development Server:**
   ```bash
   npm run dev

## Usage
1. Navigate to the Application in Your Browser:
   Open http://localhost:3000 to access the frontend.

2. Upload an Image:
   Use the upload feature to submit an image to be processed by the YOLO v8 model.

3. View Results:
   The frontend will display the identified product names, links, and timestamps of the results.


## YOLO v8 Model Integration
1. Model Path:
   Ensure the YOLO v8 model is correctly located and accessible by the FastAPI backend.
   
3. Custom Training:
  If you need to retrain the model, follow YOLO v8's documentation for custom training.
