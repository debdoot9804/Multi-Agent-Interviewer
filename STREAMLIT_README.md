# 🌐 Streamlit Web Interface

Beautiful, interactive web interface for the AI Interviewer platform.

## Features

- 🎨 **Professional UI**: Modern gradient designs and smooth user experience
- 📊 **Progress Tracking**: Real-time interview progress in the sidebar
- 🤖 **Multi-Agent Flow**: Seamless transition between Technical, HR, and Manager rounds
- 📈 **Scoring System**: Automatic evaluation and feedback generation
- 📋 **Interview Transcript**: Complete summary of all questions and answers
- 🎯 **Strengths & Weaknesses**: Detailed feedback on performance

## Running the App

### Quick Start

```bash
# Make sure you're in the project directory
cd /Users/debdoot/Desktop/AI_Interviewer

# Run the Streamlit app
streamlit run app.py
```

The app will automatically open in your default browser at `http://localhost:8501`

### Usage Flow

1. **Welcome Screen**
   - Enter your name
   - Select or specify your job role
   - Choose experience level (Junior/Mid-Level/Senior)
   - Click "Start Interview"

2. **Interview Process**
   - Answer questions from each agent sequentially
   - Track your progress in the sidebar
   - Submit answers to move to the next question

3. **Results Screen**
   - View your overall score (0-100)
   - Review strengths and areas for improvement
   - Access complete interview transcript
   - Start a new interview

## Screenshots

### Welcome Screen
The landing page where candidates enter their information and start the interview.

### Interview Screen
Interactive question-answer interface with progress tracking.

### Results Screen
Comprehensive feedback with scoring, strengths, and improvement areas.

## Customization

### Styling
Modify the CSS in `app.py` to change colors, gradients, and layout:
```python
st.markdown("""
<style>
    /* Your custom CSS here */
</style>
""", unsafe_allow_html=True)
```

### Scoring Algorithm
Update the `calculate_interview_score()` function in `app.py` to implement your custom scoring logic.

### Feedback Generation
Modify the `generate_feedback()` function to provide more sophisticated analysis.

## Deployment

### Streamlit Cloud (Free)

1. Push your code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Deploy your app with one click

### Docker

```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY . /app

RUN pip install -r requirements.txt

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

## Troubleshooting

**App won't start:**
- Make sure all dependencies are installed: `pip install -r requirements.txt`
- Check your `.env` file has all required API keys

**API errors:**
- Verify your Azure OpenAI credentials in `.env`
- Check API quota and limits

**Styling issues:**
- Clear browser cache
- Try a different browser

## Technologies Used

- **Streamlit**: Frontend framework
- **LangGraph**: Multi-agent orchestration
- **Azure OpenAI**: AI-powered question generation
- **Python**: Backend logic
