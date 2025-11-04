"""
LangGraph workflow for orchestrating the AI interview.
"""
from typing import Dict, Any, Literal
from langgraph.graph import StateGraph, END
from config.settings import Settings
from src.agents import TechnicalAgent, HRAgent, ManagerAgent
from src.graph.state import InterviewState, Message, QuestionAnswer


class InterviewWorkflow:
    """Manages the interview workflow using LangGraph."""
    
    def __init__(self, settings: Settings):
        """
        Initialize the interview workflow.
        
        Args:
            settings: Application settings
        """
        self.settings = settings
        self.technical_agent = TechnicalAgent(settings)
        self.hr_agent = HRAgent(settings)
        self.manager_agent = ManagerAgent(settings)
        self.graph = self._create_graph()
    
    def _create_graph(self) -> StateGraph:
        """
        Create the LangGraph workflow.
        
        Returns:
            StateGraph: Compiled workflow graph
        """
        # Create the graph
        workflow = StateGraph(InterviewState)
        
        # Add nodes for each agent
        workflow.add_node("technical", self._technical_node)
        workflow.add_node("hr", self._hr_node)
        workflow.add_node("manager", self._manager_node)
        
        # Add conditional edges to determine flow
        workflow.add_conditional_edges(
            "technical",
            self._route_from_technical,
            {
                "hr": "hr",
                "continue": "technical",
                "end": END
            }
        )
        
        workflow.add_conditional_edges(
            "hr",
            self._route_from_hr,
            {
                "manager": "manager",
                "continue": "hr",
                "end": END
            }
        )
        
        workflow.add_conditional_edges(
            "manager",
            self._route_from_manager,
            {
                "continue": "manager",
                "end": END
            }
        )
        
        # Set entry point
        workflow.set_entry_point("technical")
        
        return workflow.compile()
    
    def _technical_node(self, state: InterviewState) -> InterviewState:
        """
        Technical agent node - asks technical questions.
        
        Args:
            state: Current interview state
            
        Returns:
            InterviewState: Updated state
        """
        # Generate question
        question = self.technical_agent.ask_question(state)
        
        # Update state
        state["current_question"] = question
        state["technical_questions_asked"] += 1
        
        # Add to conversation history
        message = Message(
            role="agent",
            content=question,
            agent_type="technical"
        )
        state["conversation_history"].append(message)
        
        return state
    
    def _hr_node(self, state: InterviewState) -> InterviewState:
        """
        HR agent node - asks HR questions.
        
        Args:
            state: Current interview state
            
        Returns:
            InterviewState: Updated state
        """
        # Generate question
        question = self.hr_agent.ask_question(state)
        
        # Update state
        state["current_question"] = question
        state["hr_questions_asked"] += 1
        state["current_agent"] = "hr"
        
        # Add to conversation history
        message = Message(
            role="agent",
            content=question,
            agent_type="hr"
        )
        state["conversation_history"].append(message)
        
        return state
    
    def _manager_node(self, state: InterviewState) -> InterviewState:
        """
        Manager agent node - asks managerial questions.
        
        Args:
            state: Current interview state
            
        Returns:
            InterviewState: Updated state
        """
        # Generate question
        question = self.manager_agent.ask_question(state)
        
        # Update state
        state["current_question"] = question
        state["manager_questions_asked"] += 1
        state["current_agent"] = "manager"
        
        # Add to conversation history
        message = Message(
            role="agent",
            content=question,
            agent_type="manager"
        )
        state["conversation_history"].append(message)
        
        return state
    
    def _route_from_technical(
        self, state: InterviewState
    ) -> Literal["hr", "continue", "end"]:
        """
        Determine routing after technical questions.
        
        Args:
            state: Current interview state
            
        Returns:
            str: Next node to visit
        """
        if state["technical_questions_asked"] >= self.settings.max_technical_questions:
            return "hr"
        
        # Check if we have an answer to process
        if state.get("last_answer"):
            return "continue"
        
        return "end"
    
    def _route_from_hr(
        self, state: InterviewState
    ) -> Literal["manager", "continue", "end"]:
        """
        Determine routing after HR questions.
        
        Args:
            state: Current interview state
            
        Returns:
            str: Next node to visit
        """
        if state["hr_questions_asked"] >= self.settings.max_hr_questions:
            return "manager"
        
        # Check if we have an answer to process
        if state.get("last_answer"):
            return "continue"
        
        return "end"
    
    def _route_from_manager(
        self, state: InterviewState
    ) -> Literal["continue", "end"]:
        """
        Determine routing after manager questions.
        
        Args:
            state: Current interview state
            
        Returns:
            str: Next node to visit
        """
        if state["manager_questions_asked"] >= self.settings.max_manager_questions:
            state["is_complete"] = True
            state["current_agent"] = "complete"
            return "end"
        
        # Check if we have an answer to process
        if state.get("last_answer"):
            return "continue"
        
        return "end"
    
    def process_answer(self, state: InterviewState, answer: str) -> InterviewState:
        """
        Process a candidate's answer and update state.
        
        Args:
            state: Current interview state
            answer: Candidate's answer
            
        Returns:
            InterviewState: Updated state
        """
        # Add answer to conversation history
        message = Message(
            role="user",
            content=answer,
            agent_type=None
        )
        state["conversation_history"].append(message)
        
        # Create QA pair
        if state["current_question"]:
            qa_pair = QuestionAnswer(
                question=state["current_question"],
                answer=answer,
                agent_type=state["current_agent"]
            )
            state["qa_pairs"].append(qa_pair)
        
        # Set last answer for routing
        state["last_answer"] = answer
        
        return state
    
    def run_step(self, state: InterviewState) -> InterviewState:
        """
        Run one step of the interview workflow.
        
        Args:
            state: Current interview state
            
        Returns:
            InterviewState: Updated state after one step
        """
        # Invoke the graph for one step
        result = self.graph.invoke(state)
        return result
