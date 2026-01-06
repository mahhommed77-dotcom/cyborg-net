import streamlit as st

# 1. إعدادات الهوية البصرية (Cyberpunk Theme)
st.set_page_config(page_title="CyborgNet v2.0", layout="centered")

# CSS لتصميم السايبربانك
st.markdown("""
    <style>
    .main { background-color: #050505; color: #00ffcc; font-family: 'Courier New', monospace; }
    .stTextInput>div>div>input { background-color: #000000; color: #ff00ff !important; border: 1px solid #00ffcc !important; }
    .stButton>button { background-color: #00ffcc; color: black; width: 100%; border-radius: 5px; font-weight: bold; }
    .chat-box { border: 1px solid #00ffcc; padding: 10px; border-radius: 5px; background: rgba(0, 255, 204, 0.05); margin-bottom: 10px; }
    </style>
    """, unsafe_allow_html=True)

st.title("🦾 CYBORG_NET SYSTEM")
st.write("---")

# --- القسم الأول: نظام التشفير ---
st.subheader("🔐 ENCRYPTION MODULE")
secret_text = st.text_input("Enter message to encrypt:", key="encrypt_input")
if st.button("ENCRYPT NOW"):
    if secret_text:
        res = secret_text[::-1] + "X99"
        st.code(f"RESULT: {res}")

st.write("---")

# --- القسم الثاني: نظام الدردشة والذاكرة ---
st.subheader("💬 GLOBAL LOG_STREAM")

if "messages" not in st.session_state:
    st.session_state.messages = []

chat_input = st.text_input("Type your status update:", key="chat_input")
if st.button("POST TO NETWORK"):
    if chat_input:
        st.session_state.messages.append(chat_input)

# عرض السجل
for m in reversed(st.session_state.messages):
    st.markdown(f"<div class='chat-box'><b>[SYSTEM_LOG]:</b> {m}</div>", unsafe_allow_html=True)

st.sidebar.markdown("### STATUS: ONLINE")
st.sidebar.write("Logged in as: **MAX_CYBORG**")