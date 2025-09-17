# Transcript Analyzer Pro

A modern web application for analyzing customer call transcripts using AI-powered sentiment analysis and summarization.

## Features

- **AI-Powered Analysis**: Utilizes advanced algorithms to analyze transcript content
- **Sentiment Analysis**: Detects customer sentiment (Positive, Neutral, Negative) with confidence scoring
- **Smart Summarization**: Generates concise 2-3 sentence summaries of conversations
- **Real-time Processing**: Provides instant analysis with visual feedback
- **Beautiful UI**: Modern, responsive design with smooth animations
- **Export Functionality**: Results are saved to CSV for further analysis

## Installation

1. Clone or download the project files
```bash
git clone https://github.com/shivangrustagi04/sushtend.git
cd sushtend
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```
3. Create a .env file in the root directory and add your Groq API key:
```bash
echo "GROQ_API_KEY=your_groq_api_key_here" > .env
```
4. Run the Flask application:
```bash
python app.py
```
5. Open your browser and navigate to http://localhost:5000

## Usage
Paste a customer call transcript into the text area

Click the "Analyze Transcript" button

View the AI-generated summary and sentiment analysis

Results are automatically saved to output/transcript_analysis.csv

## File Structure
```bash
sushtend/
├── app.py                 # Flask backend server
├── requirements.txt       # Python dependencies
├── .env                  # Environment variables (create this)
├── output/
│   └── transcript_analysis.csv  # Analysis results
└── templates/
    └── index.html        # Main web interface
```

## Technologies Used
**Backend**: Python, Flask

**Frontend**: HTML5, CSS3, JavaScript

**AI API**: Groq

**Styling**: Custom CSS with gradients and animations

## Support
For issues or questions, please check the console for error messages or ensure your API key is properly set in the .env file.


