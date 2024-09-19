import os

import openai
from openai import OpenAI
client = OpenAI()

# Access environment variable for the API key
openai.api_key = os.getenv('OPENAI_API_KEY')
print(openai.api_key)

response = client.images.generate(
  model="dall-e-3",
  prompt="a white siamese cat",
  size="1024x1024",
  quality="standard",
  n=1,
)

image_url = response.data[0].url
print(image_url)