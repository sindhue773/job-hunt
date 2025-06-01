from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from main import run

class Item(BaseModel):
    job_title: str
    location: str
    experience_level: str
    industry: str
    skills: str
    
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Job Hunter API!"}

@app.post("/job-hunt/")
def create_item(item: Item):
    try:
        from job_search.crew import JobHunter
        inputs = item.model_dump()
        result = JobHunter().crew().kickoff(inputs=inputs)
        return {
            "message": "Job hunt completed successfully!",
            "result": result
        }
    except Exception as e:
        return {"error": str(e)}
    
@app.get("/health")
def health_check():
    return {"status": "ok"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app",  port=8000, reload=True)

