# Selfie Match

Selfie Match is a FastAPI application designed to match a selfie of a person to the photo on an ID document (e.g., passport, driving license) and verify if they match. This application leverages the DeepFace library for face verification.

## Features

- Accepts base64 encoded images of a selfie and an ID document.
- Decodes the images and performs face verification.
- Supports CORS for all origins.

## Prerequisites

- Python 3.6+
- Virtual environment (recommended)

## Installation

1. Clone the Repository

First, clone the repository to your local machine:

git clone https://github.com/HemantKundernbl/true_face-backend.git
cd true_face-backend

2. Create a Virtual Environment

Create a virtual environment to manage dependencies:
python3 -m venv env
source env/bin/activate

3. Install Dependencies

pip install fastapi uvicorn deepface opencv-python-headless numpy

## Running the Application
1. Activate the Virtual Environment
If the virtual environment is not already activated, activate it:
source env/bin/activate

2. Run the FastAPI Application
uvicorn main:app --host 0.0.0.0 --port 8000

The application will be available at http://localhost:8000.

## API Endpoints
/verify (POST)
This endpoint accepts a JSON payload containing base64 encoded images of a selfie and an ID document photo. It verifies if the two images match.

Request
URL: /verify
Method: POST
Headers: Content-Type: application/json
Body:
{
  "selfie": "<base64-encoded-selfie-image>",
  "frame": "<base64-encoded-id-image>"
}

Replace <base64-encoded-selfie-image> and <base64-encoded-id-image> with actual base64 encoded strings of the images.

Response
Success Response:

Code: 200
Content:
{
  "verified": true,
  "distance": 0.1234,
  "threshold": 0.4,
  "model": "VGG-Face"
}

Error Response:

Code: 400
Content:
{
  "detail": "Error message"
}

## Example Request

You can test the endpoint using curl:
curl -X POST "http://localhost:8000/verify" -H "Content-Type: application/json" -d '{
  "selfie": "<base64-encoded-selfie-image>",
  "frame": "<base64-encoded-id-image>"
}'

