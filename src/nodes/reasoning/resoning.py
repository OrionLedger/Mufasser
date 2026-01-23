from src.state_representation.enterprise_assistant import EnterpristAssistantState
from src.llms.chat_llms import REASONING_LLM

def reasoning_node(state: EnterpristAssistantState):
    """
    Uses the REASONING_LLM to generate a response based on the current state of the Enterprise Assistant.
    Args:
        state (EnterpristAssistantState): The current state of the Enterprise Assistant.
    Returns:
        str: The generated response from the reasoning LLM.
    """
    
    # Construct the input for the reasoning LLM
    question = state['message_history'][-1]['content'] if state['message_history'] else "No question found."
    context = state.get('retrieved_context', 'No context available.')
    
    prompt = f"Based on the following context:\n{context}\n\nAnswer the question:\n{question}"
    
    response = REASONING_LLM.invoke(prompt)

    return {
        "message_history": state['message_history'] + [{'role': 'reasoning', 'content': response}]
    }