from typing import TypedDict

class EnterpristAssistantState(TypedDict):
    user_id: str
    session_active: bool
    last_interaction_timestamp: float
    preferences: dict[str, str]
    task_queue: list[str]
    error_state: bool
    retrieved_docs: list[str]
    message_history: list[dict[str, str]]