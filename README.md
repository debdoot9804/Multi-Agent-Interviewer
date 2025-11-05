# 🤖 AI Interviewer - Multi-Agent Interview Simulation Platform

A realistic AI-powered interview simulation system built with **LangGraph** and **Azure OpenAI**. This project demonstrates multi-agent orchestration where three specialized AI agents (Technical, HR, and Manager) conduct a comprehensive interview, followed by an AI-powered evaluation.

## 🌟 Features

### Multi-Agent Interview System
- **💻 Technical Agent (Alex)**: Asks 6 technical questions focusing on coding, system design, and problem-solving
- **🤝 HR Agent (Olivia)**: Asks 3 questions about cultural fit, soft skills, and teamwork
- **👔 Manager Agent (Rahul)**: Asks 2 questions about leadership, strategy, and career vision
- **🎯 Evaluation Agent**: Provides comprehensive AI-generated feedback with scores, strengths, weaknesses, and suggestions

### Key Capabilities
- **Experience-Level Adaptive**: Questions tailored to Junior, Mid-Level, or Senior positions
- **LangGraph Orchestration**: Sophisticated workflow management with state transitions
- **Azure OpenAI Integration**: Leverages Azure OpenAI models for intelligent question generation
- **Context-Aware**: Agents adapt questions based on previous answers and candidate profile
- **Professional Web UI**: Beautiful Streamlit interface with real-time progress tracking
- **AI-Powered Evaluation**: Intelligent analysis of interview performance across all rounds
- **Modular Architecture**: Clean, maintainable code following industry best practices

## 📁 Project Structure

```
AI_Interviewer/
├── config/
│   ├── __init__.py
│   └── settings.py              # Configuration management
├── src/
│   ├── __init__.py
│   ├── agents/
│   │   ├── __init__.py
│   │   ├── base_agent.py        # Base agent class
│   │   ├── technical_agent.py   # Alex - Technical interviewer
│   │   ├── hr_agent.py          # Olivia - HR interviewer
│   │   ├── manager_agent.py     # Rahul - Hiring manager
│   │   └── evaluation_agent.py  # AI evaluation specialist
│   ├── graph/
│   │   ├── __init__.py
│   │   ├── state.py             # State management with TypedDict
│   │   └── workflow.py          # LangGraph workflow orchestration
│   └── prompts/
│       ├── __init__.py
│       └── templates.py         # Agent prompts and personalities
├── .streamlit/
│   └── config.toml              # Streamlit configuration
├── app.py                       # Streamlit web application (Main UI)
├── main.py                      # CLI application (Alternative)
├── azure_clients.py             # Azure OpenAI client setup
├── test_agent.py                # Test script for agents
├── .env                         # Environment variables (not in git)
├── .gitignore
├── requirements.txt
├── STREAMLIT_README.md          # Streamlit-specific documentation
└── README.md
```

## 🚀 Installation

### Prerequisites

- Python 3.9 or higher
- Azure OpenAI account with API access
- Git

### Setup Steps

1. **Clone the repository**:
   ```bash
   git clone https://github.com/debdoot9804/Multi-Agent-Interviewer.git
   cd Multi-Agent-Interviewer
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**:
   - macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
   - Windows:
     ```bash
     venv\Scripts\activate
     ```

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Configure your `.env` file** with your Azure OpenAI credentials:
   ```env
   OPENAI_API_KEY=your_api_key_here
   OPENAI_ENDPOINT=https://your-resource-name.openai.azure.com/
   OPENAI_CHAT_DEPLOYMENT_NAME=your_chat_deployment_name
   OPENAI_EMBED_DEPLOYMENT_NAME=your_embed_deployment_name
   API_VERSION=2024-02-15-preview
   
   # Optional: Interview Configuration
   MAX_TECHNICAL_QUESTIONS=6
   MAX_HR_QUESTIONS=3
   MAX_MANAGER_QUESTIONS=2
   TEMPERATURE=0.7
   ```

## 💻 Usage

### Streamlit Web Application (Recommended) 🌟

Run the beautiful, professional web interface:

```bash
streamlit run app.py
```

**Features:**
- 🎨 Professional gradient UI design
- 📊 Real-time progress tracking across all interview rounds
- 🤖 AI-powered evaluation with detailed feedback
- � Automatic scoring (0-100)
- 💪 Personalized strengths analysis
- 🔧 Constructive areas for improvement
- 💡 Actionable suggestions for growth
- 📋 Complete interview transcript
- 🔄 Automatic reload on code changes

The app will open in your browser at `http://localhost:8501`

