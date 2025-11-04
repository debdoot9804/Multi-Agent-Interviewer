# 🤖 AI Interviewer - Multi-Agent Interview Simulation Platform

A realistic AI-powered interview simulation system built with **LangGraph** and **Azure OpenAI**. This project demonstrates multi-agent orchestration where three distinct AI agents (Technical, HR, and Manager) conduct a comprehensive interview with candidates.

## 🌟 Features

- **Multi-Agent System**: Three specialized agents with distinct personalities:
  - 💻 **Technical Agent**: Asks up to 6 technical questions focusing on coding, system design, and problem-solving
  - 🤝 **HR Agent**: Asks up to 3 questions about cultural fit, soft skills, and teamwork
  - 👔 **Manager Agent**: Asks up to 2 questions about leadership, strategy, and career vision

- **Experience-Level Adaptive**: Questions tailored to Junior, Mid-Level, or Senior positions
- **LangGraph Orchestration**: Sophisticated workflow management with state transitions
- **Azure OpenAI Integration**: Leverages Azure OpenAI models for intelligent question generation
- **Context-Aware Questions**: Agents adapt questions based on previous answers and candidate profile
- **Modular Architecture**: Clean, maintainable code following industry best practices
- **Interactive CLI**: User-friendly command-line interface with colored output
- **Interview Summary**: Complete transcript of questions and answers

## 📁 Project Structure

```
AI_Interviewer/
├── config/
│   ├── __init__.py
│   └── settings.py          # Configuration management
├── src/
│   ├── __init__.py
│   ├── agents/
│   │   ├── __init__.py
│   │   ├── base_agent.py    # Base agent class
│   │   ├── technical_agent.py
│   │   ├── hr_agent.py
│   │   └── manager_agent.py
│   ├── graph/
│   │   ├── __init__.py
│   │   ├── state.py         # State management
│   │   └── workflow.py      # LangGraph workflow
│   ├── prompts/
│   │   ├── __init__.py
│   │   └── templates.py     # Agent prompts
│   ├── utils/
│   │   ├── __init__.py
│   │   └── helpers.py       # Utility functions
│   └── __init__.py
├── tests/
├── main.py                  # Application entry point
├── azure_clients.py         # Azure OpenAI client setup
├── test_agent.py            # Test script for agents
├── .env                     # Environment variables (not in git)
├── .gitignore
├── requirements.txt
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

### Option 1: Web Interface (Recommended)

Run the beautiful Streamlit web application:

```bash
streamlit run app.py
```

The app will open in your browser with:
- 🎨 Professional UI with gradient designs
- 📊 Real-time progress tracking
- 📈 Automatic scoring and feedback
- 📋 Complete interview transcript

See [STREAMLIT_README.md](STREAMLIT_README.md) for detailed information.

### Option 2: Command Line Interface

Run the CLI version:

```bash
python main.py
```

### Testing Agent Question Generation

```bash
python test_agent.py
```

### Interview Flow

1. **Initialization**: Enter your name, job role, and experience level
2. **Technical Round**: Answer up to 6 technical questions tailored to your experience level
3. **HR Round**: Answer up to 3 HR/cultural fit questions
4. **Manager Round**: Answer up to 2 managerial/strategic questions
5. **Summary**: Option to view complete interview transcript

### Example Session

```
╔═══════════════════════════════════════════════════╗
║                                                   ║
║          🤖 AI INTERVIEWER SYSTEM 🤖             ║
║                                                   ║
║    Multi-Agent Interview Simulation Platform     ║
║                                                   ║
╚═══════════════════════════════════════════════════╝

👤 Please enter your name: John Doe
💼 Please enter the job role you're applying for: Senior Software Engineer
📊 Please enter your experience level: Senior

============================================================
💻  TECHNICAL ROUND  💻
============================================================

Question 1/6:
Hello John! I'm excited to speak with you today about the Senior Software Engineer position...
```

## 🏗️ Architecture

### LangGraph Workflow

The system uses LangGraph to orchestrate the interview process:

```
┌─────────────┐
│   Start     │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│ Technical   │──► 6 questions
│   Agent     │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│  HR Agent   │──► 3 questions
└──────┬──────┘
       │
       ▼
┌─────────────┐
│  Manager    │──► 2 questions
│   Agent     │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│     End     │
└─────────────┘
```

### State Management

The system maintains a comprehensive state using TypedDict:
- Candidate information (name, job role, experience level)
- Current agent and question counts
- Conversation history
- Question-answer pairs
- Completion status

### Agent Design

Each agent:
- Inherits from `BaseAgent`
- Has a unique personality defined in prompts
- Uses Azure OpenAI via centralized client (`azure_clients.py`)
- Maintains context from previous answers
- Adapts questions dynamically based on experience level

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

## 🛠️ Development

### Adding a New Agent

1. Create a new agent class in `src/agents/`
2. Define prompts in `src/prompts/templates.py`
3. Add node and routing logic in `src/graph/workflow.py`
4. Update state management if needed

### Customizing Questions

Edit the prompt templates in `src/prompts/templates.py` to modify:
- Agent personalities
- Question styles
- Introduction messages
- Follow-up patterns

## 📝 Future Enhancements

- [ ] Web-based UI using FastAPI
- [ ] Interview scoring and evaluation system
- [ ] Resume parsing and context injection
- [ ] Multi-language support
- [ ] Interview session persistence (save/resume)
- [ ] Analytics and insights dashboard
- [ ] Voice-based interview mode
- [ ] Real-time feedback mechanism
- [ ] Integration with job boards
- [ ] Custom question banks per industry

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

---

**Note**: This is a simulation platform for educational and practice purposes. It's designed to help candidates prepare for real interviews and demonstrate multi-agent AI orchestration with LangGraph.

---

**Note**: This is a simulation platform for educational and practice purposes. It's designed to help candidates prepare for real interviews and demonstrate multi-agent AI orchestration.
