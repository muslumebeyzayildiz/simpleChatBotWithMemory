from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.chat_history import BaseChatMessageHistory,InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

load_dotenv()

model = ChatOpenAI(model="gpt-3.5-turbo")

store = {}
#session_id bir string olacak türünü belirttik burada.
# ve session_id oturum id --->geriye BaseChatMessageHistory dönecek
def get_session_history(session_id: str) -> BaseChatMessageHistory:
    if session_id not in store:#eğer yoksa
        store[session_id] = InMemoryChatMessageHistory()
        # session_id-->key InMemoryChatMessageHistory() bunu da --->value olarak kaydet
    return store[session_id]#onn içinde kayıtlı değeri döndürmüş olyorz


prompt = ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Answer all questions to the best of your ability.",),
        MessagesPlaceholder(variable_name="messages"),
    ]
)
chain = prompt | model
config = {"configurable": {"session_id": "xyzda123"}}
with_message_history = RunnableWithMessageHistory(chain, get_session_history)
#chainin içinde hangi fonksiyonla session history sini alabileceğimi istiyor

if __name__ == "__main__":
    while True:
        user_input = input("> ")
        response = with_message_history.invoke(
            [
                HumanMessage(content=user_input)
                 ],
            config=config,
        )
        print(response.content)