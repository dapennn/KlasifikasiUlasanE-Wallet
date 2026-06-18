import streamlit as st
import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(
    page_title="Sistem Analisis Sentimen E-Wallet",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown("""
<style>
/* ============================================
   FONT & RESET
   ============================================ */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

html, body, [class*="css"] {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
}

/* ============================================
   BACKGROUND
   ============================================ */
.stApp {
    background: #f1f5f9;
}

.stApp > div:first-child {
    background:
        radial-gradient(ellipse at 0% 0%, rgba(37,99,235,0.06) 0%, transparent 50%),
        radial-gradient(ellipse at 100% 100%, rgba(124,58,237,0.04) 0%, transparent 50%),
        #f1f5f9;
}

/* ============================================
   MAIN CONTAINER
   ============================================ */
.block-container {
    padding: 0.6rem 1.5rem 1.5rem 1.5rem !important;
    max-width: 1400px !important;
}

/* ============================================
   SIDEBAR - Premium Dark
   ============================================ */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0f172a 0%, #1e293b 100%);
    border-right: 1px solid rgba(255,255,255,0.06);
    padding-top: 0.5rem;
}

[data-testid="stSidebar"] * {
    color: #e2e8f0 !important;
}

[data-testid="stSidebar"] .st-emotion-cache-1wivap2 {
    padding: 0 0.8rem;
}

[data-testid="stSidebar"] .st-emotion-cache-1v0mbdj {
    padding: 0.2rem 0.5rem;
}

/* Sidebar Brand */
.sidebar-brand {
    padding: 0.3rem 0 0.8rem 0;
    border-bottom: 1px solid rgba(255,255,255,0.06);
    margin-bottom: 0.8rem;
}
.sidebar-brand .brand-icon {
    font-size: 1.6rem;
    margin-right: 0.5rem;
}
.sidebar-brand .brand-title {
    font-size: 1.1rem;
    font-weight: 800;
    color: #ffffff !important;
    letter-spacing: -0.02em;
}
.sidebar-brand .brand-sub {
    font-size: 0.65rem;
    color: rgba(255,255,255,0.4) !important;
    margin-top: -2px;
    letter-spacing: 0.3px;
}

/* Sidebar Menu */
[data-testid="stSidebar"] .st-emotion-cache-1p1rxkq {
    border-radius: 10px;
    padding: 0.5rem 0.8rem;
    transition: all 0.2s ease;
    background: transparent;
    font-weight: 500;
    font-size: 0.85rem;
    margin-bottom: 2px;
}

[data-testid="stSidebar"] .st-emotion-cache-1p1rxkq:hover {
    background: rgba(255,255,255,0.06);
}

[data-testid="stSidebar"] .st-emotion-cache-1p1rxkq[aria-checked="true"] {
    background: linear-gradient(90deg, rgba(37,99,235,0.25), rgba(37,99,235,0.05));
    border-left: 3px solid #3b82f6;
    color: #60a5fa !important;
}

/* Sidebar Divider */
[data-testid="stSidebar"] hr {
    border-color: rgba(255,255,255,0.06) !important;
    margin: 0.4rem 0 !important;
}

/* ============================================
   HERO BANNER
   ============================================ */
.hero-banner {
    background: linear-gradient(135deg, #ffffff 0%, #f8fafc 100%);
    border-radius: 16px;
    padding: 1rem 1.8rem;
    margin-bottom: 0.8rem;
    border: 1px solid rgba(226,232,240,0.6);
    box-shadow: 0 4px 20px rgba(0,0,0,0.04);
    position: relative;
    overflow: hidden;
}
.hero-banner::before {
    content: '';
    position: absolute;
    top: -60%;
    right: -5%;
    width: 250px;
    height: 250px;
    background: radial-gradient(circle, rgba(37,99,235,0.06), transparent 70%);
    border-radius: 50%;
}
.hero-banner::after {
    content: '';
    position: absolute;
    bottom: -50%;
    left: -5%;
    width: 200px;
    height: 200px;
    background: radial-gradient(circle, rgba(124,58,237,0.04), transparent 70%);
    border-radius: 50%;
}
.hero-banner > * {
    position: relative;
    z-index: 1;
}
.hero-banner .hero-badge {
    display: inline-block;
    background: linear-gradient(90deg, rgba(37,99,235,0.12), rgba(124,58,237,0.08));
    color: #475569;
    font-size: 0.6rem;
    font-weight: 600;
    padding: 0.1rem 0.7rem;
    border-radius: 20px;
    letter-spacing: 0.5px;
    text-transform: uppercase;
    margin-bottom: 0.1rem;
}
.hero-banner h1 {
    font-size: 1.5rem;
    font-weight: 800;
    color: #0f172a;
    margin: 0;
    letter-spacing: -0.02em;
}
.hero-banner h1 .highlight {
    background: linear-gradient(90deg, #2563eb, #7c3aed);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
.hero-banner p {
    font-size: 0.85rem;
    color: #64748b;
    margin: 0.1rem 0 0 0;
}

/* ============================================
   METRIC CARDS
   ============================================ */
[data-testid="stMetric"] {
    background: #ffffff !important;
    border-radius: 12px !important;
    padding: 0.7rem 0.8rem !important;
    border: 1px solid rgba(226,232,240,0.6) !important;
    box-shadow: 0 2px 8px rgba(0,0,0,0.03) !important;
    transition: all 0.2s ease !important;
}
[data-testid="stMetric"]:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 24px rgba(0,0,0,0.06) !important;
}
[data-testid="stMetric"] label {
    font-size: 0.65rem !important;
    font-weight: 600 !important;
    color: #64748b !important;
    text-transform: uppercase !important;
    letter-spacing: 0.3px !important;
}
[data-testid="stMetric"] div[data-testid="stMetricValue"] {
    font-size: 1.3rem !important;
    font-weight: 700 !important;
    color: #0f172a !important;
}
[data-testid="stMetric"] div[data-testid="stMetricDelta"] {
    font-size: 0.65rem !important;
}

/* ============================================
   BUTTONS - Modern
   ============================================ */
.stButton > button, .stDownloadButton > button {
    border-radius: 10px !important;
    border: none !important;
    padding: 0.45rem 1.2rem !important;
    font-weight: 600 !important;
    font-size: 0.8rem !important;
    background: linear-gradient(135deg, #2563eb, #1d4ed8) !important;
    color: white !important;
    box-shadow: 0 4px 14px rgba(37,99,235,0.25) !important;
    transition: all 0.2s ease !important;
    letter-spacing: 0.2px !important;
    cursor: pointer !important;
}
.stButton > button:hover, .stDownloadButton > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 28px rgba(37,99,235,0.35) !important;
    background: linear-gradient(135deg, #3b82f6, #2563eb) !important;
}
.stButton > button:active, .stDownloadButton > button:active {
    transform: scale(0.97) !important;
}

.stButton > button[kind="secondary"] {
    background: #ffffff !important;
    color: #1e293b !important;
    box-shadow: 0 2px 8px rgba(0,0,0,0.06) !important;
    border: 1px solid #e2e8f0 !important;
}
.stButton > button[kind="secondary"]:hover {
    background: #f8fafc !important;
    box-shadow: 0 4px 16px rgba(0,0,0,0.08) !important;
}

/* Primary Button */
.primary-btn {
    background: linear-gradient(135deg, #2563eb, #1d4ed8) !important;
    color: white !important;
}
.primary-btn:hover {
    background: linear-gradient(135deg, #3b82f6, #2563eb) !important;
}

/* ============================================
   DATA FRAME
   ============================================ */
[data-testid="stDataFrame"] {
    border-radius: 12px !important;
    overflow: hidden !important;
    border: 1px solid #e2e8f0 !important;
    box-shadow: 0 2px 8px rgba(0,0,0,0.03) !important;
}
[data-testid="stDataFrame"] table {
    font-size: 0.75rem !important;
}
[data-testid="stDataFrame"] thead tr th {
    background: #f8fafc !important;
    font-weight: 600 !important;
    color: #334155 !important;
    border-bottom: 2px solid #e2e8f0 !important;
    padding: 0.4rem 0.6rem !important;
}
[data-testid="stDataFrame"] tbody tr td {
    padding: 0.3rem 0.6rem !important;
}
[data-testid="stDataFrame"] tbody tr:hover {
    background: #f8fafc !important;
}

/* ============================================
   TABS - Modern
   ============================================ */
.stTabs [data-baseweb="tab-list"] {
    gap: 0.2rem !important;
    background: #ffffff !important;
    border-radius: 12px !important;
    padding: 0.2rem !important;
    border: 1px solid #e2e8f0 !important;
    box-shadow: 0 2px 8px rgba(0,0,0,0.02) !important;
}
.stTabs [data-baseweb="tab"] {
    border-radius: 10px !important;
    padding: 0.4rem 1rem !important;
    font-size: 0.75rem !important;
    font-weight: 500 !important;
    color: #64748b !important;
    background: transparent !important;
    border: none !important;
    transition: all 0.2s ease !important;
}
.stTabs [data-baseweb="tab"]:hover {
    background: #f1f5f9 !important;
    color: #1e293b !important;
}
.stTabs [aria-selected="true"] {
    background: #f1f5f9 !important;
    color: #2563eb !important;
    font-weight: 600 !important;
}

/* ============================================
   DIVIDER
   ============================================ */
hr {
    margin: 0.4rem 0 !important;
    border: none !important;
    border-top: 1px solid #e2e8f0 !important;
}

/* ============================================
   EXPANDER
   ============================================ */
[data-testid="stExpander"] {
    border-radius: 12px !important;
    border: 1px solid #e2e8f0 !important;
    background: #ffffff !important;
}
[data-testid="stExpander"] summary {
    font-weight: 600 !important;
    font-size: 0.8rem !important;
    color: #1e293b !important;
}

/* ============================================
   ALERTS / INFO BOXES
   ============================================ */
.stAlert {
    border-radius: 12px !important;
    padding: 0.4rem 0.8rem !important;
    font-size: 0.8rem !important;
    border: 1px solid #e2e8f0 !important;
}
.stAlert[data-baseweb="notification"] {
    background: #ffffff !important;
    border-left: 4px solid #3b82f6 !important;
}

/* ============================================
   TEXT AREA / INPUT
   ============================================ */
.stTextArea textarea {
    border-radius: 12px !important;
    border: 1px solid #e2e8f0 !important;
    font-size: 0.8rem !important;
    transition: all 0.2s ease !important;
    background: #ffffff !important;
}
.stTextArea textarea:focus {
    border-color: #3b82f6 !important;
    box-shadow: 0 0 0 3px rgba(37,99,235,0.08) !important;
}

/* ============================================
   FILE UPLOADER
   ============================================ */
[data-testid="stFileUploader"] {
    border-radius: 12px !important;
    border: 2px dashed #e2e8f0 !important;
    padding: 0.5rem !important;
    background: #ffffff !important;
    transition: all 0.2s ease !important;
}
[data-testid="stFileUploader"]:hover {
    border-color: #3b82f6 !important;
    background: #f8fafc !important;
}

/* ============================================
   SELECTBOX
   ============================================ */
[data-baseweb="select"] > div {
    border-radius: 10px !important;
    border: 1px solid #e2e8f0 !important;
}
[data-baseweb="select"] > div:focus-within {
    border-color: #3b82f6 !important;
    box-shadow: 0 0 0 3px rgba(37,99,235,0.08) !important;
}

/* ============================================
   RESPONSIVE
   ============================================ */
@media (max-width: 768px) {
    .hero-banner h1 { font-size: 1.1rem; }
    .block-container { padding: 0.5rem 0.8rem !important; }
}

/* ============================================
   SCROLLBAR
   ============================================ */
::-webkit-scrollbar {
    width: 5px;
    height: 5px;
}
::-webkit-scrollbar-track {
    background: transparent;
}
::-webkit-scrollbar-thumb {
    background: #cbd5e1;
    border-radius: 10px;
}
::-webkit-scrollbar-thumb:hover {
    background: #94a3b8;
}

/* ============================================
   MISC
   ============================================ */
.st-emotion-cache-1v0mbdj {
    padding: 0.2rem 0.5rem !important;
}
.element-container {
    margin-bottom: 0.1rem !important;
}
.st-emotion-cache-1wivap2 {
    min-height: auto !important;
}
</style>
""", unsafe_allow_html=True)

try:
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.naive_bayes import MultinomialNB
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import (
        classification_report, confusion_matrix, accuracy_score, 
        precision_score, recall_score, f1_score
    )
    SKLEARN_OK = True
except ImportError:
    SKLEARN_OK = False

@st.cache_resource
def load_sastrawi():
    try:
        from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
        return StemmerFactory().create_stemmer(), True
    except ImportError:
        return None, False

_stemmer, SASTRAWI_OK = load_sastrawi()

# KAMUS SLANG & STOPWORDS
KAMUS_SLANG = {
    "gak":"tidak","ga":"tidak","nggak":"tidak","ndak":"tidak","ngga":"tidak",
    "g":"tidak","tdk":"tidak","tak":"tidak","gk":"tidak",
    "tolo":"tolol","tolol":"bodoh","goblok":"bodoh","bego":"bodoh","idiot":"bodoh",
    "anjing":"kasar","sial":"buruk","bangke":"buruk","asu":"kasar","kontol":"kasar",
    "memek":"kasar","jancok":"kasar","cuk":"kasar","dasar":"sangat","nganu":"tidak jelas",
    "mantul":"mantap","bgtt":"banget","bgt":"banget","bgd":"banget",
    "keren":"bagus","cakep":"bagus","kece":"bagus","gacor":"bagus","jos":"bagus",
    "wow":"bagus","gila":"luar biasa",
    "apk":"aplikasi","app":"aplikasi","mksh":"terima kasih","tks":"terima kasih",
    "thx":"terima kasih","tx":"terima kasih","lemot":"lambat","eror":"error","error":"error",
    "oke":"baik","ok":"baik","bgs":"bagus","jls":"jelas",
    "kl":"kalau","sm":"sama","tp":"tapi","krn":"karena","yg":"yang","dg":"dengan",
    "utk":"untuk","dpt":"dapat","sdh":"sudah","blm":"belum","hrs":"harus",
    "bs":"bisa","gampang":"mudah","cepet":"cepat","lelet":"lambat","susah":"sulit",
}

STOPWORDS_ID = {
    "yang","dan","di","ke","dari","ini","itu","dengan","untuk","pada","adalah",
    "tidak","dalam","ada","juga","sudah","bisa","akan","karena","saya","kami",
    "kita","mereka","nya","pun","atau","tapi","kalau","jika","namun","lagi",
    "saja","ya","oh","iya","buat","banget","sangat","sekali","udah","aja",
}

LEXICON_POS = {
    "bagus","mantap","cepat","mudah","puas","suka","baik","ramah","cepet",
    "lengkap","stabil","lancar","murah","berguna","mantul","helpful","keren",
    "rekomendasi","ok","oke","top","hemat","nyaman","bagusnya","wow","jos",
    "gacor","kece","cakep","senang","terbaik","recommended","powerful","efektif",
    "efisien","terbantu","bermanfaat","memuaskan","luar biasa","istimewa","hebat",
    "sempurna","akurat","tepat","inovatif","modern","canggih","praktis","simpel",
    "simple","ringan","responsif","handal","andal","terpercaya","best","good","great",
    "amazing","awesome","excellent","perfect","love","like","terima kasih","makasih"
}

LEXICON_NEG = {
    "jelek","lambat","lemot","error","gagal","susah","ribet","eror",
    "buruk","parah","kecewa","crash","bug","timeout","loading","cacat",
    "hang","bermasalah","mati","macet","ngelag","ngadat","rusak","payah",
    "tolol","bodoh","goblok","bego","idiot","kasar","sial","bangke","nganu",
    "mengecewakan","kesal","marah","benci","dongo","pusing","repot",
    "berat","lamban","ngaco","ambyar","kacau","berantakan","lemah",
    "rapuh","tidak stabil","sering error","force close","not responding",
    "freeze","lag","stuck","blank","hitam","garing","bad","poor","terrible",
    "worst","useless","waste","hate","disappointed","frustasi","stress"
}

NEGATORS = {"tidak", "gak", "ga", "nggak", "bukan", "tak", "jangan", "belum", "kurang", "tidak ada", "tanpa"}
INTENSIFIERS = {"sangat", "amat", "benar", "sekali", "banget", "bgtt", "bgt", "bgd", "terlalu", "paling", "begitu", "begini", "begono"}

def bersihkan_teks(teks) -> str:
    teks = str(teks)
    teks = re.sub(r"http\S+|www\S+|https\S+", " ", teks)
    teks = re.sub(r"@\w+|#\w+", " ", teks)
    teks = re.sub(r"[^\w\s]", " ", teks)
    teks = re.sub(r"\d+", " ", teks)
    return re.sub(r"\s+", " ", teks).strip()

def case_folding(teks: str) -> str:
    return teks.lower()

def normalisasi_slang(teks: str) -> str:
    kata_kata = teks.split()
    hasil = []
    for k in kata_kata:
        if k in KAMUS_SLANG:
            hasil.append(KAMUS_SLANG[k])
        else:
            hasil.append(k)
    return " ".join(hasil)

def tokenizing(teks: str) -> list:
    return teks.split()

def hapus_stopword(tokens: list) -> list:
    return [w for w in tokens if w not in STOPWORDS_ID and len(w) > 1]

def stemming(tokens: list) -> str:
    teks_gabung = " ".join(tokens)
    if SASTRAWI_OK and _stemmer:
        return _stemmer.stem(teks_gabung)
    return teks_gabung

def praproses(teks: str) -> str:
    t1 = bersihkan_teks(teks)
    t2 = case_folding(t1)
    t3 = normalisasi_slang(t2)
    t4 = tokenizing(t3)
    t5 = hapus_stopword(t4)
    t6 = stemming(t5)
    return t6

def praproses_lengkap(teks: str) -> dict:
    t1 = bersihkan_teks(teks)
    t2 = case_folding(t1)
    t3 = normalisasi_slang(t2)
    t4 = tokenizing(t3)
    t5 = hapus_stopword(t4)
    t6 = stemming(t5)
    return {
        "teks_asli": teks,
        "1_Cleaning": t1,
        "2_Case_Folding": t2,
        "3_Normalisasi_Slang": t3,
        "4_Tokenizing": str(t4),
        "5_Stopword_Removal": str(t5),
        "6_Stemming": t6
    }

def label_lexicon(teks: str) -> str:
    teks_bersih = praproses(teks)
    tokens = teks_bersih.split()
    
    if not tokens:
        return "Netral"
    
    teks_lower = teks.lower()
    kata_kasar = ["tolol", "goblok", "bego", "idiot", "anjing", "sial", "bangke", 
                  "asu", "kontol", "memek", "jancok", "cuk", "dongo", "nganu"]
    
    for kasar in kata_kasar:
        if kasar in teks_lower:
            negasi = ["tidak", "gak", "ga", "nggak", "bukan"]
            posisi = teks_lower.find(kasar)
            if posisi > 0:
                teks_sebelum = teks_lower[max(0, posisi-20):posisi]
                if any(neg in teks_sebelum for neg in negasi):
                    continue
            return "Negatif"
    
    kata_positif_kuat = ["terbaik", "sempurna", "recommended", "wow", "keren", "mantap", "best", "great", "amazing"]
    for positif in kata_positif_kuat:
        if positif in teks_lower:
            return "Positif"
    
    skor = 0
    for i, tok in enumerate(tokens):
        prev = tokens[i - 1] if i > 0 else ""
        intensifier = 2 if prev in INTENSIFIERS else 1
        is_negated = prev in NEGATORS
        
        if tok in LEXICON_POS:
            if is_negated:
                skor -= 1 * intensifier
            else:
                skor += 1 * intensifier
        elif tok in LEXICON_NEG:
            if is_negated:
                skor += 1 * intensifier
            else:
                skor -= 1 * intensifier
    
    if len(tokens) > 0:
        skor = skor / len(tokens) * 10
    
    if skor > 0.3:
        return "Positif"
    elif skor < -0.3:
        return "Negatif"
    return "Netral"

def label_lexicon_sederhana(teks: str) -> str:
    teks_bersih = case_folding(bersihkan_teks(teks))
    teks_normal = normalisasi_slang(teks_bersih)
    tokens = teks_normal.split()
    
    kata_positif = [
        "bagus", "mantap", "baik", "cepat", "mudah", "puas", "suka", 
        "keren", "hebat", "top", "ok", "oke", "mantul", "wow", "jos",
        "lengkap", "stabil", "lancar", "murah", "terbaik", "senang",
        "aman", "bantu", "berguna", "cepet", "gampang"
    ]
    
    kata_negatif = [
        "jelek", "lambat", "error", "eror", "gagal", "susah", "ribet", "buruk", 
        "parah", "kecewa", "tolol", "goblok", "bego", "idiot", "sial", "payah",
        "lemot", "crash", "bug", "macet", "rusak", "sampah", "penipu", 
        "rugi", "hilang", "lelet", "ngelag", "nyangkut", "kasar"
    ]
    
    skor = 0
    for kata in tokens:
        if kata in kata_positif:
            skor += 1
        elif kata in kata_negatif:
            skor -= 1
            
    if skor > 0:
        return "Positif"
    elif skor < 0:
        return "Negatif"
    return "Netral"

def st_get(key, default=None):
    return st.session_state.get(key, default)

def hero(title, subtitle, badge=""):
    badge_html = f'<span class="hero-badge">{badge}</span>' if badge else ''
    st.markdown(f"""
    <div class="hero-banner">
        {badge_html}
        <h1>{title}</h1>
        <p>{subtitle}</p>
    </div>
    """, unsafe_allow_html=True)

# Inisialisasi session state
for k in ["df_raw","df_proses","df_train","df_test","X_train","X_test","y_train","y_test","tfidf","nb_model","y_pred","kol_teks","df_with_predictions"]:
    if k not in st.session_state:
        st.session_state[k] = None

# ==================== SIDEBAR ====================
with st.sidebar:
    st.markdown("""
    <div class="sidebar-brand">
        <div style="display:flex;align-items:center;">
            <span class="brand-icon">📊</span>
            <span class="brand-title">Sentiment Analysis</span>
        </div>
        <div class="brand-sub">Sistem Klasifikasi E-Wallet</div>
    </div>
    """, unsafe_allow_html=True)
    
    menu = st.radio(
        "NAVIGASI",
        ["🏠 Beranda", "📁 Upload Data", "🔧 Preprocessing", "⚙️ Training", "🔍 Uji Klasifikasi", "📊 Laporan"],
        label_visibility="collapsed"
    )
    
    st.divider()
    
    if menu == "🔍 Uji Klasifikasi":
        metode_uji = st.radio("Metode Klasifikasi", ["Lexicon", "Naïve Bayes"], index=0)
    else:
        metode_uji = "Lexicon"

# ==================== MENU BERANDA ====================
if menu == "🏠 Beranda":
    hero("Sistem Klasifikasi Sentimen E-Wallet", "Analisis sentimen otomatis untuk GoPay, ShopeePay, dan DANA", "DATA MINING")
    
    c1, c2, c3 = st.columns(3)
    with c1:
        st.metric("🎯 Target Platform", "3", "GoPay • ShopeePay • DANA")
    with c2:
        st.metric("🤖 Metode", "Naïve Bayes", "Multinomial Classifier")
    with c3:
        st.metric("🏷️ Kategori Sentimen", "3", "Positif • Negatif • Netral")
    
    st.info("💡 **Alur Penggunaan:** Upload Data → Preprocessing → Training → Uji Klasifikasi")

# ==================== MENU UPLOAD DATA ====================
elif menu == "📁 Upload Data":
    hero("Upload Dataset", "Upload file CSV atau Excel untuk diproses", "📂")
    
    uploaded = st.file_uploader("Pilih file dataset", type=["csv", "xlsx", "xls"])
    if uploaded:
        try:
            df = pd.read_csv(uploaded) if uploaded.name.endswith(".csv") else pd.read_excel(uploaded)
            st.session_state.df_raw = df
            st.success(f"✅ {len(df)} baris berhasil dimuat")
            
            st.write("**📋 Preview Data (100 baris pertama)**")
            st.dataframe(df.head(100), use_container_width=True, height=280)
            
            c1, c2, c3 = st.columns(3)
            with c1:
                st.metric("Jumlah Baris", f"{len(df):,}")
            with c2:
                st.metric("Jumlah Kolom", f"{df.shape[1]}")
            with c3:
                missing = df.isna().sum().sum()
                st.metric("Missing Value", f"{int(missing)}")
            
        except Exception as e:
            st.error(f"Gagal membaca file: {e}")
    else:
        st.info("💡 Silakan upload file CSV atau Excel untuk memulai")

# ==================== MENU PREPROCESSING ====================
elif menu == "🔧 Preprocessing":
    hero("Preprocessing Data", "Bersihkan dan siapkan data untuk proses training", "🧹")
    
    df = st_get("df_raw")
    if df is None:
        st.warning("⚠️ Belum ada data. Upload file CSV atau Excel terlebih dahulu di menu Upload Data.")
    else:
        if st.session_state.df_proses is not None:
            st.success("✅ Data berhasil diproses")
            
            c1, c2 = st.columns([4, 1])
            with c2:
                if st.button("🔄 Proses Ulang", use_container_width=True):
                    st.session_state.df_proses = None
                    st.session_state.df_train = None
                    st.session_state.df_test = None
                    st.session_state.X_train = None
                    st.session_state.X_test = None
                    st.session_state.y_train = None
                    st.session_state.y_test = None
                    st.rerun()
            
            df_proses = st.session_state.df_proses
            
            c_m1, c_m2, c_m3, c_m4 = st.columns(4)
            total_data = len(df_proses)
            jml_positif = len(df_proses[df_proses['label'] == 'Positif'])
            jml_negatif = len(df_proses[df_proses['label'] == 'Negatif'])
            jml_netral = len(df_proses[df_proses['label'] == 'Netral'])
            
            with c_m1:
                st.metric("Total Ulasan", f"{total_data:,}")
            with c_m2:
                st.metric("🟢 Positif", f"{jml_positif:,}")
            with c_m3:
                st.metric("🔴 Negatif", f"{jml_negatif:,}")
            with c_m4:
                st.metric("⚪ Netral", f"{jml_netral:,}")
            
            st.divider()
            
            st.subheader("📊 Hasil Preprocessing")
            kolom_tampil = ["aplikasi", "teks_cleaning", "teks_case_folding", 
                           "teks_normalisasi", "teks_tokenizing", "teks_stopword", "teks_stemming", "label"]
            st.dataframe(df_proses[kolom_tampil].head(10), use_container_width=True, height=240)
            
        else:
            kolom_teks = None
            for col in df.columns:
                if col.lower() in ['ulasan', 'review', 'text', 'komentar', 'content']:
                    kolom_teks = col
                    break
            if kolom_teks is None:
                kolom_teks = df.columns[0]
            
            kolom_app = None
            for col in df.columns:
                if col.lower() in ['aplikasi', 'app', 'platform', 'nama_aplikasi']:
                    kolom_app = col
                    break
            
            c1, c2, c3 = st.columns([1, 1, 1.5])
            with c1:
                st.info(f"📝 Kolom teks: **{kolom_teks}**")
            with c2:
                if kolom_app:
                    st.success(f"✅ Kolom aplikasi: **{kolom_app}**")
                else:
                    st.warning("⚠️ Kolom aplikasi tidak ditemukan")
            with c3:
                if st.button("🚀 Proses Preprocessing", use_container_width=True, type="primary"):
                    with st.spinner("Memproses data..."):
                        df_proses = df.copy()
                        teks_asli = df_proses[kolom_teks].astype(str).fillna("")
                        
                        hasil_preprocessing = []
                        progress_bar = st.progress(0)
                        for i, teks in enumerate(teks_asli):
                            hasil = praproses_lengkap(teks)
                            hasil_preprocessing.append(hasil)
                            progress_bar.progress((i + 1) / len(teks_asli))
                        progress_bar.empty()
                        
                        df_prepro = pd.DataFrame(hasil_preprocessing)
                        df_proses["teks_cleaning"] = df_prepro["1_Cleaning"]
                        df_proses["teks_case_folding"] = df_prepro["2_Case_Folding"]
                        df_proses["teks_normalisasi"] = df_prepro["3_Normalisasi_Slang"]
                        df_proses["teks_tokenizing"] = df_prepro["4_Tokenizing"]
                        df_proses["teks_stopword"] = df_prepro["5_Stopword_Removal"]
                        df_proses["teks_stemming"] = df_prepro["6_Stemming"]
                        
                        df_proses["label"] = teks_asli.apply(label_lexicon)
                        df_proses["aplikasi"] = df_proses[kolom_app] if kolom_app else "Umum"
                        
                        df_train, df_test = train_test_split(df_proses, test_size=0.2, random_state=42, stratify=df_proses["label"])
                        
                        st.session_state.update({
                            "df_proses": df_proses,
                            "df_train": df_train,
                            "df_test": df_test,
                            "X_train": df_train["teks_stemming"],
                            "X_test": df_test["teks_stemming"],
                            "y_train": df_train["label"],
                            "y_test": df_test["label"],
                            "kolom_teks_pilihan": kolom_teks
                        })
                        
                        st.session_state.nb_model = None
                        st.session_state.tfidf = None
                        
                        st.rerun()

# ==================== MENU TRAINING ====================
elif menu == "⚙️ Training":
    hero("Training Model", "Latih model Naïve Bayes dengan data yang sudah dipreprocessing", "⚡")
    
    if st.session_state.df_proses is None:
        st.warning("⚠️ Silakan lakukan preprocessing data di menu 'Preprocessing' terlebih dahulu.")
    else:
        model_loaded = st.session_state.nb_model is not None
        
        if model_loaded:
            st.success("✅ Model berhasil dilatih dan tersimpan")
            
            df_proses = st.session_state.df_proses
            model = st.session_state.nb_model
            tfidf = st.session_state.tfidf
            y_test = st.session_state.y_test
            X_test_vec = tfidf.transform(st.session_state.X_test)
            y_pred = model.predict(X_test_vec)
            
            acc = accuracy_score(y_test, y_pred) * 100
            
            c1, c2, c3, c4 = st.columns(4)
            jml_pos = len(df_proses[df_proses['label'] == 'Positif'])
            jml_neg = len(df_proses[df_proses['label'] == 'Negatif'])
            
            with c1:
                st.metric("Total Data", f"{len(df_proses)}")
            with c2:
                st.metric("Positif", f"{jml_pos}")
            with c3:
                st.metric("Negatif", f"{jml_neg}")
            with c4:
                st.metric("Akurasi", f"{acc:.2f}%")
            
            st.divider()
            
            ce1, ce2, ce3 = st.columns(3)
            f1_pos = f1_score(y_test, y_pred, labels=['Positif'], average='macro', zero_division=0) * 100
            f1_neg = f1_score(y_test, y_pred, labels=['Negatif'], average='macro', zero_division=0) * 100
            
            with ce1:
                st.metric("Akurasi", f"{acc:.2f}%")
            with ce2:
                st.metric("F1-Score (Positif)", f"{f1_pos:.2f}%")
            with ce3:
                st.metric("F1-Score (Negatif)", f"{f1_neg:.2f}%")
            
            st.divider()
            
            col_cm, col_report = st.columns([1, 1.5])
            
            with col_cm:
                st.markdown("**Confusion Matrix**")
                cm = confusion_matrix(y_test, y_pred, labels=model.classes_)
                fig_cm, ax_cm = plt.subplots(figsize=(4.5, 3.5))
                sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', cbar=False,
                            xticklabels=model.classes_, yticklabels=model.classes_,
                            annot_kws={"size": 11, "weight": "bold"}, linewidths=1, linecolor='white')
                ax_cm.set_ylabel('Data Asli', fontsize=9)
                ax_cm.set_xlabel('Prediksi', fontsize=9)
                plt.xticks(fontsize=8)
                plt.yticks(fontsize=8, rotation=0)
                fig_cm.patch.set_alpha(0)
                plt.tight_layout()
                st.pyplot(fig_cm, use_container_width=True)
            
            with col_report:
                st.markdown("**Classification Report**")
                report_dict = classification_report(y_test, y_pred, output_dict=True, zero_division=0)
                report_df = pd.DataFrame(report_dict).transpose()
                
                for col in ['precision', 'recall', 'f1-score']:
                    report_df[col] = (report_df[col] * 100).apply(lambda x: f"{x:.2f}%")
                report_df['support'] = report_df['support'].astype(int)
                report_df = report_df.rename(columns={"precision": "Precision", "recall": "Recall", "f1-score": "F1-Score", "support": "Support"})
                
                st.dataframe(report_df, use_container_width=True, height=200)
            
            st.divider()
            
            cb1, cb2, cb3 = st.columns([1, 1.5, 1])
            with cb2:
                if st.button("🔄 Training Ulang Model", use_container_width=True, type="primary"):
                    st.session_state.nb_model = None
                    st.session_state.tfidf = None
                    st.rerun()
        
        else:
            st.info("📌 Model belum dilatih. Klik tombol di bawah untuk memulai training.")
            
            st.divider()
            
            cb1, cb2, cb3 = st.columns([1, 1.5, 1])
            with cb2:
                if st.button("🚀 Mulai Training Model", use_container_width=True, type="primary"):
                    with st.spinner("Melatih model algoritma Naïve Bayes..."):
                        tfidf = TfidfVectorizer(max_features=5000, ngram_range=(1,2), min_df=2)
                        X_train_vec = tfidf.fit_transform(st.session_state.X_train)
                        model = MultinomialNB(alpha=0.1)
                        model.fit(X_train_vec, st.session_state.y_train)
                        
                        st.session_state.tfidf = tfidf
                        st.session_state.nb_model = model
                        
                        st.success("✅ Training selesai! Model berhasil disimpan.")
                        st.rerun()

