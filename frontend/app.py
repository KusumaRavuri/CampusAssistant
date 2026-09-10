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


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="GITAM Campus Assistant",
    page_icon="🎓",
    layout="centered"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>

    /* --------------------------------------------------------
       Main App
    -------------------------------------------------------- */

    .stApp {
        background: linear-gradient(
            135deg,
            #0a0714 0%,
            #120a1e 50%,
            #0b0815 100%
        );
    }

    .block-container {
        max-width: 760px;
        padding-top: 3.5rem;
        padding-bottom: 3rem;
    }


    /* --------------------------------------------------------
       Header
    -------------------------------------------------------- */

    .title {
        font-size: 42px;
        font-weight: 750;
        text-align: center;
        letter-spacing: -1px;
        background: linear-gradient(
            90deg,
            #f2884a,
            #eb8a96,
            #ffffff
        );
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 8px;
    }

    .subtitle {
        text-align: center;
        color: #a7a0b8;
        font-size: 16px;
        margin-bottom: 36px;
    }


    /* --------------------------------------------------------
       Question Label
    -------------------------------------------------------- */

    .stTextInput label {
        color: #c9c2d8 !important;
        font-weight: 600 !important;
    }


    /* --------------------------------------------------------
       TEXT INPUT
       Important fix for LIGHT MODE
    -------------------------------------------------------- */

    .stTextInput input {
        background-color: #ffffff !important;
        color: #17131f !important;
        -webkit-text-fill-color: #17131f !important;

        border: 1px solid #d8d2df !important;
        border-radius: 14px !important;

        padding: 12px 15px !important;
        font-size: 15px !important;

        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.08);
    }

    .stTextInput input::placeholder {
        color: #8b8495 !important;
        -webkit-text-fill-color: #8b8495 !important;
        opacity: 1 !important;
    }

    .stTextInput input:focus {
        border-color: #f2884a !important;
        box-shadow:
            0 0 0 1px #f2884a,
            0 4px 16px rgba(242, 136, 74, 0.15) !important;
    }


    /* --------------------------------------------------------
       ASK BUTTON
    -------------------------------------------------------- */

    .stButton {
        margin-top: 8px;
    }

    .stButton button {
        width: 100%;
        min-height: 44px;

        background: linear-gradient(
            90deg,
            #f2884a,
            #eb8a96
        ) !important;

        color: #1a0f08 !important;

        border: none !important;
        border-radius: 12px !important;

        font-size: 15px !important;
        font-weight: 700 !important;

        transition: all 0.2s ease;
    }

    .stButton button:hover {
        transform: translateY(-1px);
        box-shadow:
            0 6px 18px rgba(242, 136, 74, 0.25);
    }


    /* --------------------------------------------------------
       SECTION LABELS
    -------------------------------------------------------- */

    .section-label {
        color: #f0a080;
        font-size: 12px;
        font-weight: 750;
        letter-spacing: 1.5px;
        margin-top: 30px;
        margin-bottom: 8px;
    }


    /* --------------------------------------------------------
       ANSWER CARD
    -------------------------------------------------------- */

    .answer {
        background: rgba(255, 255, 255, 0.045);

        border: 1px solid rgba(255, 255, 255, 0.10);
        border-left: 3px solid #f2884a;

        border-radius: 14px;

        padding: 20px 22px;

        color: #eeeaf3;
        font-size: 15px;
        line-height: 1.75;

        margin-top: 4px;

        box-shadow:
            0 8px 25px rgba(0, 0, 0, 0.12);
    }


    /* --------------------------------------------------------
       SOURCE CARDS
    -------------------------------------------------------- */

    .source {
        background: rgba(255, 255, 255, 0.035);

        border: 1px solid rgba(255, 255, 255, 0.08);

        border-radius: 10px;

        padding: 11px 14px;

        margin-top: 8px;

        color: #aaa2bd;

        font-size: 14px;

        transition: background 0.2s ease;
    }

    .source:hover {
        background: rgba(255, 255, 255, 0.06);
    }


    /* --------------------------------------------------------
       WARNING MESSAGE
    -------------------------------------------------------- */

    .stAlert {
        border-radius: 12px !important;
    }


    /* --------------------------------------------------------
       SPINNER
    -------------------------------------------------------- */

    .stSpinner > div {
        border-top-color: #f2884a !important;
    }


    /* --------------------------------------------------------
       MOBILE RESPONSIVE
    -------------------------------------------------------- */

    @media (max-width: 600px) {

        .block-container {
            padding-left: 1rem;
            padding-right: 1rem;
            padding-top: 2.5rem;
        }

        .title {
            font-size: 32px;
        }

        .subtitle {
            font-size: 14px;
            margin-bottom: 28px;
        }

        .answer {
            padding: 16px;
        }

    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# HEADER
# ============================================================

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


# ============================================================
# QUESTION INPUT
# ============================================================

question = st.text_input(
    "Ask your question",
    placeholder="Example: Who is eligible for course registration?",
    key="question_input"
)


# ============================================================
# ASK BUTTON
# ============================================================

if st.button("Ask"):

    if not question.strip():

        st.warning("Please enter a question.")

    else:

        with st.spinner("Searching academic regulations..."):

            answer, sources = generate_answer(question)


        # ----------------------------------------------------
        # ANSWER
        # ----------------------------------------------------

        st.markdown(
            '<div class="section-label">ANSWER</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            f'<div class="answer">{answer}</div>',
            unsafe_allow_html=True
        )


        # ----------------------------------------------------
        # SOURCES
        # ----------------------------------------------------

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
