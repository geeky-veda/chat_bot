import streamlit as st

st.set_page_config(page_title="ChatBot", page_icon="favicon.ico", layout="wide")


def home():
    st.markdown(f"# {list(page_func.keys())[0]}")
    st.markdown("<h1 style='text-align: center; color:skyblue; font-size:70px;user-select: none;'>""Welcome 😎""</h1>", unsafe_allow_html=True)
    st.markdown("""<p style='font-size: 24px;user-select: none;'>
    Certainly! Please navigate to the sidebar and select any bot that you would like to use. The sidebar typically contains a list of available bots or options for you to choose from. Once you've made your selection, you can start interacting with the chosen bot to explore its features or seek assistance.
    </p>
    """, unsafe_allow_html=True)
    st.balloons()


def pytonbot():
    import streamlit as st
    import google.generativeai as genai
    from dotenv import load_dotenv
    import os

    load_dotenv()


    api_key = st.sidebar.text_input("Enter Gemini AI API KEY",type="password")
    genai.configure(api_key=api_key)

    generation_config = {
        "temperature": 0.9,
        "top_p": 1,
        "top_k": 1,
        "max_output_tokens": 500,
        }
    model = genai.GenerativeModel("gemini-pro", generation_config=generation_config)
    st.markdown(f"# {list(page_func.keys())[1]}")

    prompt1 = st.chat_input("Say something")
    st.write("")

    if "messagespy" not in st.session_state:
        st.session_state.messagespy = []
    for messagepy in st.session_state.messagespy:
        with st.chat_message(messagepy["role"]):
            st.markdown(messagepy["content"])

    if prompt1 == None:
        st.write("")
    else:
        with st.chat_message("user"):
            st.markdown(prompt1)
            st.session_state.messagespy.append({"role": "user", "content": prompt1})
            response = model.generate_content("Python:"+prompt1)
        with st.chat_message("assistant"):
            st.write(response.text)
            st.session_state.messagespy.append({"role": "assistant", "content": response.text})
    
    
def mysqlbot():

    import streamlit as st
    import google.generativeai as genai
    from dotenv import load_dotenv
    import os

    load_dotenv()

    api_key = os.environ.get("gemini_api")
    genai.configure(api_key=api_key)

    generation_config = {
         "temperature": 0.9,
         "top_p": 1,
         "top_k": 1,
         "max_output_tokens": 1000,
    }
    model = genai.GenerativeModel("gemini-pro", generation_config=generation_config)
    st.markdown(f"# {list(page_func.keys())[2]}")

    prompt = st.chat_input("Say something")
    st.write("")

    if "messagesmy" not in st.session_state:
      st.session_state.messagesmy = []
    for messagemy in st.session_state.messagesmy:
        with st.chat_message(messagemy["role"]):
            st.markdown(messagemy["content"])

    if prompt == None:
        st.write("")
    else:
        with st.chat_message("user"):
            st.markdown(prompt)
            st.session_state.messagesmy.append({"role": "user", "content": prompt})
            response = model.generate_content("Mysql:" + prompt)
        with st.chat_message("assistant"):
            st.write(response.text)
            st.session_state.messagesmy.append({"role": "assistant", "content": response.text})

page_func= {
        "Home": home,
        "Python Bot": pytonbot,
        "Mysql Bot": mysqlbot
    }
bot_name = st.sidebar.selectbox("Select a Bot to use", page_func.keys())
page_func[bot_name]()
