import os
from langchain_openai import ChatOpenAI
from langchain_community.agent_toolkits.load_tools import load_tools
from langchain.agents import initialize_agent

# from openai import OpenAI
# from dotenv import load_dotenv

# load_dotenv()
# print(os.environ.get("OPENAI_API_KEY")) #key should now be available

# ChatOpenAI(api_key = os.environ.get("OPENAI_API_KEY"))
# ChatOpenAI(api_key = "")


llm = ChatOpenAI(model="gpt-3.5-turbo", api_key="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")
tools = load_tools(["ddg-search", "wikipedia"], llm=llm)

# print(tools[0].name, tools[0].description)


agent = initialize_agent(tools, llm, agent="zero-shot-react-description", verbose=True)
print('--------------------------------------------------------------------------------------------------------------------------------------------')
# print(agent.agent.llm_chain.prompt.template)

query = """
Vou viajar para Londres em novembro de2024. Quero que faça um roteiro de viagem para mim com eventos que irão ocorrer na data da viagem e com preço  de passagem de São Paulo para Londres.
"""

agent.run(query)