import streamlit as st
import pandas as pd
from openai import OpenAI

st.set_page_config(
    page_title="Home | Money Matters",
    page_icon="Personalized.png",
)
print("set page config")
#title the page
#st.title("Money Matters!")
#display an image
st.image("Personalized.png", width=400)

st.title("About the website")
print("set page title and image")
st.write("""
         **:green[Welcome to Money Matters!]** Here, we hope to help you take charge of your financial destiny 
         by learning about personal finance. 
         
         - With the **:green[learn]** page, you can learn or refresh key personal finance concepts.
         - With the **:green[ask]** page, you can ask our Chat-GPT-based AI any burning finance questions you have. It has been augmented to ensure specificity and reliability.
         - With the **:green[apply]** page, you can quiz yourself on personal finance basics. These help you figure out where there may be gaps in your knowledge.
         - With the **:green[analyze]** page, you can paste in any company press release or other article and we will summarize it and assess whether or not the company would be a good investment right now.
         
         We have augmented our AI using a set of carefully curated resources from reputable sources such as Khan Academy, the Federal Reserve Bank of St. Louis, TED-Ed, DardenMBA, PBS, and moneyinstructor.com, and *greatly appreciate* being able to build on their great work.
         """)

print("reached the end")

#create two tabs and add elements to each
# asktab, learntab = st.tabs(["Ask", "Learn"])
# asktab.write("**This is a chatbot. Ask it anything!**")
# learntab.write("**Scroll through and learn.**")

# with learntab.expander("Learn more about stocks:"):
#     st.write("""
#         Investing in stocks means owning parts of a company.
#         more stuff about investing, ...
#     """)

# learntab.video("https://www.ted.com/talks/oliver_elfenbaum_how_does_the_stock_market_work?language=en", format="video/mp3")


# openai.api_key = st.secrets["database"]["OPENAI_API_KEY"]

# message_placeholder = st.empty()
# full_response = ""

# #Set a default model
# if "openai_model" not in st.session_state:
#     st.session_state["openai_model"] = "gpt-3.5-turbo"

# # Initialize chat history
# if "messages" not in st.session_state:
#     st.session_state.messages = []
#     #st.session_state.messages.append({"role": "system", "content": "Please provide the user good financial advice"})


# # Display chat messages from history on app rerun
# for message in st.session_state.messages:
#     with asktab.chat_message(message["role"]):
#         asktab.markdown(message["content"])

# asktab.chat_message("Ask any finance question")

# # Accept user input
# if prompt := st.chat_input("Ask any finance question"):
#    #  Add user message to chat history
#     st.session_state.messages.append({"role": "user", "content": prompt})
#     # Display user message in chat message container
#     with asktab.chat_message("user"):
#         asktab.markdown(prompt)
#      #Display assistant response in chat message container

#     with st.chat_message("assistant"):
#         for response in openai.ChatCompletion.create(
#         model=st.session_state["openai_model"],
#         messages=[{"role": m["role"], "content": m["content"]} for m in st.session_state.messages],
#         stream=True,
#     ):
#         full_response += response.choices[0].delta.get("content", "")
#         message_placeholder.markdown(full_response + "▌")
#         message_placeholder.markdown(full_response)
#     st.session_state.messages.append({"role": "assistant", "content": full_response})
    
#     message_placeholder = st.empty()
#         full_response = ""
#         for response in openai.ChatCompetion.create(
#             model="gpt-3.5-turbo",
#             messages=[
#                 {"role": m["role"], "content": m["content"]}
#                 for m in st.session_state.messages
#             ],
#             stream=True,
#         ):
#             full_response += response.choices[0].delta.get("content", "")
#             message_placeholder.markdown(full_response + "▌")
#         message_placeholder.markdown(full_response)
#     st.session_state.messages.append({"role": "assistant", "content": full_response})
    
#     for response in openai.ChatCompletion.create(
#         model=st.session_state["openai_model"],
#         messages=[{"role": m["role"], "content": m["content"]} for m in st.session_state.messages],
#         stream=True,
#     ):
#         full_response += response.choices[0].delta.get("content", "")
#         message_placeholder.markdown(full_response + "▌")
#         message_placeholder.markdown(full_response)
#     st.session_state.messages.append({"role": "assistant", "content": full_response})
