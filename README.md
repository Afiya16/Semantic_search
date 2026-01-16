Search API using FastAPI
#-------------------------#
#-------------------------#

#----------------------------------------#
->Project Overview and selected Task
#----------------------------------------#

This projects implements a Search API using FastAPI as part of the given assignment requirements.
The selected task focuses on builing a backend API that accepts a user query,processes it, and returns relevant search results.

#-----------------------------------------#
->Architecture Summary
#-----------------------------------------#

This applications follows a simple and clean architecture.
Client (Postman / cURL / Browser)
↓
FastAPI Application
↓
Search Logic (Query processing)
↓
JSON Response

->FastAPI handles HTTP requests and responses

->Search logic processes user queries

->Results are returned in JSON format

#---------------------------------------#
->Setup Instructions
#---------------------------------------#

Python Version
Python 3.9 or above is required

Environment Creation
Create a virtual environment:
python -m venv venv

Activate the environment:
venv\Scripts\activate

Dependency Installation
Install all required dependencies:
pip install -r requirements.txt

How to Run the API
Start the FastAPI server using Uvicorn:
uvicorn main:app --reload
The API will be available at:http://127.0.0.1:8000 
Swagger UI (API documentation):http://127.0.0.1:8000/docs 

How to Test Endpoints (cURL / Postman)
Eg-> Endpoint
GET /search?query=example
Using Browser or Postman
http://127.0.0.1:8000/search?query=laptop 
Sample JSON Response
Response body
{
  "original_query": "cheap laptop",
  "refined_query": "cheap laptop affordable budget notebook computer",
  "results": [
    {
      "price": 45000,
      "description": "Affordable laptop for daily use",
      "id": 1,
      "name": "HP Pavilion",
      "category": "Laptop"
    }
  ]
}

#-----------------------------------------------#
->Streamlit UI Setup
#-----------------------------------------------#
Streamlit UI is not implemented in this project.
The API can be tested directly using Swagger UI, Postman, or cURL.

#----------------------------------------------#
->Environment Variable Explanation
#----------------------------------------------#
This project does not require any mandatory environment variables.(Optional variables can be added later if needed, such as API keys or database URLs.)

#----------------------------------------------#
->Notes and Assumptions
#----------------------------------------------#
Mini-agent and test-agent files are excluded intentionally
Search logic is kept simple for clarity
No external database is used
Data is handled in-memory
Dockerization is optional and not included


#--------------------------------------------#
Submitted By
#--------------------------------------------#
Afiya Khatoon
Btech-CSE
(Python,AI/ML Enthusiast)