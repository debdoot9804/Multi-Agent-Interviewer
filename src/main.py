"""
Main application entry point for the AI Interviewer.
"""
import sys
import os
from dotenv import load_dotenv

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from config import get_settings
from src.graph.state import create_initial_state, Message
from src.graph.workflow import InterviewWorkflow
from src.utils import (
    print_banner,
    print_agent_header,
    print_question,
    print_answer_prompt,
    print_completion_message,
    print_error,
    print_info,
    format_conversation_summary,
)


def get_candidate_info() -> tuple[str, str]:
    """
    Get candidate information from user input.
    
    Returns:
        tuple: (candidate_name, job_role)
    """
    print_banner()
    print_info("Welcome to the AI Interviewer! Let's get started.\n")
    
    candidate_name = input("👤 Please enter your name: ").strip()
    while not candidate_name:
        print_error("Name cannot be empty.")
        candidate_name = input("👤 Please enter your name: ").strip()
    
    job_role = input("💼 Please enter the job role you're applying for: ").strip()
    while not job_role:
        print_error("Job role cannot be empty.")
        job_role = input("💼 Please enter the job role you're applying for: ").strip()
    
    print_info(f"\nGreat! Starting your interview for {job_role} position.\n")
    input("Press Enter to begin...")
    
    return candidate_name, job_role


def run_interview():
    """Main function to run the interview."""
    try:
        # Load environment variables
        load_dotenv()
        
        # Get settings
        settings = get_settings()
        
        # Get candidate information
        candidate_name, job_role = get_candidate_info()
        
        # Initialize state
        state = create_initial_state(candidate_name, job_role)
        
        # Create workflow
        workflow = InterviewWorkflow(settings)
        
        # Track current agent for UI
        current_agent_type = None
        
        # Run interview loop
        while not state["is_complete"]:
            # Check if agent changed
            if state["current_agent"] != current_agent_type:
                current_agent_type = state["current_agent"]
                if current_agent_type != "complete":
                    print_agent_header(current_agent_type)
            
            # Clear last answer before getting new question
            state["last_answer"] = None
            
            # Get next question from workflow
            state = workflow.run_step(state)
            
            # Display the question
            if state["current_question"]:
                agent_type = state["current_agent"]
                
                # Determine question number and max for current agent
                if agent_type == "technical":
                    q_num = state["technical_questions_asked"]
                    max_q = settings.max_technical_questions
                elif agent_type == "hr":
                    q_num = state["hr_questions_asked"]
                    max_q = settings.max_hr_questions
                else:  # manager
                    q_num = state["manager_questions_asked"]
                    max_q = settings.max_manager_questions
                
                print_question(state["current_question"], q_num, max_q)
                
                # Get candidate's answer
                print_answer_prompt()
                answer = input().strip()
                
                # Validate answer
                while not answer:
                    print_error("Answer cannot be empty. Please provide an answer.")
                    print_answer_prompt()
                    answer = input().strip()
                
                # Process the answer
                state = workflow.process_answer(state, answer)
                print()  # Add spacing
        
        # Interview completed
        print_completion_message()
        
        # Ask if they want to see summary
        show_summary = input("\nWould you like to see the interview summary? (y/n): ").strip().lower()
        if show_summary == 'y':
            summary = format_conversation_summary(state["qa_pairs"])
            print(summary)
        
        print_info("Thank you for using AI Interviewer!")
        
    except KeyboardInterrupt:
        print("\n\n" + "=" * 60)
        print_info("Interview interrupted by user.")
        print("=" * 60)
        sys.exit(0)
    except Exception as e:
        print_error(f"An unexpected error occurred: {str(e)}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    run_interview()
