import os
from langchain.llms import OpenAI
from langchain.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain
from dotenv import load_dotenv


load_dotenv()

dburi = "sqlite:///sqlitedb/chinook.db"
db = SQLDatabase.from_uri(dburi)

llm = OpenAI(temperature=0)

db_chain = SQLDatabaseChain.from_llm(
    llm=llm,
    db=db,
    verbose=True
)

#db_chain.run("List all the tables in the database")
# db_chain.run("What is the total number of employees and total number of distinct employees?")
# db_chain.run("What is the schema of the cutstomer table?")
db_chain.run("give me the names of top five countries where most of the customers are from in decreasing order.")