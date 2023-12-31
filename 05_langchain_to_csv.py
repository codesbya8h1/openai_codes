import os
from dotenv import load_dotenv
from langchain.llms.openai import OpenAI
from langchain_experimental.agents.agent_toolkits import create_csv_agent

load_dotenv()

filepath = "csv/customers.csv"
llm = OpenAI(temperature=0)
agent = create_csv_agent(llm, filepath, verbose=True)
agent.run("Whats the total number of rows?")
agent.run("Whats the total number of columns?")
agent.run("Whats the max length of the Addess column?")
agent.run("what's the longest address which has  max length?")
