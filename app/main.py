from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import List, Dict, Any
from openai import OpenAI
import os
import json

from fastapi.middleware.cors import CORSMiddleware

# Load environment variables from .env file
from dotenv import load_dotenv
load_dotenv()

app = FastAPI(title="GPT-4 Agent API")

# Configure CORS to allow frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For development; restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Define the data item model
class DataItem(BaseModel):
    step: str
    data: Dict[str, Any]

# Define the request body using Pydantic
class PromptRequest(BaseModel):
    prompt: str
    data: List[DataItem]

# Define the response model
class PromptResponse(BaseModel):
    response: str

@app.post("/generate", response_model=PromptResponse)
async def generate_response(request: PromptRequest):
    try:
        # Log the received request for debugging
        print(f"Received prompt: {request.prompt}")
        print(f"Received data: {json.dumps(request.dict(), indent=2)}")

        # Prepare the data as a string to include in the prompt
        data_strings = []
        for item in request.data:
            step = item.step
            data = item.data
            data_string = f"{step}\n{json.dumps(data, indent=2)}"
            data_strings.append(data_string)
        data_prompt = "\n\n".join(data_strings)

        # Construct the full prompt
        full_prompt = f"{request.prompt}\n\nHere is some relevant data:\n{data_prompt}"

        # Log the full prompt for debugging
        print(f"Full prompt sent to OpenAI:\n{full_prompt}")

        # Call OpenAI's GPT-4 API using the new interface
        completion = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that can analyze network data and provide insights."},
                {"role": "user", "content": full_prompt},
            ],
            max_tokens=500,
            temperature=0.7,
        )

        # Extract the assistant's reply
        assistant_reply = completion.choices[0].message.content.strip()

        # Log the assistant's reply for debugging
        print(f"Assistant's reply:\n{assistant_reply}")

        return PromptResponse(response=assistant_reply)

    except Exception as e:
        # Log the error for debugging
        print(f"Error in generate_response: {str(e)}")
        # Handle errors
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/", response_class=HTMLResponse)
async def read_index():
    try:
        with open("index.html") as f:
            return f.read()
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="index.html not found")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)