# ==================== MENU UJI KLASIFIKASI ====================
elif menu == "🔍 Uji Klasifikasi":
    hero("Uji Klasifikasi Sentimen", "Masukkan ulasan untuk dianalisis sentimennya", "🔬")
    
    if metode_uji == "Lexicon":
        st.info("📖 Mode Lexicon - Mencocokkan kata positif/negatif dasar")
        
        c1, c2 = st.columns([2, 1.2])
        with c1:
            teks = st.text_area("Masukkan ulasan:", height=90, 
                               placeholder="Contoh: Aplikasi ini bagus banget, transfer cepat")
            if st.button("🔍 Analisis", use_container_width=True, type="primary"):
                if teks.strip():
                    hasil = label_lexicon_sederhana(teks)
                    teks_bersih = praproses(teks)
                    
                    if hasil == "Positif": st.success(f"### 🟢 Hasil: {hasil}")
                    elif hasil == "Negatif": st.error(f"### 🔴 Hasil: {hasil}")
                    else: st.warning(f"### 🟡 Hasil: {hasil}")
                    
                    with st.expander("Lihat detail preprocessing"):
                        st.code(teks_bersih)
                else:
                    st.error("Masukkan teks terlebih dahulu")
        
        with c2:
            st.markdown("""
            <div style="background:#ffffff;border-radius:12px;padding:0.8rem 1rem;border:1px solid #e2e8f0;">
                <p style="font-weight:600;font-size:0.75rem;color:#1e293b;margin-bottom:0.3rem;">📝 Kata Positif</p>
                <p style="font-size:0.7rem;color:#64748b;margin-bottom:0.5rem;">bagus, mantap, baik, cepat, mudah, puas, suka</p>
                <p style="font-weight:600;font-size:0.75rem;color:#1e293b;margin-bottom:0.3rem;">📝 Kata Negatif</p>
                <p style="font-size:0.7rem;color:#64748b;">jelek, lambat, error, gagal, susah, ribet, buruk</p>
            </div>
            """, unsafe_allow_html=True)
    
    else:
        model = st_get("nb_model")
        if model is None:
            st.warning("⚠️ Model belum dilatih. Training dulu di menu Training.")
        else:
            st.info("🧠 Mode Naïve Bayes - Menggunakan probabilitas machine learning")
            
            teks = st.text_area("Masukkan ulasan:", height=90,
                               placeholder="Contoh: Aplikasi ini bagus banget, transfer cepat")
            if st.button("🔍 Prediksi", use_container_width=True, type="primary"):
                if teks.strip():
                    teks_bersih = praproses(teks)
                    vektor = st.session_state.tfidf.transform([teks_bersih])
                    pred = model.predict(vektor)[0]
                    prob = model.predict_proba(vektor)[0]
                    
                    if pred == "Positif": st.success(f"### 🟢 Hasil Prediksi: {pred}")
                    elif pred == "Negatif": st.error(f"### 🔴 Hasil Prediksi: {pred}")
                    else: st.warning(f"### 🟡 Hasil Prediksi: {pred}")
                    
                    prob_df = pd.DataFrame({
                        "Kategori Kelas": model.classes_,
                        "Persentase Keyakinan": [f"{p*100:.1f}%" for p in prob]
                    })
                    st.dataframe(prob_df, hide_index=True, use_container_width=True)
                    
                    with st.expander("Lihat detail preprocessing"):
                        st.code(teks_bersih)
                else:
                    st.error("Masukkan teks terlebih dahulu")