See [STREAMLIT_README.md](STREAMLIT_README.md) for detailed information.

### Command Line Interface (Alternative)

Run the traditional CLI version:

```bash
python main.py
```

**Features:**
- Colored terminal output
- Interactive question-answer flow
- Interview transcript summary

### Testing Agent Question Generation

Test individual agents:

```bash
python test_agent.py
```

### Interview Flow

1. **Welcome Screen** 👋
   - Enter your name
   - Select job role
   - Choose experience level (Junior/Mid-Level/Senior)

2. **Technical Round** 💻 (6 questions)
   - Alex, the Technical Interviewer, asks coding, system design, and problem-solving questions
   - Questions adapt to your experience level

3. **HR Round** 🤝 (3 questions)
   - Olivia, the HR Manager, assesses cultural fit and soft skills
   - Focus on teamwork, communication, and values

4. **Managerial Round** 👔 (2 questions)
   - Rahul, the Hiring Manager, evaluates leadership and strategic thinking
   - Questions about decision-making and career vision

5. **AI Evaluation** 🎯
   - Comprehensive analysis of your entire interview
   - Detailed score (0-100)
   - Specific strengths identified
   - Constructive areas for improvement
   - Actionable suggestions for growth
   - Overall hiring recommendation

### Example Web Interface

Visit the app to experience:
- Beautiful gradient cards for each interview round
- Real-time question counters (e.g., "Question 3/6")
- Progress bar showing overall completion
- Professional results screen with color-coded scores
- Detailed feedback sections with icons and formatting

## 🏗️ Architecture

### LangGraph Workflow

The system uses LangGraph to orchestrate a multi-agent interview process with AI evaluation:

```
┌─────────────┐
│    Start    │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│ Technical   │──► Alex asks 6 technical questions
│   Agent     │    (Coding, system design, algorithms)
└──────┬──────┘
       │
       ▼
┌─────────────┐
│  HR Agent   │──► Olivia asks 3 HR questions
│             │    (Cultural fit, soft skills)
└──────┬──────┘
       │
       ▼
┌─────────────┐
│  Manager    │──► Rahul asks 2 managerial questions
│   Agent     │    (Leadership, strategy, vision)
└──────┬──────┘
       │
       ▼
┌─────────────┐
│ Evaluation  │──► AI analyzes entire interview
│   Agent     │    (Score, strengths, weaknesses, suggestions)
└──────┬──────┘
       │
       ▼
┌─────────────┐
│     End     │──► Display comprehensive results
└─────────────┘
```

### State Management

The system maintains comprehensive state using TypedDict:
- **Candidate Info**: name, job_role, experience_level
- **Agent Tracking**: current_agent, questions_asked per agent
- **Conversation**: conversation_history, qa_pairs
- **Progress**: is_complete, current_question, last_answer
- **Evaluation**: AI-generated evaluation results

### Agent Personalities

#### Alex - Technical Interviewer 💻
- Direct, analytical, and detail-oriented
- 10+ years of software engineering experience
- Focuses on technical depth and problem-solving
- Adapts difficulty based on experience level

#### Olivia - HR Manager 🤝
- Warm, empathetic, and people-focused
- Expert in talent acquisition and cultural fit
- Creates comfortable environment for candidates
- Excellent at reading between the lines

#### Rahul - Hiring Manager 👔
- Strategic, results-oriented, and visionary
- Direct supervisor for the role
- Assesses leadership potential and growth
- Decisive but fair in evaluation

#### Evaluation Specialist 🎯
- Comprehensive interview analysis expert
- Evaluates across technical, HR, and managerial dimensions
- Provides fair, constructive, and actionable feedback
- Considers experience level in evaluation

### Agent Design

Each agent:
- Inherits from `BaseAgent`
- Has a unique personality defined in prompt templates
- Uses Azure OpenAI via centralized client (`azure_clients.py`)
- Maintains context from previous answers
- Adapts questions dynamically based on experience level
- Generates natural, conversational questions without numbering

