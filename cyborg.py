import streamlit as st
from datetime import datetime
import time

# --- 1. إعدادات الهوية البصرية (Cyberpunk Theme) ---
st.set_page_config(page_title="CyborgNet v1.0", page_icon="🦾", layout="centered")

# لمسة الـ CSS لتحويل المتصفح إلى شاشة Cyborg
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Share+Tech+Mono&display=swap');
    
    html, body, [class*="css"]  {
        background-color: #050505;
        color: #00ffcc;
        font-family: 'Share Tech Mono', monospace;
    }
    
    .stTextInput > div > div > input {
        background-color: #000000;
        color: #ff00ff !important;
        border: 1px solid #00ffcc !important;
        box-shadow: 0 0 10px #00ffcc;
    }

    .chat-box {
        border: 1px solid #333;
        padding: 15px;
        border-radius: 10px;
        background: rgba(0, 255, 204, 0.05);
        margin-bottom: 15px;
        border-left: 5px solid #ff00ff;
    }

    .system-msg {
        color: #ff00ff;
        font-size: 0.8em;
        text-transform: uppercase;
        letter-spacing: 2px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. منطق البيانات (The Core) ---
if "messages" not in st.session_state:
    st.session_state.messages = []
    # رسالة ترحيب من النظام
    st.session_state.messages.append({
        "role": "system",
        "user": "SYSTEM",
        "content": "Cyborg Terminal Activated. Secure Line Established.",
        "time": datetime.now().strftime("%H:%M")
    })

# --- 3. واجهة المستخدم (The Interface) ---
st.markdown("<h1 style='text-align: center; color: #00ffcc; text-shadow: 0 0 20px #00ffcc;'>⚡ CYBORG_NET TERMINAL</h1>", unsafe_allow_html=True)
st.write(f"<p style='text-align: center;' class='system-msg'>Status: Online | User: Max_Cyborg</p >", unsafe_allow_html=True)

# عرض الرسائل بأسلوب "سايبر"
for msg in st.session_state.messages:
    with st.container():
        if msg["role"] == "system":
            st.markdown(f"<p class='system-msg' style='text-align:center;'>--- {msg['content']} ---</p >", unsafe_allow_html=True)
        else:
            st.markdown(f"""
                <div class="chat-box">
                    <small style="color: #444;">[{msg['time']}]</small> 
                    <b style="color: #ff00ff;">{msg['user']} >></b> {msg['content']}
                </div>
                """, unsafe_allow_html=True)

# --- 4. التحكم والإدخال ---
input_text = st.chat_input("أدخل بياناتك هنا...")

if input_text:
    # إضافة رسالة المستخدم
    new_msg = {
        "role": "user",
        "user": "MAX_CYBORG",
        "content": input_text,
        "time": datetime.now().strftime("%H:%M")
    }
    st.session_state.messages.append(new_msg)
    
    # "حركة حلوة": رد تلقائي من النظام (بوت صغير)
    if "طبخة" in input_text or "اكل" in input_text:
        st.session_state.messages.append({
            "role": "system",
            "user": "AI",
            "content": "تحذير: تم اكتشاف مكونات طبخة غريبة في الذاكرة!",
            "time": datetime.now().strftime("%H:%M")
        })
    
    st.rerun()

# أزرار تحكم إضافية في الجانب (Sidebar)
with st.sidebar:
    st.header("⚙️ العدادات")
    if st.button("مسح السجل (Purge)"):
        st.session_state.messages = []
        st.rerun()
    st.write("---")
    st.write("Cyborg Device: MSI Laptop")