# ==================== MENU LAPORAN ====================
elif menu == "📊 Laporan":
    hero("Laporan Hasil Analisis", "Dashboard komprehensif untuk kebutuhan skripsi", "📋")
    
    df_proses = st_get("df_proses")
    if df_proses is None:
        st.warning("⚠️ Belum ada data. Proses data terlebih dahulu di menu Preprocessing.")
    else:
        tabs = st.tabs(["📈 Analisis Sentimen", "🏆 Komparasi Platform", "📥 Export Data"])
        
        with tabs[0]:
            c1, c2 = st.columns(2)
            with c1:
                dist = df_proses["label"].value_counts()
                fig, ax = plt.subplots(figsize=(5, 4))
                colors = ['#22c55e', '#ef4444', '#f59e0b']
                ax.pie(dist.values, labels=dist.index, autopct='%1.1f%%', colors=colors, 
                       wedgeprops={'edgecolor': 'white', 'linewidth': 2})
                ax.set_title("Distribusi Sentimen", fontsize=11, fontweight='bold')
                st.pyplot(fig, use_container_width=True)
            with c2:
                fig, ax = plt.subplots(figsize=(6, 4))
                ax.bar(dist.index, dist.values, color=['#22c55e','#ef4444','#f59e0b'])
                for i, v in enumerate(dist.values):
                    ax.text(i, v + (max(dist.values)*0.02), str(v), ha='center', fontweight='bold')
                ax.set_ylabel("Jumlah")
                ax.set_xlabel("Label Sentimen")
                st.pyplot(fig, use_container_width=True)
        
        with tabs[1]:
            app_sentimen = pd.crosstab(df_proses["aplikasi"], df_proses["label"])
            
            fig, ax = plt.subplots(figsize=(8, 4))
            app_sentimen.plot(kind='bar', stacked=False, ax=ax, color=['#22c55e', '#ef4444', '#f59e0b'])
            plt.xticks(rotation=0)
            ax.set_ylabel("Jumlah Ulasan")
            ax.set_xlabel("Platform E-Wallet")
            ax.legend(title="Sentimen")
            for container in ax.containers:
                ax.bar_label(container, label_type='edge', fontsize=8)
            plt.tight_layout()
            st.pyplot(fig, use_container_width=True)
            
            st.divider()
            
            skor = {}
            for app in df_proses["aplikasi"].unique():
                df_app = df_proses[df_proses["aplikasi"] == app]
                positif = len(df_app[df_app["label"] == "Positif"])
                negatif = len(df_app[df_app["label"] == "Negatif"])
                skor[app] = (positif - negatif) / len(df_app) * 100
            
            terbaik = max(skor, key=skor.get)
            st.success(f"🥇 **{terbaik}** adalah platform dengan sentimen pengguna terbaik.")
            
            cols = st.columns(len(df_proses["aplikasi"].unique()))
            for i, app in enumerate(df_proses["aplikasi"].unique()):
                with cols[i]:
                    df_app = df_proses[df_proses["aplikasi"] == app]
                    dist = df_app["label"].value_counts()
                    st.info(f"**📱 {app}**\n\nTotal: {len(df_app)}\n🟢 {dist.get('Positif',0)}\n🔴 {dist.get('Negatif',0)}\n⚪ {dist.get('Netral',0)}")
        
        with tabs[2]:
            st.write("**📥 Download Data untuk Skripsi**")
            
            c1, c2 = st.columns(2)
            with c1:
                csv_proses = df_proses.to_csv(index=False).encode('utf-8')
                st.download_button(
                    "⬇️ Data Sentimen Lengkap",
                    csv_proses,
                    "Lampiran_Data_Sentimen_Full.csv",
                    "text/csv",
                    use_container_width=True
                )
                st.caption("📌 Untuk **Lampiran** skripsi")
            
            with c2:
                rekap_df = pd.crosstab(df_proses["aplikasi"], df_proses["label"]).reset_index()
                csv_rekap = rekap_df.to_csv(index=False).encode('utf-8')
                st.download_button(
                    "⬇️ Rekap Sentimen per Platform",
                    csv_rekap,
                    "Tabel_Rekap_Sentimen_Bab4.csv",
                    "text/csv",
                    use_container_width=True
                )
                st.caption("📌 Untuk **Tabel 4.1** di Bab 4")