from fastapi import FastAPI

# Creates an object of the FastAPI class
app = FastAPI()

@app.get("/")
def root():
    return {"message": "AI Job Application Manager API"}


@app.get("/health")
def health():
    return {"status": "API is healthy"}
