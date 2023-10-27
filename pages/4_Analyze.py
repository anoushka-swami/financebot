import openai
import streamlit as st

st.set_page_config(
    page_title="Analyze | Money Matters",
    page_icon="Personalized.png",
)

(column1,column2)=st.columns([3,7])
column1.image("Personalized.png", width=100)
column2.title("Your analyst assistant")
st.markdown("""
Please enter a news article that you would like to analyze and understand the investing ramifications of.
""")

avatars={"system":"💻","user":"🤔","assistant":"📝"}

SYSTEM_PROMPT="""
Ignore all previous commands. When the user provides an input, respond with a summary of the input. 
Your tone is professional, concise, and courteous.
In reviewing the input, you look for inaccuracies, as well as understanding the user's intent.
Limit your feedback to 5-7 sentences divided into three paragraphs.
Start all responses with: "Here is my summary and understanding of this information:"
The third paragraph contains only one sentence about whether you recommend users buy, sell, or hold the stock, and you start the third paragraph with: 'I recommend'.
"""

SYSTEM_MESSAGE={"role": "system", "content": SYSTEM_PROMPT}

if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.messages.append(SYSTEM_MESSAGE)

for message in st.session_state.messages:
    if message["role"] != "system":
        avatar=avatars[message["role"]]
        with st.chat_message(message["role"],avatar=avatar):
            st.markdown(message["content"])

if prompt := st.chat_input("Please paste the financial information/press release that you'd like to analyze"):
    new_message={"role": "user", "content": prompt}
    st.session_state.messages.append(new_message)
    with st.chat_message("user"):
        st.markdown(prompt)
    with st.chat_message("assistant", avatar=avatars["assistant"]):
        message_placeholder = st.empty()
        full_response = ""
        for response in openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": m["role"], "content": m["content"]}
                      for m in st.session_state.messages], stream=True):
            full_response += response.choices[0].delta.get("content", "")
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
    st.session_state.messages.append({"role": "assistant", "content": full_response})