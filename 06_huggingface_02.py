from dotenv import load_dotenv
from langchain import HuggingFaceHub, LLMChain
from langchain.prompts import PromptTemplate

load_dotenv()

hub_llm = HuggingFaceHub(
    repo_id="gpt2",
    model_kwargs={'temperature': 0.8, 'max_length':100}
)

prompt = PromptTemplate(
    input_variables=["profession"],
    template= "You had one job! You as a  {professions} dint have to be sarcastic"
)

hub_chain = LLMChain(prompt=prompt, llm=hub_llm, verbose=True)
print(hub_chain.run("Fintech CEO"))
print(hub_chain.run("Nurse"))
print(hub_chain.run("Politician"))
print(hub_chain.run("Athlete"))
