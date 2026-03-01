import streamlit as st

st.set_page_config(
    page_title=" | Smart Support",
    page_icon="🎯",
    layout="centered"
)

AGENT_ID = "agent_5401kj0w72jgfq5sed8kv93cqmzz"

st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Tajawal:wght@300;400;700;900&family=Syne:wght@400;700;800&display=swap" rel="stylesheet">
<style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    .stApp { background: #050810; font-family: 'Syne', sans-serif; }
    .stApp::before {
        content: ''; position: fixed; top:-50%; left:-50%; width:200%; height:200%;
        background:
            radial-gradient(ellipse at 20% 20%, rgba(255,60,100,0.12) 0%, transparent 50%),
            radial-gradient(ellipse at 80% 80%, rgba(60,100,255,0.10) 0%, transparent 50%);
        animation: bgShift 8s ease-in-out infinite alternate;
        pointer-events: none; z-index: 0;
    }
    @keyframes bgShift {
        0%   { transform: translate(0,0) rotate(0deg); }
        100% { transform: translate(2%,2%) rotate(3deg); }
    }
    .stApp::after {
        content: ''; position: fixed; inset: 0;
        background-image:
            linear-gradient(rgba(255,255,255,0.015) 1px, transparent 1px),
            linear-gradient(90deg, rgba(255,255,255,0.015) 1px, transparent 1px);
        background-size: 50px 50px; pointer-events: none; z-index: 0;
    }
    .block-container { position:relative; z-index:1; padding:2rem 1rem 4rem; max-width:860px !important; }
    .header-wrap { text-align:center; padding:60px 20px 40px; }
    .header-eyebrow {
        display:inline-flex; align-items:center; gap:8px;
        background:rgba(255,60,100,0.1); border:1px solid rgba(255,60,100,0.3);
        color:#ff3c64; padding:6px 18px; border-radius:100px;
        font-size:0.75em; font-weight:700; letter-spacing:2px;
        text-transform:uppercase; margin-bottom:24px;
    }
    .pulse-dot { width:7px; height:7px; background:#ff3c64; border-radius:50%; animation:pulseDot 1.4s infinite; }
    @keyframes pulseDot {
        0%,100% { opacity:1; transform:scale(1); }
        50%      { opacity:0.4; transform:scale(0.7); }
    }
    .header-title {
        font-family:'Syne',sans-serif; font-size:clamp(2.2em,6vw,3.8em); font-weight:800;
        color:#ffffff; line-height:1.1; margin-bottom:8px; letter-spacing:-1px;
    }
    .header-title span {
        background:linear-gradient(135deg,#ff3c64,#ff8c42);
        -webkit-background-clip:text; -webkit-text-fill-color:transparent; background-clip:text;
    }
    .header-arabic {
        font-family:'Tajawal',sans-serif; font-size:clamp(1.1em,3vw,1.6em); font-weight:700;
        color:rgba(255,255,255,0.5); margin-bottom:20px; direction:rtl;
    }
    .header-desc { color:rgba(255,255,255,0.45); font-size:0.95em; max-width:500px; margin:0 auto 30px; line-height:1.6; }
    .badges { display:flex; justify-content:center; gap:10px; flex-wrap:wrap; margin-bottom:10px; }
    .badge { padding:6px 16px; border-radius:100px; font-size:0.78em; font-weight:700; }
    .badge-red    { background:rgba(255,60,100,0.15);  border:1px solid rgba(255,60,100,0.35);  color:#ff6b85; }
    .badge-blue   { background:rgba(60,130,255,0.15);  border:1px solid rgba(60,130,255,0.35);  color:#6b9eff; }
    .badge-orange { background:rgba(255,150,60,0.15);  border:1px solid rgba(255,150,60,0.35);  color:#ffb06b; }
    .badge-green  { background:rgba(60,255,150,0.15);  border:1px solid rgba(60,255,150,0.35);  color:#6bffb0; }
    .features-grid { display:grid; grid-template-columns:repeat(2,1fr); gap:14px; margin:30px 0; }
    .feature-card {
        background:rgba(255,255,255,0.03); border:1px solid rgba(255,255,255,0.07);
        border-radius:16px; padding:22px; transition:all 0.3s; position:relative; overflow:hidden;
    }
    .feature-card::before {
        content:''; position:absolute; top:0; left:0; right:0; height:2px;
        background:linear-gradient(90deg,transparent,var(--accent),transparent);
        opacity:0; transition:opacity 0.3s;
    }
    .feature-card:hover { background:rgba(255,255,255,0.06); border-color:rgba(255,255,255,0.15); transform:translateY(-2px); }
    .feature-card:hover::before { opacity:1; }
    .feature-icon  { font-size:1.8em; margin-bottom:10px; }
    .feature-title { color:#fff; font-weight:700; font-size:0.95em; margin-bottom:6px; }
    .feature-desc  { color:rgba(255,255,255,0.4); font-size:0.82em; line-height:1.5; font-family:'Tajawal',sans-serif; }
    .fc-red    { --accent:#ff3c64; } .fc-blue  { --accent:#3c82ff; }
    .fc-orange { --accent:#ff963c; } .fc-green { --accent:#3cff8a; }
    hr { border-color:rgba(255,255,255,0.06) !important; margin:30px 0 !important; }
    .how-to {
        background:rgba(255,255,255,0.02); border:1px solid rgba(255,255,255,0.06);
        border-radius:16px; padding:24px; margin-top:20px;
    }
    .how-to-title { color:rgba(255,255,255,0.4); font-size:0.75em; font-weight:700; letter-spacing:1.5px; text-transform:uppercase; margin-bottom:16px; }
    .how-to-grid { display:grid; grid-template-columns:1fr 1fr; gap:20px; }
    .how-to-col h4 { color:rgba(255,255,255,0.6); font-size:0.85em; margin-bottom:10px; }
    .how-to-col p { color:rgba(255,255,255,0.3); font-size:0.82em; line-height:1.9; font-family:'Tajawal',sans-serif; }
    .rtl { direction:rtl; text-align:right; }
    .ltr { direction:ltr; text-align:left; font-family:'Syne',sans-serif !important; }
    .footer {
        text-align:center; color:rgba(255,255,255,0.12); font-size:0.75em;
        margin-top:50px; padding-top:20px;
        border-top:1px solid rgba(255,255,255,0.05); letter-spacing:1.5px;
    }
    .footer span { color:#ff3c64; }
    #MainMenu, footer, header { visibility:hidden; }
    .stDeployButton { display:none; }
</style>
""", unsafe_allow_html=True)

# ===== HEADER =====
st.markdown("""
<div class="header-wrap">
    <div class="header-eyebrow"><div class="pulse-dot"></div>LIVE · AI AGENT ONLINE</div>
    <div class="header-title">Smart Customer<br><span>Support Center</span></div>
    <div class="header-arabic">مركز خدمة العملاء ا</div>
    <p class="header-desc">AI-powered agent for returns, orders, and customer registration — available 24/7 in Egyptian Arabic</p>
    <div class="badges">
        <span class="badge badge-red">🇪🇬 Egyptian Arabic</span>
        <span class="badge badge-blue">⚡ 24/7 Available</span>
        
        <span class="badge badge-green">✅ Live</span>
    </div>
</div>
""", unsafe_allow_html=True)

# ===== FEATURE CARDS =====
st.markdown("""
<div class="features-grid">
    <div class="feature-card fc-red">
        <div class="feature-icon">🔄</div>
        <div class="feature-title">Return Requests</div>
        <div class="feature-desc">فحص تلقائي لأهلية الإرجاع خلال 14 يوم</div>
    </div>
    <div class="feature-card fc-blue">
        <div class="feature-icon">📦</div>
        <div class="feature-title">Order Management</div>
        <div class="feature-desc">متابعة الأوردرات وتسجيل طلبات جديدة</div>
    </div>
    <div class="feature-card fc-orange">
        <div class="feature-icon">👤</div>
        <div class="feature-title">New Customers</div>
        <div class="feature-desc">تسجيل عملاء جدد وجمع بياناتهم بسهولة</div>
    </div>
    <div class="feature-card fc-green">
        <div class="feature-icon">❓</div>
        <div class="feature-title">FAQ Support</div>
        <div class="feature-desc">إجابات فورية من قاعدة المعرفة</div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# ===== WIDGET =====
widget_html = f"""
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<style>
  body {{
    margin: 0;
    padding: 20px 0;
    background: transparent;
    display: flex;
    justify-content: center;
    align-items: flex-start;
    min-height: 520px;
  }}
  elevenlabs-convai {{
    width: 100%;
    max-width: 640px;
  }}
</style>
</head>
<body>
  <elevenlabs-convai
    agent-id="{AGENT_ID}"
    expand="true">
  </elevenlabs-convai>
  <script src="https://elevenlabs.io/convai-widget/index.js" async></script>
  <script>
    window.addEventListener('load', function() {{
      function tryExpand() {{
        var w = document.querySelector('elevenlabs-convai');
        if (w) w.setAttribute('expand', 'true');
      }}
      setTimeout(tryExpand, 500);
      setTimeout(tryExpand, 1500);
      setTimeout(tryExpand, 3000);
    }});
  </script>
</body>
</html>
"""
st.components.v1.html(widget_html, height=560, scrolling=True)

# ===== HOW TO USE =====
st.markdown("""
<div class="how-to">
    <div class="how-to-title">📋 How to Use | كيفية الاستخدام</div>
    <div class="how-to-grid">
        <div class="how-to-col">
            <h4>🎙️ Voice Call</h4>
            <p class="ltr">
                1. Click the microphone button<br>
                2. Allow microphone access<br>
                3. Speak in Egyptian Arabic<br>
                4. Agent responds with voice
            </p>
        </div>
        <div class="how-to-col">
            <h4>💬 Text Chat</h4>
            <p class="rtl">
                ١. اكتب رسالتك في صندوق النص<br>
                ٢. اضغط Enter أو زر الإرسال<br>
                ٣. الأجنت هيرد عليك فوراً<br>
                ٤. تقدر تكتب بالعربي أو الإنجليزي
            </p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ===== FOOTER =====
st.markdown("""
<div class="footer">
    POWERED BY <span>ELEVENLABS AI</span> &nbsp;·&nbsp; BUILT FOR EGYPTIAN E-COMMERCE &nbsp;·&nbsp; VERSION 3.0
</div>
""", unsafe_allow_html=True)
