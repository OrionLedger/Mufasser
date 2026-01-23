from langchain_openai import ChatOpenAI

ANALYZER_LLM = ChatOpenAI(
    model_name="gpt-4o-mini",
    temperature=0,
)

REASONING_LLM = ChatOpenAI(
    model="gpt-4o",
    temperature=0.2
)
