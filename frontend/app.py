import streamlit as st
import sys
import os

# Allow Python to find backend
sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from backend.rag import generate_answer


# -----------------------------
# Page configuration
# -----------------------------

st.set_page_config(
    page_title="GITAM Campus Assistant",
    page_icon="🎓",
    layout="centered"
)


# -----------------------------
# CSS
# -----------------------------

st.markdown("""
<style>

.stApp {
    background: linear-gradient(
        135deg,
        #0a0714,
        #120a1e
    );
    color: white;
}

.block-container {
    max-width: 750px;
    padding-top: 4rem;
}

.title {
    font-size: 42px;
    font-weight: 700;
    text-align: center;
    background: linear-gradient(
        90deg,
        #f2884a,
        #eb8a96,
        #ffffff
    );
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.subtitle {
    text-align: center;
    color: #9d95b5;
    font-size: 16px;
    margin-bottom: 40px;
}

.stTextInput input {
    background: rgba(255,255,255,0.05);
    color: white;
    border: 1px solid rgba(255,255,255,0.15);
    border-radius: 12px;
}

.stButton button {
    background: linear-gradient(
        90deg,
        #f2884a,
        #eb8a96
    );
    color: #1a0f08;
    border: none;
    border-radius: 10px;
    font-weight: 600;
}

.answer {
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(255,255,255,0.1);
    border-left: 3px solid #f2884a;
    border-radius: 12px;
    padding: 20px;
    margin-top: 15px;
    line-height: 1.7;
}

.source {
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 10px;
    padding: 10px 14px;
    margin-top: 8px;
    color: #aaa2bd;
    font-size: 14px;
}

</style>
""", unsafe_allow_html=True)


# -----------------------------
# Header
# -----------------------------

st.markdown(
    '<div class="title">🎓 Campus Assistant</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Ask questions about GITAM academic regulations'
    '</div>',
    unsafe_allow_html=True
)


# -----------------------------
# Question
# -----------------------------

question = st.text_input(
    "Ask your question",
    placeholder="Example: Who is eligible for course registration?"
)


# -----------------------------
# Ask
# -----------------------------

if st.button("Ask"):

    if not question.strip():

        st.warning("Please enter a question.")

    else:

        with st.spinner("Searching academic regulations..."):

            answer, sources = generate_answer(question)

        st.markdown(
            '<div class="section-label">ANSWER</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            f'<div class="answer">{answer}</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            '<div class="section-label">SOURCES</div>',
            unsafe_allow_html=True
        )

        for source in sources:

            st.markdown(
                f"""
                <div class="source">
                    📄 Page {source['page']} —
                    {source['source']}
                </div>
                """,
                unsafe_allow_html=True
            )