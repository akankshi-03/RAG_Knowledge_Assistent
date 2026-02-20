import streamlit as st
from rag_chatbot import setup_rag, get_answer

st.set_page_config(page_title="Hybrid RAG Assistant", layout="wide")

st.title("🚀 Hybrid RAG Knowledge Assistant")

# ---------------- SIDEBAR ---------------- #

st.sidebar.header("📂 Document Control")

uploaded_file = st.sidebar.file_uploader("Upload your PPT file", type=["pptx"])

# Reset Chat Button
if st.sidebar.button("🔄 Reset Chat"):
    st.session_state.messages = []
    st.success("Chat reset successfully!")

# ---------------- MAIN LOGIC ---------------- #

if uploaded_file:

    # Re-index when new file uploaded
    if "current_file" not in st.session_state or st.session_state.current_file != uploaded_file.name:
        with st.spinner("Indexing document... Please wait..."):
            setup_rag(uploaded_file)
            st.session_state.current_file = uploaded_file.name
            st.session_state.messages = []
        st.success("✅ Document indexed successfully!")

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat history
    for role, message in st.session_state.messages:
        with st.chat_message(role):
            st.markdown(message)

    # Chat input (ChatGPT style)
    if prompt := st.chat_input("Ask something about the document..."):

        # Show user message
        with st.chat_message("user"):
            st.markdown(prompt)

        st.session_state.messages.append(("user", prompt))

        # Get bot response
        with st.spinner("Thinking..."):
            answer, sources = get_answer(prompt)

        # Show bot message
        with st.chat_message("assistant"):
            st.markdown(answer)

            # Expandable source viewer
            with st.expander("🔍 View Retrieved Sources"):
                for i, chunk in enumerate(sources):
                    st.markdown(f"**Source {i+1}:**")
                    st.write(chunk)

        st.session_state.messages.append(("assistant", answer))

else:
    st.info("👈 Please upload a PPT file to start chatting.")