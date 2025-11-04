"""
Utility functions for the AI Interviewer.
"""
from typing import List
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)


def print_banner():
    """Print the application banner."""
    banner = """
    ╔═══════════════════════════════════════════════════╗
    ║                                                   ║
    ║          🤖 AI INTERVIEWER SYSTEM 🤖             ║
    ║                                                   ║
    ║    Multi-Agent Interview Simulation Platform     ║
    ║                                                   ║
    ╚═══════════════════════════════════════════════════╝
    """
    print(Fore.CYAN + banner + Style.RESET_ALL)


def print_agent_header(agent_type: str):
    """
    Print header when an agent takes over.
    
    Args:
        agent_type: Type of agent (technical, hr, manager)
    """
    headers = {
        "technical": {
            "title": "TECHNICAL ROUND",
            "emoji": "💻",
            "color": Fore.BLUE
        },
        "hr": {
            "title": "HR ROUND",
            "emoji": "🤝",
            "color": Fore.GREEN
        },
        "manager": {
            "title": "MANAGERIAL ROUND",
            "emoji": "👔",
            "color": Fore.MAGENTA
        }
    }
    
    header = headers.get(agent_type, {"title": "INTERVIEW", "emoji": "📋", "color": Fore.WHITE})
    
    separator = "=" * 60
    print(f"\n{header['color']}{separator}")
    print(f"{header['emoji']}  {header['title']}  {header['emoji']}")
    print(f"{separator}{Style.RESET_ALL}\n")


def print_question(question: str, question_num: int, max_questions: int):
    """
    Print an interview question.
    
    Args:
        question: The question text
        question_num: Current question number
        max_questions: Maximum number of questions for this agent
    """
    print(f"{Fore.YELLOW}Question {question_num}/{max_questions}:{Style.RESET_ALL}")
    print(f"{Fore.WHITE}{question}{Style.RESET_ALL}\n")


def print_answer_prompt():
    """Print the prompt for the candidate to answer."""
    print(f"{Fore.CYAN}Your answer: {Style.RESET_ALL}", end="")


def print_completion_message():
    """Print interview completion message."""
    message = """
    ╔═══════════════════════════════════════════════════╗
    ║                                                   ║
    ║         ✅ INTERVIEW COMPLETED! ✅               ║
    ║                                                   ║
    ║   Thank you for participating in this interview  ║
    ║                                                   ║
    ╚═══════════════════════════════════════════════════╝
    """
    print(Fore.GREEN + message + Style.RESET_ALL)


def print_error(message: str):
    """
    Print an error message.
    
    Args:
        message: Error message to display
    """
    print(f"{Fore.RED}❌ Error: {message}{Style.RESET_ALL}")


def print_info(message: str):
    """
    Print an info message.
    
    Args:
        message: Info message to display
    """
    print(f"{Fore.CYAN}ℹ️  {message}{Style.RESET_ALL}")


def format_conversation_summary(qa_pairs: List[dict]) -> str:
    """
    Format the interview conversation as a summary.
    
    Args:
        qa_pairs: List of question-answer pairs
        
    Returns:
        str: Formatted summary
    """
    summary = "\n" + "=" * 60 + "\n"
    summary += "INTERVIEW SUMMARY\n"
    summary += "=" * 60 + "\n\n"
    
    current_agent = None
    for qa in qa_pairs:
        # Print agent header if changed
        if qa["agent_type"] != current_agent:
            current_agent = qa["agent_type"]
            agent_names = {
                "technical": "TECHNICAL ROUND",
                "hr": "HR ROUND",
                "manager": "MANAGERIAL ROUND"
            }
            summary += f"\n--- {agent_names.get(current_agent, 'UNKNOWN')} ---\n\n"
        
        summary += f"Q: {qa['question']}\n"
        summary += f"A: {qa['answer']}\n\n"
    
    summary += "=" * 60 + "\n"
    return summary
