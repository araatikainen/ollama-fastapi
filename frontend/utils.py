import os
import requests
import base64
from io import BytesIO
from PIL import Image

def send_request(path: str, data: dict):
    """Send request to backend API"""
    try:
        response = requests.post(
            os.getenv("BACKEND_URL") + path, 
            json=data
            )
        
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": str(e)}
    

def convert_to_base64(pil_image):
    """
    Convert PIL images to Base64 encoded strings

    :param pil_image: PIL image
    :return: Re-sized Base64 string
    """

    buffered = BytesIO()
    pil_image.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")
    return img_str


def convert_image(image: str):

    # Open the uploaded image using PIL
    image = Image.open(image)
    # Convert the image to a Base64 string
    img_base64 = convert_to_base64(image)
    
    return img_base64
        