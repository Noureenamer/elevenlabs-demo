import streamlit as st

st.set_page_config(
    page_title="خدمة العملاء | Smart Support",
    page_icon="🎯",
    layout="centered"
)

AGENT_ID = "agent_5401kj0w72jgfq5sed8kv93cqmzz"

st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=DM+Sans:wght@300;400;500;600&family=Tajawal:wght@300;400;700;900&display=swap" rel="stylesheet">
<style>
:root {
    --cream: #F5F0E8;
    --warm-white: #FDFAF4;
    --charcoal: #1A1814;
    --ink: #2D2926;
    --gold: #C9973A;
    --gold-light: #E8C475;
    --gold-pale: #F7EDD5;
    --rust: #C45C2E;
    --sage: #5A7A5E;
    --muted: #8C8479;
    --border: rgba(90,75,55,0.12);
    --shadow: rgba(26,24,20,0.08);
}

* { margin:0; padding:0; box-sizing:border-box; }

.stApp {
    background: var(--warm-white);
    font-family: 'DM Sans', sans-serif;
    color: var(--ink);
}

/* Subtle paper texture overlay */
.stApp::before {
    content:'';
    position:fixed;
    inset:0;
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='400' height='400'%3E%3Cfilter id='noise'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3CfeColorMatrix type='saturate' values='0'/%3E%3C/filter%3E%3Crect width='400' height='400' filter='url(%23noise)' opacity='0.03'/%3E%3C/svg%3E");
    pointer-events:none;
    z-index:0;
    opacity:0.6;
}

.block-container {
    position:relative;
    z-index:1;
    padding: 0 1rem 4rem;
    max-width: 860px !important;
}

/* ── MASTHEAD ── */
.masthead {
    border-bottom: 1px solid var(--border);
    padding: 18px 0 14px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 0;
}
.masthead-brand {
    font-family: 'DM Serif Display', serif;
    font-size: 1.05em;
    color: var(--charcoal);
    letter-spacing: 0.02em;
}
.masthead-live {
    display: flex;
    align-items: center;
    gap: 6px;
    font-size: 0.72em;
    font-weight: 600;
    color: var(--sage);
    letter-spacing: 1.5px;
    text-transform: uppercase;
}
.live-dot {
    width: 7px; height: 7px;
    background: var(--sage);
    border-radius: 50%;
    animation: blink 2s ease-in-out infinite;
}
@keyframes blink {
    0%,100% { opacity:1; }
    50% { opacity:0.25; }
}

/* ── HERO ── */
.hero {
    padding: 70px 0 50px;
    display: grid;
    grid-template-columns: 1fr auto;
    gap: 40px;
    align-items: end;
    border-bottom: 1px solid var(--border);
}
.hero-left {}
.hero-eyebrow {
    font-size: 0.72em;
    font-weight: 600;
    letter-spacing: 2.5px;
    text-transform: uppercase;
    color: var(--gold);
    margin-bottom: 18px;
}
.hero-title {
    font-family: 'DM Serif Display', serif;
    font-size: clamp(2.8em, 7vw, 5em);
    line-height: 1.0;
    color: var(--charcoal);
    margin-bottom: 16px;
}
.hero-title em {
    font-style: italic;
    color: var(--rust);
}
.hero-arabic {
    font-family: 'Tajawal', sans-serif;
    font-size: 1.3em;
    font-weight: 700;
    color: var(--muted);
    direction: rtl;
    margin-bottom: 22px;
    line-height: 1.5;
}
.hero-desc {
    font-size: 0.92em;
    color: var(--muted);
    line-height: 1.7;
    max-width: 400px;
}
.hero-right {
    text-align: right;
    padding-bottom: 6px;
}
.hero-number {
    font-family: 'DM Serif Display', serif;
    font-size: 5em;
    color: var(--gold-pale);
    line-height: 1;
    display: block;
}
.hero-number-label {
    font-size: 0.72em;
    color: var(--muted);
    letter-spacing: 1.5px;
    text-transform: uppercase;
}

/* ── PILLS ── */
.pills {
    display: flex;
    gap: 8px;
    flex-wrap: wrap;
    padding: 24px 0;
    border-bottom: 1px solid var(--border);
}
.pill {
    padding: 7px 18px;
    border-radius: 100px;
    font-size: 0.78em;
    font-weight: 500;
    border: 1px solid;
    font-family: 'DM Sans', sans-serif;
}
.pill-gold   { color: var(--gold);  border-color: var(--gold);  background: rgba(201,151,58,0.06); }
.pill-rust   { color: var(--rust);  border-color: var(--rust);  background: rgba(196,92,46,0.06); }
.pill-sage   { color: var(--sage);  border-color: var(--sage);  background: rgba(90,122,94,0.06); }
.pill-muted  { color: var(--muted); border-color: var(--border); background: rgba(0,0,0,0.02); }

/* ── FEATURE STRIP ── */
.features {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    border-bottom: 1px solid var(--border);
}
.feat {
    padding: 30px 20px;
    border-right: 1px solid var(--border);
    transition: background 0.25s;
}
.feat:last-child { border-right: none; }
.feat:hover { background: var(--gold-pale); }
.feat-icon { font-size: 1.6em; margin-bottom: 12px; }
.feat-title {
    font-family: 'DM Serif Display', serif;
    font-size: 0.95em;
    color: var(--charcoal);
    margin-bottom: 6px;
}
.feat-desc {
    font-family: 'Tajawal', sans-serif;
    font-size: 0.8em;
    color: var(--muted);
    line-height: 1.5;
    direction: rtl;
}

