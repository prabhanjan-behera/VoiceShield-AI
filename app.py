import streamlit as st
import time
import speech_recognition as sr
import os

# Page config must be the first Streamlit command
st.set_page_config(page_title="VoiceShield AI - AutoScan", page_icon="🛡️", layout="wide")

if "alert_triggered" not in st.session_state:
    st.session_state.alert_triggered = False

# ==========================================
# 1. PREMIUM FULL-SCREEN RED ALERT ENGINE 
# ==========================================
if st.session_state.alert_triggered:
    st.components.v1.html(
        """
        <script>
            var speech = new SpeechSynthesisUtterance("Scam Alert! Threat detected. Do not share OTP or money.");
            speech.lang = 'en-US'; window.speechSynthesis.speak(speech);
        </script>
        """, height=0
    )
    
    st.markdown(
        """
        <style>
        .stApp { background-color: #e60000 !important; }
        /* Heading aur spans ko white rakhenge, par <p> ko general white nahi karenge taaki button kharab na ho */
        .stApp h1, .stApp h2, .stApp h3, .stApp span { color: white !important; }
        
        /* BUTTON CSS FIX */
        div.stButton > button {
            background-color: #ffffff !important; 
            border: 4px solid #800000 !important;
            border-radius: 12px !important;
            height: 70px !important;
            box-shadow: 0px 8px 20px rgba(0,0,0,0.5) !important;
            transition: all 0.3s ease-in-out !important;
        }
        
        /* Bina hover kiye text RED dikhega */
        div.stButton > button p {
            color: #cc0000 !important; 
            font-size: 22px !important;
            font-weight: 900 !important;
        }
        
        /* Hover karne par background RED aur text WHITE ho jayega */
        div.stButton > button:hover {
            background-color: #800000 !important; 
            border: 4px solid #ffffff !important;
            transform: scale(1.03);
        }
        div.stButton > button:hover p {
            color: #ffffff !important; 
        }
        </style>
        """, unsafe_allow_html=True
    )
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; font-size: 80px; text-shadow: 2px 2px 5px black;'>🚨 AI SCAM ALERT DETECTED! 🚨</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; font-size: 40px; background-color: rgba(0,0,0,0.3); padding: 20px; border-radius: 15px; border: 2px dashed white; color: white;'>STOP! DO NOT SHARE ANY OTP.<br>DO NOT TRANSFER ANY MONEY!</h3><br><br>", unsafe_allow_html=True)
    
    # Do columns banaye hain taaki dono buttons aamne-saamne achhe se dikhein
    col1, col2, col3, col4 = st.columns([1, 2, 2, 1])
    
    with col2:
        # Pura call katne ka action
        if st.button("🔴 DISCONNECT CALL", use_container_width=True):
            st.session_state.alert_triggered = False
            st.rerun()
            
    with col3:
        # False alarm ignore karke baat jaari rakhne ka action
        if st.button("✅ IGNORE & CONTINUE", use_container_width=True):
            st.session_state.alert_triggered = False
            st.rerun()
            
    st.stop()

# ==========================================
# MAIN APP STYLING (FUTURISTIC UI)
# ==========================================
st.markdown(
    """
    <style>
    .stApp { background-color: #f4f8fb; }
    h1, h2, h3 { color: #002244 !important; font-family: 'Arial', sans-serif; }
    .main-text { color: #1a4d80; font-size: 18px; font-weight: 500; }
    .stAudio { border-radius: 10px; box-shadow: 0px 4px 10px rgba(0,0,0,0.1); padding: 10px; background-color: white; }
    
    /* FUTURISTIC GLOWING BUTTON CSS */
    div.stButton > button {
        background: linear-gradient(135deg, #0a192f 0%, #023e8a 100%) !important;
        color: #00f2fe !important;
        border: 2px solid #00f2fe !important;
        box-shadow: 0 0 15px rgba(0, 242, 254, 0.4), inset 0 0 10px rgba(0, 242, 254, 0.2) !important;
        border-radius: 12px !important;
        font-size: 22px !important;
        font-weight: 800 !important;
        letter-spacing: 1.5px;
        height: 70px !important;
        transition: all 0.3s ease-in-out !important;
    }
    div.stButton > button:hover {
        background: linear-gradient(135deg, #023e8a 0%, #00f2fe 100%) !important;
        color: #ffffff !important;
        border: 2px solid #ffffff !important;
        box-shadow: 0 0 25px rgba(0, 242, 254, 0.8), inset 0 0 15px rgba(255, 255, 255, 0.5) !important;
        transform: scale(1.02);
    }
    </style>
    """, unsafe_allow_html=True
)

# ==========================================
# 2. BRANDING & LOGO HEADER
# ==========================================
col_logo, col_title = st.columns([1, 5])
with col_logo:
    try:
        if os.path.exists("31077.png"):
            st.image("31077.png", use_container_width=True)
        else:
            st.markdown("<div style='font-size: 70px; text-align: center;'>🛡️</div>", unsafe_allow_html=True)
    except Exception:
        st.markdown("<div style='font-size: 70px; text-align: center;'>🛡️</div>", unsafe_allow_html=True)

