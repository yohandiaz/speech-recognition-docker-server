from flask import Flask, request, render_template
import sys
sys.path.append('../speech-recognition')


from audioToText import audioToText

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/audio_to_text', methods=['POST'])
def audio_to_text():
    # Get the uploaded file from the HTML form
    audio_file = request.files['audio_file']

    # Save the uploaded file to the server
    audio_file_path = audio_file.filename
    audio_file.save(audio_file_path)

    # Transcribe the audio to text
    audioToText(audio_file_path)

    return render_template('result.html')

if __name__ == '__main__':
    app.run(debug=True)
