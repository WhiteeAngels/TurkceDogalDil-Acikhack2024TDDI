from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from data_processing import DataProcessing

app = FastAPI()
data_processor = DataProcessing()

class TextInput(BaseModel):
    text: str

@app.get("/")
def read_root():
    return {"message": "Welcome to the Text Analysis API"}

@app.post("/predict/", response_model=dict)
async def analyze(text_input: TextInput):
    text = text_input.text

    if not text:
        raise HTTPException(status_code=400, detail="Metin gerekli")

    try:
        analysis_result = data_processor.process_text(text)
        return analysis_result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8027)