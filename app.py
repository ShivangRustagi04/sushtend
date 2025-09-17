from flask import Flask, render_template, request, jsonify
import groq
import csv
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

client = groq.Client(api_key=os.getenv('GROQ_API_KEY'))

def analyze_transcript(transcript):
    try:
        prompt = f"""
        Analyze the following customer service call transcript and provide:
        1. A concise summary (2-3 sentences)
        2. Customer sentiment (positive, neutral, or negative)
        
        Transcript: {transcript}
        
        Please respond in the following format:
        SUMMARY: [summary here]
        SENTIMENT: [sentiment here]
        """
        completion = client.chat.completions.create(
            model="moonshotai/kimi-k2-instruct",
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant that analyzes customer service call transcripts. Provide clear summaries and accurate sentiment analysis."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.3,
            max_tokens=500
        )
        response = completion.choices[0].message.content
        summary = ""
        sentiment = ""
        lines = response.split('\n')
        for line in lines:
            if line.startswith('SUMMARY:'):
                summary = line.replace('SUMMARY:', '').strip()
            elif line.startswith('SENTIMENT:'):
                sentiment = line.replace('SENTIMENT:', '').strip().lower()
        return summary, sentiment
    except Exception as e:
        print(f"Error analyzing transcript: {e}")
        return None, None

def save_to_csv(transcript, summary, sentiment):
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    csv_file = os.path.join(BASE_DIR, "output", "transcript_analysis.csv")
    file_exists = os.path.isfile(csv_file)
    with open(csv_file, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(['Timestamp', 'Transcript', 'Summary', 'Sentiment'])
        writer.writerow([
            datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            transcript[:15000] + '...' if len(transcript) > 15000 else transcript,
            summary,
            sentiment
        ])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    try:
        transcript = request.form.get('transcript', '')
        if not transcript.strip():
            return jsonify({'error': 'Transcript cannot be empty'}), 400
        summary, sentiment = analyze_transcript(transcript)
        if not summary or not sentiment:
            return jsonify({'error': 'Failed to analyze transcript'}), 500
        save_to_csv(transcript, summary, sentiment)
        return jsonify({
            'transcript': transcript,
            'summary': summary,
            'sentiment': sentiment
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    os.makedirs('output', exist_ok=True)
    app.run(debug=True, port=5000)
