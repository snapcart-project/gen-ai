import tempfile, subprocess
from werkzeug.utils import secure_filename
import os
from flask import Flask, request, jsonify
from google.cloud import speech
import vertexai
from vertexai.generative_models import GenerativeModel, Part

# Initialize Flask application
app = Flask(__name__)

# This is important for a hackathon: it allows the frontend website to connect to your backend
from flask_cors import CORS
CORS(app)

# Initialize Google Cloud clients
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"C:\\Users\\priya\\Downloads\\snapchart-472412-bd5ccc3c9430.json"  
# Update with your service account file path
# The GOOGLE_APPLICATION_CREDENTIALS environment variable handles authentication for you
speech_client = speech.SpeechClient()
vertexai.init(project="snapchart-472412", location="us-central1")# Initialize Vertex AI
model = GenerativeModel("gemini-1.5-pro")


# The main API endpoint for your voice-to-story feature
@app.route('/api/process-voice', methods=['POST'])
def process_voice():
    # Check if an audio file was uploaded in the request
    if 'audio' not in request.files:
        return jsonify({"error": "No audio file provided"}), 400

    audio_file = request.files['audio']
    language_code = request.form.get('language_code', 'en-IN') # Default to Indian English if not specified

    # Step 1: Transcribe the audio using Speech-to-Text API
    try:
        # Save uploaded file to a temporary location
        tmp_in = tempfile.NamedTemporaryFile(delete=False, suffix=".mp4")
        audio_file.save(tmp_in.name)
        # Prepare a path for converted file
        tmp_out = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
        # >>> CHANGE ONLY THIS LINE: put the path where your ffmpeg.exe is located <<<
        ffmpeg_path = r"C:\Users\priya\Downloads\ffmpeg-8.0-essentials_build\ffmpeg-8.0-essentials_build\bin\ffmpeg.exe"
        # Convert input to 16kHz mono PCM WAV
        subprocess.run([
            ffmpeg_path, "-y", "-i", tmp_in.name,
            "-ar", "16000", "-ac", "1", "-acodec", "pcm_s16le",
            tmp_out.name
        ], check=True)
        # Read converted WAV into memory
        with open(tmp_out.name, "rb") as f:
            audio_bytes = f.read()

        # Build Google Speech request with converted audio
        audio_content = speech.RecognitionAudio(content=audio_bytes)
        config = speech.RecognitionConfig(
            encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=16000,
            language_code=language_code
        )
        response = speech_client.recognize(config=config, audio=audio_content)
        
        if not response.results:
            return jsonify({"error": "Could not transcribe audio"}), 400
        
        transcribed_text = response.results[0].alternatives[0].transcript
        
    except Exception as e:
        return jsonify({"error": f"Speech-to-Text error: {str(e)}"}), 500

    # Step 2: Use the Gemini model to generate a polished story
    try:
        model = GenerativeModel("gemini-1.5-pro")
        prompt = f"""
        You are an expert copywriter for a marketplace for local artisans. Take the raw, unpolished voice notes below and write a beautiful product story, catchy social media captions, and relevant hashtags.

        Raw Notes: {transcribed_text}

        Response format:
        ### Product Story
        [Write a 1-2 paragraph, authentic product story.]
        
        ### Marketing Captions
        [Provide 3 short, engaging captions.]
        
        ### Hashtags
        [List 5-8 relevant hashtags.]
        """
        gemini_response = model.generate_content(prompt)
        
        # Extract the structured text from the Gemini response
        polished_content = gemini_response.text
        
    except Exception as e:
        return jsonify({"error": f"Vertex AI error: {str(e)}"}), 500

    # Step 3: Return the final, polished content to the frontend
    return jsonify({
        "status": "success",
        "transcribed_text": transcribed_text,
        "polished_content": polished_content
    })

# Run the Flask app
if __name__ == '__main__':
    # You will need to set the GOOGLE_CLOUD_PROJECT environment variable as well
    # export GOOGLE_CLOUD_PROJECT="snapchart-472412" (or your project ID)
    app.run(debug=True, port=5000)
