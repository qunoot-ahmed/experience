from flask import Flask, render_template, jsonify
import os
import openai
from openai import OpenAI
client = OpenAI()

# Initialize the Flask application
app = Flask(__name__)

# Access environment variable for the API key
openai.api_key = os.getenv('OPENAI_API_KEY')
print(openai.api_key)

# Define a route and its corresponding request handler
@app.route('/')
def index():
    return render_template(
        'index.html',)

@app.route('/generateimages/<prompt>')
def generate(prompt):
    try:
        print("prompt:", prompt)
        response = client.images.generate(
            model="dall-e-3",
            prompt=prompt,
            size="1024x1024",
            quality="standard",
            n=1
        )
        print(response)
        # Extract image URLs from the response
        image_urls = [img.url for img in response.data]
        return jsonify({"image_urls": image_urls})
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": str(e)}), 500


# Run the Flask app
if __name__ == '__main__':
    app.run(debug=False)
