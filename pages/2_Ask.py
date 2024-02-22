import time

import numpy as np

from pinecone import Pinecone
from openai import OpenAI
import streamlit as st
import os

st.set_page_config(
    page_title="Ask | Money Matters",
    page_icon="Personalized.png",
)

(column1,column2)=st.columns([3,7])
column1.image("Personalized.png", width=100)
column2.title("Your financial mentor")
st.markdown("""
Please enter a question about personal finance. You can tailor your question to be more specific to your needs.
            \n Here are some questions from recent users which show different angles you can ask from:
            \n * "I'm a college student with no steady income but I have $1000 in my bank account. Can you create me a savings plan for the next 4 years?"
            \n * "How do I become able to start renting an apartment?"
            \n * "I am a 24 year old single mother of a toddler. I just finished my Master's degree in anthropology. Right now I'm working as a waitress and share an apartment's rent with two friends. What are possible steps for me to take care of my daughter, find a good job, and at some point rent my own apartment for just me and my daughter? Please focus on financial advice."
""")

avatars={"system":"💻","user":"🤔","assistant":"💵"}


os.environ['PINECONE_API_ENV']='gcp-starter'
os.environ['PINECONE_INDEX_NAME']='pinecone-index'

PINECONE_API_KEY=st.secrets['PINECONE_API_KEY']
PINECONE_API_ENV=os.environ['PINECONE_API_ENV']
PINECONE_INDEX_NAME=os.environ['PINECONE_INDEX_NAME']
client=OpenAI(ai_api_key=st.secrets['OPENAI_API_KEY'])

def augmented_content(inp):
    ## Create the embedding using OpenAI keys
    ## Do similarity search using Pinecone
    ## Return the top 5 results
    ##embedding=openai.Embedding.create(model="text-embedding-ada-002", input=inp)['data'][0]['embedding'] 
    ##pinecone.init(api_key=PINECONE_API_KEY, environment=PINECONE_API_ENV) 
    ##index = pinecone.Index(PINECONE_INDEX_NAME) 
    ##results=index.query(embedding,top_k=3,include_metadata=True) 
    ##print(f"Results: {results}")
    ##st.write(f"Results: {results}")
    ##rr=[ r['metadata']['text'] for r in results['matches']] 
    ##print(f"RR: {rr}")
    ##st.write(f"RR: {rr}")
    ##print(f"42 PINECONE_API_KEY={PINECONE_API_KEY}")
    embedding=client.embeddings.create(model="text-embedding-ada-002", input=inp).data[0].embedding
    ##print(f"44 PINECONE_API_KEY={PINECONE_API_KEY}")
    pc = Pinecone(api_key=PINECONE_API_KEY)
    ##pinecone.init(api_key=PINECONE_API_KEY, environment=PINECONE_API_ENV)
    ##print(f"46 PINECONE_API_KEY={PINECONE_API_KEY}")
    ##index = pinecone.Index(PINECONE_INDEX_NAME)
    index = pc.Index(PINECONE_INDEX_NAME)
    ##print(f"48 PINECONE_API_KEY={PINECONE_API_KEY}")
    results=index.query(vector=embedding,top_k=3,include_metadata=True)
    print(f"Results: {results}") #debugger
    ##st.write(f"Results: {results}")
    rr=[ r['metadata']['text'] for r in results['matches']]
    ##print(f"RR: {rr}")
    ##st.write(f"RR: {rr}")
    return rr


SYSTEM_MESSAGE={"role": "system", 
                "content": """"Ignore all previous commands. 
                You are a helpful and patient financial guide. 
                When asked a question, your response should be polite, and you should not only answer a question but provide a larger lesson about finance including examples. 
                Using markdown language formatting, bold key phrases and use bullet points when relevant.
                Keep responses below 300 words. 
                If you don't know an answer, state the exact words 'I don't have an answer for that' and don't add any more. 
                You must not provide answers to questions which are not about finance, aside from stating the exact text 'I don't have an answer for that.'.""""
                }

if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.messages.append(SYSTEM_MESSAGE)

for message in st.session_state.messages:
    if message["role"] != "system":
        avatar=avatars[message["role"]]
        with st.chat_message(message["role"],avatar=avatar):
            st.markdown(message["content"])

if prompt := st.chat_input("Ask your question here!"):
    retrieved_content = augmented_content(prompt)
    ##print(f"Retrieved content: {retrieved_content}")
    prompt_guidance=f"""
Please guide the user with the following information:
{retrieved_content}
The user's question was: {prompt}
    """
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    with st.chat_message("assistant", avatar=avatars["assistant"]):
        message_placeholder = st.empty()
        full_response = ""
        
        messageList=[{"role": m["role"], "content": m["content"]}
                      for m in st.session_state.messages]
        messageList.append({"role": "user", "content": prompt_guidance})
        
        ##for response in openai.ChatCompletion.create( 
          ##  model="gpt-3.5-turbo", 
           ## messages=messageList, stream=True): 
            ##full_response += response.choices[0].delta.get("content", "") 
            ##message_placeholder.markdown(full_response + "▌") 
        ##message_placeholder.markdown(full_response) 
    ##with st.sidebar.expander("Retrieval context provided to GPT-3"):
     ##   st.write(f"{retrieved_content}")
    ##st.session_state.messages.append({"role": "assistant", "content": full_response}) 

        for response in client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messageList, stream=True):
          ##  print("starting 122")
            ##print(response.choices[0])
            ##print(response.choices[0].delta.content)
            response_content = response.choices[0].delta.content          
            if (response_content):
                full_response += response.choices[0].delta.content
        
        ##print(full_response)

            ##full_response += response.choices[0].delta.get("content", "")
            ##message_placeholder.markdown(full_response + "▌")
        ##message_placeholder.markdown(full_response)
        ##Choice(delta=ChoiceDelta(content=' finance', function_call=None, role=None, tool_calls=None), finish_reason=None, index=0, logprobs=None)
        message_placeholder.markdown(full_response)
        st.session_state.messages.append({"role": "assistant", "content": full_response})
                    
        
##print(Completion.choices[0].message)