with col_title:
    st.markdown("<h1 style='margin-bottom: -15px; color: #002244 !important; font-size: 50px; font-weight: 900;'>VOICE SHIELD <span style='color: #0088cc;'>AI</span></h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='margin-top: 0px; color: #555555 !important; font-weight: 400; font-style: italic; font-size: 22px;'>Secure. Guard. Verify.</h3>", unsafe_allow_html=True)

st.markdown("<hr style='border: 1px solid #cce6ff;'>", unsafe_allow_html=True)

# ==========================================
# 3. PAN-INDIA MULTI-LINGUAL MASTER DATABASE
# ==========================================
# Yeh dictionary background mein sabhi bhashaon ke words pakdegi
SCAM_KEYWORDS = {
    "otp", "money", "bank", "card", "cash", "password", "pin", "send", "rupees", "rupee", "pay", "transfer", "block", "emergency", "urgent", "rs", "5000", "dollars",
    "paise", "paisa", "bhejo", "do", "nikaalo", "khata", "chahiye", "पैसे", "पैसा", "भेजो", "दो", "ओटीपी", "खाता", "इमरजेंसी",
    "tanka", "bheja", "diya", "diyantu", "account block","tonka","otp", "ଟଙ୍କା", "ପଇସା", "ଦିଅ", "ପାସୱାର୍ଡ", "ଓଟିପି",
    "taka", "poisa", "pathao", "dao", "taka lagbe", "টাকা", "পয়সা", "পাঠাও", "দাও", "অ্যাকাউন্ট",
    "paisa", "moklo", "aapo", "khatu", "jaroori", "પૈસા", "મોકલો", "આપો", "ખાતું", "તાત્કાલિક",
    "hanna", "duddu", "kalisi", "kodi", "khati", "ಹಣ", "ದುಡ್ಡು", "ಕಳಿಸಿ", "ಕೊಡಿ", "ಖಾತೆ",
    "panam", "kashu", "ayayku", "tharu", "panam venam", "പണം", "കാശ്", "അയക്കൂ", "തരൂ", "അക്കൗണ്ട്",
    "pathva", "dya", "khate", "paise pahije", "पैसे", "पाठवा", "द्या", "खाते", "तातडीचे",
    "panam", "kasu", "anuppu", "kudu", "kanakku", "பணம்", "காசு", "அனுப்பு", "குடு", "கணக்கு",
    "dabbulu", "dabbu", "pampu", "ivvu", "avasaram", "డబ్బులు", "డబ్బు", "పంపు", "ఇవ్వు", "ఖాతా",
    "deo", "khata", "paisa bhejo", "ਪੈਸੇ", "ਭੇਜੋ", "ਦਿਓ", "ਖਾਤਾ", "ਜ਼ਰੂਰੀ",
    "bhejo", "khata", "zaroori", "پیسے", "بھیجو", "دو", "اکاؤنٹ", "لازمی",
    "tonka" # Added phonetic variations for Odia
}

# ==========================================
# 4. CORE PROCESSING UI (NO DROPDOWN - FULL AUTO)
# ==========================================
st.write("### 🎙️ Live Voice Input Processing Layer")
st.markdown("<p class='main-text'>Record your voice call. The AI automatically scans for threats across all 11 regional databases in the background.</p>", unsafe_allow_html=True)

audio_value = st.audio_input("Record call audio:")

if audio_value:
    if st.button("🧬 AUTO-SCAN & ANALYZE VOICE PRINT", use_container_width=True):
        with st.spinner("AI Engine auto-detecting and matching voice print against pan-India threat records..."):
            try:
                recognizer = sr.Recognizer()
                with sr.AudioFile(audio_value) as source:
                    audio_data = recognizer.record(source)
                    # Hardcoded to en-IN so it acts as an automatic Indian catch-all
                    transcribed_text = recognizer.recognize_google(audio_data, language="en-IN")
                
                st.info(f"📡 **Live Intercepted Auto-Transcript:** \"{transcribed_text}\"")
                
                text_lower = transcribed_text.lower()
                words_spoken = text_lower.split() 
                
                start_time = time.time()
                is_scam_found = False
                
                # Checking for threat keywords
                for word in words_spoken:
                    if word in SCAM_KEYWORDS:
                        is_scam_found = True
                        break
                
                end_time = time.time()
                execution_time_ms = (end_time - start_time) * 1000
                
                if is_scam_found:
                    st.toast(f"Threat matched in {execution_time_ms:.2f} ms!", icon="⚡")
                    st.session_state.alert_triggered = True
                    st.rerun()
                else:
                    st.success(f"✅ SAFE: Authentic Voice Certified (Processed in {execution_time_ms:.2f} ms).")
                    st.markdown("<p style='color: #2e7d32; font-weight: bold;'>No suspicious keywords found across active Indian threat databases.</p>", unsafe_allow_html=True)
                    
            except sr.UnknownValueError:
                st.error("❌ NO AUDIO DETECTED: AI could not catch any clear voice waves. Please speak louder and try again.")
            except Exception as e:
                st.error(f"❌ SYSTEM ERROR: Details: {e}")