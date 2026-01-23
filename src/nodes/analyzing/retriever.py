from src.state_representation.enterprise_assistant import EnterpristAssistantState
from src.tools.retrieve_context import retrieve_context
from src.llms.chat_llms import ANALYZER_LLM
from langchain_core.prompts import ChatPromptTemplate

def retriever_node(state: EnterpristAssistantState) -> str:
    """
    Analyzes the current state of the Enterprise Assistant and retrieves relevant information.
    Args:
        state (EnterpristAssistantState): The current state of the Enterprise Assistant.
    Returns:
        str: A summary of the relevant information retrieved from the state.
    """
    
    ## Construct the prompt for the LLM
    question = state['message_history'][-1]['content'] if state['message_history'] else "No question found."
    prompt = ChatPromptTemplate.from_template(
        """
        Given the following state of the Enterprise Assistant:\n{state}\n\nQuestion: {question}\n\nform a query that will be used to retrieve relevant information from the knowledge base.
        only provide the query without any additional explanation.
        """
    )
    
    formatted_prompt = prompt.format(state=state, question=question)
    response = ANALYZER_LLM.invoke(formatted_prompt)

    return {
        "retrieved_docs": state['retrieved_docs'] + [response]
    }