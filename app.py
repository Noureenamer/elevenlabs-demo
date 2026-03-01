import streamlit as st

st.set_page_config(
    page_title="خدمة العملاء | Smart Support",
    page_icon="🎯",
    layout="centered"
)

AGENT_ID = "agent_5401kj0w72jgfq5sed8kv93cqmzz"

# ── LOAD CSS FROM FILE ──
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ── MASTHEAD ──
st.markdown("""
<div class="masthead">
    <div class="masthead-brand">Smart Support · مركز الدعم</div>
    <div class="masthead-live">
        <div class="live-dot"></div>
        Agent Online
    </div>
</div>
""", unsafe_allow_html=True)

# ── HERO ──
st.markdown("""
<div class="hero">
    <div class="hero-left">
        <div class="hero-eyebrow">AI-Powered Customer Service</div>
        <div class="hero-title">Your Support,<br><em>Reimagined.</em></div>
        <div class="hero-arabic">مساعدك الذكي — على مدار الساعة</div>
        <p class="hero-desc">An intelligent agent that speaks Egyptian Arabic, handles returns, orders, and all your questions — instantly, 24/7.</p>
    </div>
    <div class="hero-right">
        <span class="hero-number">24/7</span>
        <div class="hero-number-label">Always Available</div>
    </div>
</div>
""", unsafe_allow_html=True)

# ── PILLS ──
st.markdown("""
<div class="pills">
    <span class="pill pill-gold">🇪🇬 Egyptian Arabic</span>
    <span class="pill pill-sage">✅ Live Agent</span>
    <span class="pill pill-rust">🎙️ Voice + Text</span>
    <span class="pill pill-muted">🤖 ElevenLabs AI</span>
    <span class="pill pill-muted">⚡ Instant Replies</span>
</div>
""", unsafe_allow_html=True)

# ── FEATURE STRIP ──
st.markdown("""
<div class="features">
    <div class="feat">
        <div class="feat-icon">🔄</div>
        <div class="feat-title">Returns</div>
        <div class="feat-desc">طلبات الإرجاع خلال 14 يوم</div>
    </div>
    <div class="feat">
        <div class="feat-icon">📦</div>
        <div class="feat-title">Orders</div>
        <div class="feat-desc">متابعة وإلغاء الطلبات</div>
    </div>
    <div class="feat">
        <div class="feat-icon">💬</div>
        <div class="feat-title">FAQ</div>
        <div class="feat-desc">إجابات فورية على كل سؤال</div>
    </div>
    <div class="feat">
        <div class="feat-icon">👤</div>
        <div class="feat-title">Customers</div>
        <div class="feat-desc">تسجيل عملاء جدد بسهولة</div>
    </div>
</div>
""", unsafe_allow_html=True)

# ── WIDGET HEADER ──
st.markdown("""
<div class="widget-section">
    <div class="section-header">
        <span class="section-num">01</span>
        <span class="section-title">Talk to the Agent</span>
        <span class="section-sub">Voice &amp; Text · العربي المصري</span>
    </div>
    <div class="widget-frame">
        <div class="widget-topbar">
            <div class="wt-dots">
                <div class="wt-dot wt-dot-r"></div>
                <div class="wt-dot wt-dot-y"></div>
                <div class="wt-dot wt-dot-g"></div>
            </div>
            <div class="wt-live-badge">● LIVE</div>
            <div class="wt-label">Smart Support Agent</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ── ELEVENLABS WIDGET ──
widget_html = f"""
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<style>
  * {{ margin:0; padding:0; box-sizing:border-box; }}
  html, body {{ width:100%; height:100%; background:transparent; overflow:hidden; }}
  .widget-wrapper {{
    width:100%; height:700px;
    display:flex; justify-content:center; align-items:flex-start;
    padding:10px 0;
    background: #F5F0E8;
  }}
  elevenlabs-convai {{
    width: 100% !important;
    max-width: 800px;
    height: 680px !important;
    display: block !important;
  }}
</style>
</head>
<body>
<div class="widget-wrapper">
  <elevenlabs-convai agent-id="{AGENT_ID}" expand="true" expandedbydefault="true"></elevenlabs-convai>
</div>
<script src="https://elevenlabs.io/convai-widget/index.js" async></script>
<script>
  function forceExpand() {{
    var w = document.querySelector('elevenlabs-convai');
    if (w) {{
      w.setAttribute('expand', 'true');
      w.setAttribute('expandedbydefault', 'true');
      try {{
        var s = w.shadowRoot;
        if (s) {{
          var b = s.querySelector('[data-testid="expand-button"], button[aria-label*="expand"], .expand-btn');
          if (b) b.click();
        }}
      }} catch(e) {{}}
    }}
  }}
  [300, 800, 1500, 3000, 5000].forEach(t => setTimeout(forceExpand, t));
</script>
</body>
</html>
"""
st.components.v1.html(widget_html, height=720, scrolling=False)

# ── HOW TO USE ──
st.markdown("""
<div class="section-header" style="margin-top:50px;">
    <span class="section-num">02</span>
    <span class="section-title">How to Use</span>
    <span class="section-sub">كيفية الاستخدام</span>
</div>
<div class="howto">
    <div class="howto-col">
        <div class="howto-label">Option A</div>
        <div class="howto-heading">🎙️ Voice Call</div>
        <div class="howto-step"><span class="step-n">1.</span><span class="step-t">Click <b>"Start a call"</b> button above</span></div>
        <div class="howto-step"><span class="step-n">2.</span><span class="step-t">Allow <b>microphone</b> access when prompted</span></div>
        <div class="howto-step"><span class="step-n">3.</span><span class="step-t">Speak naturally in <b>Egyptian Arabic</b></span></div>
        <div class="howto-step"><span class="step-n">4.</span><span class="step-t">Agent replies with <b>voice instantly</b></span></div>
    </div>
    <div class="howto-col rtl-col">
        <div class="howto-label">Option B — الخيار الثاني</div>
        <div class="howto-heading">💬 محادثة نصية</div>
        <div class="howto-step"><span class="step-n">١.</span><span class="step-t">اضغط <b>"Start a call"</b> في الأعلى</span></div>
        <div class="howto-step"><span class="step-n">٢.</span><span class="step-t">دور على <b>صندوق النص</b> في الأسفل</span></div>
        <div class="howto-step"><span class="step-n">٣.</span><span class="step-t">اكتب رسالتك واضغط <b>Enter</b></span></div>
        <div class="howto-step"><span class="step-n">٤.</span><span class="step-t">الأجنت هيرد عليك <b>فوراً بالعربي</b></span></div>
    </div>
</div>
""", unsafe_allow_html=True)

# ── FOOTER ──
st.markdown("""
<div class="footer-strip">
    <div class="footer-brand">Smart Support · مركز الدعم الذكي</div>
    <div class="footer-meta">Powered by <span>ElevenLabs AI</span> · v4.0</div>
</div>
""", unsafe_allow_html=True)
