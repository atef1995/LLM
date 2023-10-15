import os
import asyncio

if os.name == "nt":  # Check if the operating system is Windows
    asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())

import pytesseract
from playwright.async_api import async_playwright
from pdf2image import convert_from_path


if asyncio.get_event_loop().is_closed():
    loop = asyncio.ProactorEventLoop()
    asyncio.set_event_loop(loop)


def from_pdf(pdf_data):
    # Convert PDF to list of images
    images = convert_from_path(pdf_path)

    # Initialize text variable
    text = ""

    # Iterate through images and perform OCR
    for i, image in enumerate(images):
        text += pytesseract.image_to_string(image)

    return text


async def from_url(url):
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto(url)

        # For a more targeted scraping, you would identify the specific elements you want
        # For instance, to get all text inside <p> tags:
        # text_elements = page.query_selector_all("p")
        # text = " ".join([elem.inner_text() for elem in text_elements])

        # For a generic scrape, you could just grab the entire page content:
        text = await page.content()

        await browser.close()
    return text
