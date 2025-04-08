from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage

load_dotenv()
model = ChatOpenAI(model="gpt-3.5-turbo")
#message=HumanMessage(content="Hello, my name is Beyzos")
#response=model.invoke([message])
#print(response.content)

# her seferinde ayrı bölüm açış gibi hafıza olmadan cevap veriyor

#print(model.invoke([HumanMessage(content="Hello, my name is Beyzos")]))
#print(model.invoke([HumanMessage(content="What's my name?")]))

if __name__ == "__main__":
    response = model.invoke(
        [
            HumanMessage(content="Hi! I'm Beyzos"),
            AIMessage(content="Hello Beyzos! How can I assist you today?"),
            HumanMessage(content="What's my name?"),
        ]
    )
    print(response)