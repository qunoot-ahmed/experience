import os
from flask import Flask, render_template, request, jsonify
import openai
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Set OpenAI API key from environment variable
openai.api_key = os.getenv('OPENAI_API_KEY')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/transcribe', methods=['POST'])
def transcribe_audio():
    if 'audio' not in request.files:
        return jsonify({'error': 'No audio file provided'}), 400

    audio_file = request.files['audio']

    if audio_file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    # Secure the filename to avoid issues with special characters
    filename = secure_filename(audio_file.filename)

    # Set the .name attribute of the file object
    audio_file.name = filename

    try:
        # Open the file and pass it to the OpenAI API for transcription
        transcription = openai.Audio.transcribe(
            model="whisper-1",
            file=audio_file
        )

        # Return the transcription as a JSON response
        return jsonify({'transcription': transcription['text']})

    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
