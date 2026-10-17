from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.agents import create_agent
from langchain_core.tools import tool

load_dotenv()  # loads GROQ_API_KEY from .env


def generate_pet_name(animal_type, pet_color):
    llm = ChatGroq(model="openai/gpt-oss-120b", temperature=0.7)

    prompt = PromptTemplate(
        input_variables=["animal_type", "pet_color"],
        template="I have a {animal_type} pet and I want a cool name for it {pet_color} in color. Suggest me five cool names for my pet",
    )

    chain = prompt | llm | StrOutputParser()

    response = chain.invoke({"animal_type": animal_type, "pet_color": pet_color})
    return response

@tool
def multiply(a,b):
    """Multiply two numbers."""
    return a*b


def langchain_agents():
    llm = ChatGroq(model="openai/gpt-oss-120b", temperature=0.7)
    agent = create_agent(
        model=llm,
        tools=[multiply],
        system_prompt="You are a helpful assistant. Use tools for math.",
        debug=True
    )
    result = agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": "What is the average age of a dog? Multiply it by 3.",
                }
            ]
        }
    )
    return result["messages"][-1].content


if __name__ == "__main__":
    #print(generate_pet_name("cow", "black"))
    print(langchain_agents())
