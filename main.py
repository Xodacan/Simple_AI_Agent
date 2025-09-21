import openai
from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain.agents import create_tool_calling_agent, AgentExecutor
from tools import search_tool, wikipedia_tool, save_tool

load_dotenv()   

class ResearchResponse(BaseModel):
    topic: str
    summary: str
    sources: list[str]
    tools_used: list[str]



llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
llm_1= ChatAnthropic(model="claude-3-5-sonnet-20240620", temperature=0)
llm_2= OllamaLLM(model="mistral")

parser = PydanticOutputParser(pydantic_object=ResearchResponse)

prompt = ChatPromptTemplate.from_messages([
    ("system", 
    
    """
    You are a helpful assistant that can answer questions and help with tasks.
    Answer the user query by using the necessary tools.
    wrap the output in this format and return noithing else \n{format_instructions}
    """),
    ("placeholder", "{chat_history}"),
    ("human", "{query}"),
    ("placeholder", "{agent_scratchpad}"),
]).partial(format_instructions=parser.get_format_instructions())

tools = [search_tool, wikipedia_tool, save_tool]
agent = create_tool_calling_agent(
    llm = llm, 
    prompt= prompt, 
    tools=tools
)

agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True
)

query = input("what can I help you research?")
raw_response = agent_executor.invoke({"query": query})
print(raw_response)

try:
    structured_response = parser.parse(raw_response.get("output"))
    print(structured_response.topic)
except Exception as e:
    print("error parsing the response", e, "raw response", raw_response)