## ⚙️ Configuration

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `OPENAI_API_KEY` | Azure OpenAI API key | Required |
| `OPENAI_ENDPOINT` | Azure OpenAI endpoint URL | Required |
| `OPENAI_CHAT_DEPLOYMENT_NAME` | Chat deployment name | Required |
| `OPENAI_EMBED_DEPLOYMENT_NAME` | Embedding deployment name | Optional |
| `API_VERSION` | API version | 2024-02-15-preview |
| `MAX_TECHNICAL_QUESTIONS` | Max technical questions | 6 |
| `MAX_HR_QUESTIONS` | Max HR questions | 3 |
| `MAX_MANAGER_QUESTIONS` | Max manager questions | 2 |
| `TEMPERATURE` | Model temperature | 0.7 |

## 🧪 Testing

Run the test script to verify agent functionality:

```bash
python test_agent.py
```

This will test the Technical Agent's question generation with a mock interview state.

## � Recent Updates & Features

### ✨ Latest Enhancements

- ✅ **AI-Powered Evaluation Agent**: Comprehensive interview analysis with detailed feedback
- ✅ **Named Agents**: Alex (Technical), Olivia (HR), Rahul (Manager)
- ✅ **Professional Web UI**: Beautiful Streamlit interface with gradient designs
- ✅ **Real-time Progress Tracking**: Visual progress bars and question counters
- ✅ **Smart Question Flow**: Questions adapt based on experience level
- ✅ **Auto-reload**: Development mode with automatic code reload
- ✅ **Fixed Question Numbering**: Clean question display without duplication
- ✅ **Accurate Progress Counting**: Proper tracking of answered questions
- ✅ **Structured Evaluation**: Score, strengths, weaknesses, and suggestions

### 🔄 Workflow Improvements

- Proper state management with question count increments
- Routing logic optimized for smooth agent transitions
- Evaluation triggered automatically after final question
- Complete interview transcript in results

## �🛠️ Development

### Adding a New Agent

1. Create agent class in `src/agents/`:
   ```python
   from src.agents.base_agent import BaseAgent
   
   class NewAgent(BaseAgent):
       def __init__(self):
           super().__init__()
   ```

2. Define prompts in `src/prompts/templates.py`
3. Add node and routing in `src/graph/workflow.py`
4. Update state management in `src/graph/state.py` if needed
5. Export in `src/agents/__init__.py`

### Customizing Questions

Edit prompt templates in `src/prompts/templates.py`:
- Agent personalities and names
- Question styles and focus areas
- Introduction messages
- Evaluation criteria

### Running in Development Mode

Streamlit automatically reloads on file changes (configured in `.streamlit/config.toml`):
```toml
[server]
runOnSave = true
fileWatcherType = "auto"

[runner]
fastReruns = true
```

## 🎯 Future Enhancements

- [ ] ~~Web-based UI~~ ✅ **COMPLETED** (Streamlit app)
- [ ] ~~Interview evaluation system~~ ✅ **COMPLETED** (AI Evaluation Agent)
- [ ] Resume parsing and context injection
- [ ] Multi-language support
- [ ] Interview session persistence (save/resume interviews)
- [ ] Analytics and insights dashboard
- [ ] Voice-based interview mode
- [ ] Export interview results as PDF
- [ ] Integration with job boards/ATS systems
- [ ] Custom question banks per industry/role
- [ ] Video interview capability
- [ ] Mock coding environment integration
- [ ] Behavioral assessment metrics
- [ ] Interview scheduling and reminders

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is open source and available under the MIT License.

## 👤 Author

**Debdoot Debbarma**
- GitHub: [@debdoot9804](https://github.com/debdoot9804)

## 🙏 Acknowledgments

- Built with [LangGraph](https://github.com/langchain-ai/langgraph) for multi-agent orchestration
- Powered by [Azure OpenAI](https://azure.microsoft.com/en-us/products/ai-services/openai-service)
- Uses [LangChain](https://github.com/langchain-ai/langchain) framework
- UI built with [Streamlit](https://streamlit.io/)
- Colorful terminal output with [Colorama](https://github.com/tartley/colorama)

## 🌐 Live Demo

Try the live demo: [Coming Soon]

## 📸 Screenshots

### Welcome Screen
Professional interface for entering candidate information

### Interview Screen
Real-time question display with progress tracking

### Results Screen
Comprehensive AI-generated evaluation with scores and feedback

---

**Note**: This is a simulation platform for educational and practice purposes. It's designed to help candidates prepare for real interviews and demonstrates advanced multi-agent AI orchestration with LangGraph.

For questions or support, please open an issue on GitHub.

**Happy Interviewing! 🚀**
