from fastapi import FastAPI, HTTPException, Request
import extract  # This is your custom extraction module
from pydantic import BaseModel


class ExtractData(BaseModel):
    url: str = None
    data: str = None


app = FastAPI()


@app.post("/extract/")
async def extract_data(payload: ExtractData):
    url = payload.url
    pdf_data = payload.data

    if url:
        # Use playwright to extract data from a website
        text = await extract.from_url(url)
        return {"text": text}

    elif pdf_data:
        # Use pytesseract to extract data from a PDF
        text = await extract.from_pdf(pdf_data)
        return {"text": text}

    else:
        raise HTTPException(
            status_code=400, detail="Either data or url should be supplied."
        )
