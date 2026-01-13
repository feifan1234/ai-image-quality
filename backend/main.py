from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from analyzer.scorer import QualityScorer
from utils.image_loader import load_image_from_bytes
import uvicorn
import sys
import os

# Add backend directory to path so imports work
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

app = FastAPI(
    title="AI Image Quality Assessment System",
    description="API for analyzing image quality (sharpness, brightness, contrast, noise)",
    version="1.0.0"
)

# Enable CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # In production, replace with specific frontend origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

scorer = QualityScorer()

@app.get("/")
def read_root():
    return {"message": "AI Image Quality System API is running"}

@app.post("/analyze")
async def analyze_image(file: UploadFile = File(...)):
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="File must be an image")
    
    try:
        contents = await file.read()
        image = load_image_from_bytes(contents)
        result = scorer.analyze(image)
        return {
            "filename": file.filename,
            "analysis": result
        }
    except Exception as e:
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"Analysis failed: {str(e)}")

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