/* ── WIDGET SECTION ── */
.widget-section {
    padding: 50px 0 0;
}
.section-header {
    display: flex;
    align-items: baseline;
    gap: 14px;
    margin-bottom: 30px;
}
.section-num {
    font-family: 'DM Serif Display', serif;
    font-size: 1.5em;
    color: var(--gold-light);
}
.section-title {
    font-family: 'DM Serif Display', serif;
    font-size: 1.3em;
    color: var(--charcoal);
}
.section-sub {
    font-size: 0.82em;
    color: var(--muted);
    margin-left: auto;
    letter-spacing: 0.5px;
}

.widget-frame {
    border: 1px solid var(--border);
    border-radius: 20px;
    overflow: hidden;
    background: var(--cream);
    box-shadow: 0 4px 40px var(--shadow), 0 1px 0 rgba(255,255,255,0.8) inset;
    position: relative;
}
.widget-topbar {
    background: var(--charcoal);
    padding: 14px 20px;
    display: flex;
    align-items: center;
    gap: 12px;
}
.wt-dots { display:flex; gap:6px; }
.wt-dot {
    width: 10px; height: 10px; border-radius: 50%;
}
.wt-dot-r { background: #FF5F57; }
.wt-dot-y { background: #FEBC2E; }
.wt-dot-g { background: #28C840; }
.wt-label {
    font-size: 0.78em;
    color: rgba(255,255,255,0.4);
    letter-spacing: 1px;
    margin-left: auto;
    text-transform: uppercase;
}
.wt-live-badge {
    font-size: 0.72em;
    font-weight: 600;
    color: #28C840;
    display: flex;
    align-items: center;
    gap: 5px;
}

/* ── HOW TO ── */
.howto {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 1px;
    background: var(--border);
    border: 1px solid var(--border);
    border-radius: 16px;
    overflow: hidden;
    margin-top: 40px;
}
.howto-col {
    background: var(--warm-white);
    padding: 28px 26px;
}
.howto-col:hover { background: var(--gold-pale); transition: background 0.2s; }
.howto-label {
    font-size: 0.7em;
    font-weight: 600;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: var(--gold);
    margin-bottom: 14px;
}
.howto-heading {
    font-family: 'DM Serif Display', serif;
    font-size: 1.1em;
    color: var(--charcoal);
    margin-bottom: 14px;
}
.howto-step {
    display: flex;
    gap: 10px;
    align-items: flex-start;
    margin-bottom: 10px;
}
.step-n {
    font-family: 'DM Serif Display', serif;
    font-size: 0.9em;
    color: var(--gold);
    min-width: 18px;
    padding-top: 1px;
}
.step-t {
    font-size: 0.85em;
    color: var(--muted);
    line-height: 1.5;
}
.step-t b { color: var(--ink); }
.rtl-col { direction: rtl; text-align: right; }
.rtl-col .howto-step { flex-direction: row-reverse; }
.rtl-col .step-t { font-family: 'Tajawal', sans-serif; font-size: 0.9em; }

/* ── FOOTER ── */
.footer-strip {
    margin-top: 60px;
    padding: 28px 0;
    border-top: 1px solid var(--border);
    display: flex;
    align-items: center;
    justify-content: space-between;
}
.footer-brand {
    font-family: 'DM Serif Display', serif;
    font-size: 0.95em;
    color: var(--muted);
}
.footer-meta {
    font-size: 0.72em;
    color: rgba(140,132,121,0.5);
    letter-spacing: 1.5px;
    text-transform: uppercase;
}
.footer-meta span { color: var(--gold); }

#MainMenu, footer, header { visibility:hidden; }
.stDeployButton { display:none; }
</style>
""", unsafe_allow_html=True)

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

# ── WIDGET ──
st.markdown("""
<div class="widget-section">
    <div class="section-header">
        <span class="section-num">01</span>
        <span class="section-title">Talk to the Agent</span>
        <span class="section-sub">Voice & Text · العربي المصري</span>
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
""", unsafe_allow_html=True)

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
    --widget-width: 100%;
    width: 100% !important;
    max-width: 800px;
    height: 680px !important;
    display: block !important;
  }}
</style>
</head>
<body>
<div class="widget-wrapper">
  <elevenlabs-convai
    agent-id="{AGENT_ID}"
    expand="true"
    expandedbydefault="true">
  </elevenlabs-convai>
</div>
<script src="https://elevenlabs.io/convai-widget/index.js" async></script>
<script>
  function forceExpand() {{
    var widget = document.querySelector('elevenlabs-convai');
    if (widget) {{
      widget.setAttribute('expand', 'true');
      widget.setAttribute('expandedbydefault', 'true');
      try {{
        var shadow = widget.shadowRoot;
        if (shadow) {{
          var btn = shadow.querySelector('[data-testid="expand-button"], button[aria-label*="expand"], .expand-btn');
          if (btn) btn.click();
        }}
      }} catch(e) {{}}
    }}
  }}
  document.addEventListener('DOMContentLoaded', forceExpand);
  [300, 800, 1500, 3000, 5000].forEach(t => setTimeout(forceExpand, t));
  new MutationObserver(function(mutations) {{
    mutations.forEach(function(m) {{
      m.addedNodes.forEach(function(n) {{
        if (n.tagName === 'ELEVENLABS-CONVAI' || (n.querySelector && n.querySelector('elevenlabs-convai'))) {{
          setTimeout(forceExpand, 200);
        }}
      }});
    }});
  }}).observe(document.body, {{ childList:true, subtree:true }});
</script>
</body>
</html>
"""

st.components.v1.html(widget_html, height=720, scrolling=False)

st.markdown("</div></div>", unsafe_allow_html=True)

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
