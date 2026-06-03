import streamlit as st
import shutil
import os

DEFAULT_SETTINGS = {
    "top_k": 5,
    "score_threshold":1.3,
    "temperature": 0.0,
    "chunk_size": 1000,
    "chunk_overlap": 200,
    "memory_count": 6,
    "rerank_top_n": 3,
    "show_debug": False
}

def sidebar_settings_While_Embedding(pdf_sources=None):

    with st.sidebar:

        st.header("⚙️ Settings")

        if pdf_sources is None:
            pdf_sources = []

        pdf_filter = st.selectbox(
            "Select Document",
            ["All Documents"] + pdf_sources
        )

        top_k = st.slider(
            "Top K Chunks",
            min_value=1,
            max_value=10,
            value=DEFAULT_SETTINGS["top_k"]
        )

        rerank_top_n = st.slider(
            "Rerank Top N",
            min_value=1,
            max_value=10,
            value=DEFAULT_SETTINGS["rerank_top_n"]
        )
        
        score_threshold = st.slider(
            "Distance Threshold",
            min_value=0.0,
            max_value=2.5,
            value=DEFAULT_SETTINGS["score_threshold"]
        )

        temperature = st.slider(
            "Temperature",
            min_value=0.0,
            max_value=1.0,
            value=DEFAULT_SETTINGS["temperature"]
        )

        chunk_size = st.slider(
            "Chunk Size",
            min_value=500,
            max_value=2000,
            value=DEFAULT_SETTINGS["chunk_size"],
            step=100
        )

        chunk_overlap = st.slider(
            "Chunk Overlap",
            min_value=0,
            max_value=500,
            value=DEFAULT_SETTINGS["chunk_overlap"],
            step=50
        )

        memory_count = st.slider(
            "Messages sent to LLM",
            min_value=2,
            max_value=20,
            value=DEFAULT_SETTINGS["memory_count"],
            step=2
        )
   
        show_debug = st.checkbox(
            "Show Debug",
            value=DEFAULT_SETTINGS["show_debug"]
        )

        
    if st.sidebar.button("🗑️ Clear Chat"):
             st.session_state.messages = []
             st.rerun()

    if st.sidebar.button("Reset Vector DB"):
            if os.path.exists("vectorstore"):
                shutil.rmtree("vectorstore")

            if "vector_store" in st.session_state:
                del st.session_state.vector_store

            st.session_state.messages = []
            st.session_state.uploader_key += 1
            st.success("Vector DB reset successfully.")
            st.rerun()           

    return {
        "top_k": top_k,
        "score_threshold": score_threshold,
        "temperature": temperature,
        "chunk_size": chunk_size,
        "chunk_overlap": chunk_overlap,
        "memory_count": memory_count,
        "show_debug": show_debug,
        "rerank_top_n": rerank_top_n,
        "pdf_filter": pdf_filter
    }

def sidebar_settings(pdf_sources=None):

    with st.sidebar:

        st.header("⚙️ Settings")

        if pdf_sources is None:
            pdf_sources = []

        pdf_filter = st.selectbox(
            "Select Document",
            ["All Documents"] + pdf_sources
        )

        top_k = st.slider(
            "Top K Chunks",
            min_value=1,
            max_value=10,
            value=DEFAULT_SETTINGS["top_k"]
        )

        rerank_top_n = st.slider(
            "Rerank Top N",
            min_value=1,
            max_value=10,
            value=DEFAULT_SETTINGS["rerank_top_n"]
        )

        score_threshold = st.slider(
            "Distance Threshold",
            min_value=0.0,
            max_value=2.5,
            value=DEFAULT_SETTINGS["score_threshold"]
        )

        temperature = st.slider(
            "Temperature",
            min_value=0.0,
            max_value=1.0,
            value=DEFAULT_SETTINGS["temperature"]
        )

        memory_count = st.slider(
            "Messages sent to LLM",
            min_value=2,
            max_value=20,
            value=DEFAULT_SETTINGS["memory_count"],
            step=2
        )
   
        show_debug = st.checkbox(
            "Show Debug",
            value=DEFAULT_SETTINGS["show_debug"]
        )

    if st.sidebar.button("🗑️ Clear Chat"):
            st.session_state.messages = []
            st.rerun()
            

    if st.sidebar.button("Reset Vector DB"):
            if os.path.exists("vectorstore"):
                shutil.rmtree("vectorstore")

            if "vector_store" in st.session_state:
                del st.session_state.vector_store

            st.session_state.messages = []
            st.session_state.uploader_key += 1
            st.success("Vector DB reset successfully.")
            st.rerun()

    return {
        "top_k": top_k,
        "score_threshold": score_threshold,
        "temperature": temperature,
        "chunk_size": DEFAULT_SETTINGS["chunk_size"],
        "chunk_overlap": DEFAULT_SETTINGS["chunk_overlap"],
        "memory_count": memory_count,
        "show_debug": show_debug,
        "rerank_top_n": rerank_top_n,
        "pdf_filter": pdf_filter
    }