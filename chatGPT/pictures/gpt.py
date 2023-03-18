import os
import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")



# response = openai.Image.create(
#   prompt="a white siamese cat",
#   n=1,
#   size="1024x1024"
# )
# image_url = response['data'][0]['url']


def GPT_function(name):
    try:
        response = openai.Image.create(
        prompt=f"{name}",
        n=1,
        size="1024x1024"
        )
        image_url = response['data'][0]['url']
        return image_url
    except:
        return 'http://unavailable'
