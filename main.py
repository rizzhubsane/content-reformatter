# main.py
import streamlit as st
from prompts import PLATFORM_PROMPTS
from reformatter import generate_platform_outputs
import os
from dotenv import load_dotenv
import time

load_dotenv()

# Page config
st.set_page_config(
    page_title="Cosmic Content Forge • Neural Edition",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Advanced CSS for futuristic space theme
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Rajdhani:wght@300;400;500;600;700&display=swap');
    
    :root {
        --primary: #00fff0;
        --secondary: #ff0080;
        --accent: #8000ff;
        --bg-dark: #0a0a0a;
        --bg-card: rgba(10, 10, 10, 0.8);
        --glow: 0 0 20px;
    }
    
    * {
        box-sizing: border-box;
    }
    
    .stApp {
        background: radial-gradient(circle at 20% 50%, #120458 0%, transparent 50%),
                    radial-gradient(circle at 80% 20%, #8000ff 0%, transparent 50%),
                    radial-gradient(circle at 40% 80%, #00fff0 0%, transparent 50%),
                    linear-gradient(135deg, #000000 0%, #0a0a0a 100%);
        font-family: 'Rajdhani', sans-serif;
        min-height: 100vh;
        overflow-x: hidden;
    }
    
    /* Hide Streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stDeployButton {visibility: hidden;}
    
    /* Cyberpunk grid overlay */
    .cyber-grid {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-image: 
            linear-gradient(rgba(0, 255, 240, 0.03) 1px, transparent 1px),
            linear-gradient(90deg, rgba(0, 255, 240, 0.03) 1px, transparent 1px);
        background-size: 100px 100px;
        pointer-events: none;
        z-index: -1;
        animation: gridMove 20s linear infinite;
    }
    
    @keyframes gridMove {
        0% { transform: translate(0, 0); }
        100% { transform: translate(100px, 100px); }
    }
    
    /* Advanced particle system */
    .particle-system {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        pointer-events: none;
        z-index: -1;
        overflow: hidden;
    }
    
    .particle {
        position: absolute;
        background: var(--primary);
        border-radius: 50%;
        filter: blur(1px);
        animation: particleFloat 25s infinite linear;
    }
    
    .particle:nth-child(2n) {
        background: var(--secondary);
        animation-duration: 30s;
    }
    
    .particle:nth-child(3n) {
        background: var(--accent);
        animation-duration: 35s;
    }
    
    @keyframes particleFloat {
        0% { 
            transform: translateY(100vh) translateX(0) rotate(0deg); 
            opacity: 0; 
        }
        5% { opacity: 1; }
        95% { opacity: 1; }
        100% { 
            transform: translateY(-100vh) translateX(100px) rotate(360deg); 
            opacity: 0; 
        }
    }
    
    /* Neural network background */
    .neural-bg {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        pointer-events: none;
        z-index: -2;
    }
    
    .neural-node {
        position: absolute;
        width: 4px;
        height: 4px;
        background: var(--primary);
        border-radius: 50%;
        box-shadow: var(--glow) var(--primary);
        animation: pulse 4s ease-in-out infinite;
    }
    
    .neural-connection {
        position: absolute;
        height: 1px;
        background: linear-gradient(90deg, transparent, var(--primary), transparent);
        animation: dataFlow 6s ease-in-out infinite;
    }
    
    @keyframes pulse {
        0%, 100% { transform: scale(1); opacity: 0.7; }
        50% { transform: scale(1.5); opacity: 1; }
    }
    
    @keyframes dataFlow {
        0% { opacity: 0; transform: scaleX(0); }
        50% { opacity: 1; transform: scaleX(1); }
        100% { opacity: 0; transform: scaleX(0); }
    }
    
    /* Main container with holographic effect */
    .main-container {
        max-width: 1400px;
        margin: 0 auto;
        padding: 2rem;
        position: relative;
        z-index: 1;
    }
    
    /* Futuristic hero section */
    .hero {
        text-align: center;
        margin-bottom: 4rem;
        padding: 3rem 0;
        position: relative;
        overflow: hidden;
    }
    
    .hero::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: linear-gradient(45deg, transparent, rgba(0, 255, 240, 0.1), transparent);
        animation: scanLine 3s ease-in-out infinite;
    }
    
    @keyframes scanLine {
        0% { transform: translateX(-100%); }
        100% { transform: translateX(100%); }
    }
    
    .hero h1 {
        font-family: 'Orbitron', monospace;
        font-size: 4rem;
        font-weight: 900;
        background: linear-gradient(45deg, var(--primary), var(--secondary), var(--accent));
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 1rem;
        text-shadow: 0 0 30px rgba(0, 255, 240, 0.5);
        animation: glitchText 10s ease-in-out infinite;
        position: relative;
        z-index: 2;
    }
    
    @keyframes glitchText {
        0%, 90%, 100% { transform: translate(0); }
        91% { transform: translate(2px, -2px); }
        92% { transform: translate(-2px, 2px); }
        93% { transform: translate(2px, 2px); }
        94% { transform: translate(-2px, -2px); }
        95% { transform: translate(0); }
    }
    
    .hero p {
        font-size: 1.4rem;
        color: #b0b0b0;
        max-width: 700px;
        margin: 0 auto;
        line-height: 1.8;
        animation: fadeInUp 2s ease-out;
    }
    
    @keyframes fadeInUp {
        from { opacity: 0; transform: translateY(30px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    /* Futuristic section cards */
    .section {
        background: linear-gradient(145deg, rgba(0, 255, 240, 0.1), rgba(128, 0, 255, 0.1));
        border-radius: 20px;
        padding: 2.5rem;
        margin-bottom: 2rem;
        backdrop-filter: blur(20px);
        border: 2px solid transparent;
        background-clip: padding-box;
        position: relative;
        overflow: hidden;
        transition: all 0.4s ease;
        animation: slideInLeft 1s ease-out;
    }
    
    .section::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: linear-gradient(45deg, var(--primary), var(--secondary), var(--accent));
        border-radius: 20px;
        padding: 2px;
        mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
        mask-composite: exclude;
        z-index: -1;
    }
    
    .section:hover {
        transform: translateY(-5px);
        box-shadow: 0 20px 40px rgba(0, 255, 240, 0.3);
    }
    
    @keyframes slideInLeft {
        from { opacity: 0; transform: translateX(-50px); }
        to { opacity: 1; transform: translateX(0); }
    }
    
    .section h2 {
        font-family: 'Orbitron', monospace;
        color: var(--primary);
        font-size: 1.8rem;
        font-weight: 700;
        margin-bottom: 1.5rem;
        display: flex;
        align-items: center;
        gap: 1rem;
        text-shadow: 0 0 10px var(--primary);
    }
    
    /* Holographic text area */
    .stTextArea textarea {
        background: rgba(0, 0, 0, 0.9) !important;
        color: #ffffff !important;
        border: 2px solid rgba(0, 255, 240, 0.5) !important;
        border-radius: 15px !important;
        font-family: 'Rajdhani', sans-serif !important;
        font-size: 16px !important;
        line-height: 1.6 !important;
        padding: 1.5rem !important;
        transition: all 0.3s ease !important;
        box-shadow: inset 0 0 20px rgba(0, 255, 240, 0.1) !important;
    }
    
    .stTextArea textarea:focus {
        border-color: var(--primary) !important;
        box-shadow: 0 0 0 3px rgba(0, 255, 240, 0.3), inset 0 0 20px rgba(0, 255, 240, 0.2) !important;
        transform: scale(1.02) !important;
    }
    
    /* Futuristic multiselect */
    .stMultiSelect > div > div {
        background: rgba(0, 0, 0, 0.9) !important;
        border: 2px solid rgba(0, 255, 240, 0.5) !important;
        border-radius: 15px !important;
        transition: all 0.3s ease !important;
    }
    
    .stMultiSelect > div > div:focus-within {
        border-color: var(--primary) !important;
        box-shadow: 0 0 0 3px rgba(0, 255, 240, 0.3) !important;
    }
    
    /* Platform chips */
    .stMultiSelect span {
        background: linear-gradient(45deg, var(--primary), var(--secondary)) !important;
        color: #000000 !important;
        border-radius: 20px !important;
        padding: 0.5rem 1rem !important;
        font-weight: 600 !important;
        text-shadow: none !important;
    }
    
    /* Neural network generate button */
    .generate-button {
        background: linear-gradient(45deg, var(--primary), var(--secondary), var(--accent));
        border: none;
        border-radius: 50px;
        padding: 1.5rem 3rem;
        font-family: 'Orbitron', monospace;
        font-size: 1.2rem;
        font-weight: 700;
        color: #000000;
        cursor: pointer;
        transition: all 0.4s ease;
        position: relative;
        overflow: hidden;
        text-transform: uppercase;
        letter-spacing: 2px;
        box-shadow: 0 0 30px rgba(0, 255, 240, 0.5);
        animation: buttonPulse 3s ease-in-out infinite;
    }
    
    .generate-button::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.4), transparent);
        transition: left 0.5s ease;
    }
    
    .generate-button:hover::before {
        left: 100%;
    }
    
    .generate-button:hover {
        transform: scale(1.05);
        box-shadow: 0 0 50px rgba(0, 255, 240, 0.8);
    }
    
    @keyframes buttonPulse {
        0%, 100% { box-shadow: 0 0 30px rgba(0, 255, 240, 0.5); }
        50% { box-shadow: 0 0 50px rgba(0, 255, 240, 0.8); }
    }
    
    /* Holographic output cards */
    .output-card {
        background: linear-gradient(145deg, rgba(0, 0, 0, 0.9), rgba(0, 255, 240, 0.1));
        border-radius: 20px;
        padding: 2rem;
        margin-bottom: 2rem;
        border: 2px solid rgba(0, 255, 240, 0.3);
        position: relative;
        overflow: hidden;
        transition: all 0.4s ease;
        animation: materializeCard 0.8s ease-out;
    }
    
    .output-card::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: linear-gradient(45deg, transparent, rgba(0, 255, 240, 0.1), transparent);
        animation: hologramSweep 4s ease-in-out infinite;
    }
    
    @keyframes hologramSweep {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
    
    @keyframes materializeCard {
        from { 
            opacity: 0; 
            transform: translateY(50px) rotateX(45deg); 
        }
        to { 
            opacity: 1; 
            transform: translateY(0) rotateX(0deg); 
        }
    }
    
    .output-card:hover {
        transform: translateY(-10px) rotateX(5deg);
        box-shadow: 0 30px 60px rgba(0, 255, 240, 0.4);
    }
    
    .output-card h3 {
        font-family: 'Orbitron', monospace;
        color: var(--secondary);
        font-size: 1.4rem;
        font-weight: 700;
        margin-bottom: 1rem;
        display: flex;
        align-items: center;
        gap: 1rem;
        text-shadow: 0 0 10px var(--secondary);
        z-index: 2;
        position: relative;
    }
    
    /* Futuristic code blocks */
    .stCode {
        background: rgba(0, 0, 0, 0.95) !important;
        border: 2px solid rgba(0, 255, 240, 0.3) !important;
        border-radius: 15px !important;
        box-shadow: inset 0 0 20px rgba(0, 255, 240, 0.1) !important;
        font-family: 'Rajdhani', monospace !important;
        animation: codeAppear 1s ease-out !important;
    }
    
    @keyframes codeAppear {
        from { opacity: 0; transform: scale(0.9); }
        to { opacity: 1; transform: scale(1); }
    }
    
    /* Quantum download buttons */
    .stDownloadButton button {
        background: linear-gradient(45deg, var(--accent), var(--primary)) !important;
        color: #000000 !important;
        border: none !important;
        border-radius: 25px !important;
        padding: 0.8rem 2rem !important;
        font-family: 'Orbitron', monospace !important;
        font-weight: 600 !important;
        transition: all 0.3s ease !important;
        text-transform: uppercase !important;
        letter-spacing: 1px !important;
        box-shadow: 0 0 20px rgba(128, 0, 255, 0.5) !important;
    }
    
    .stDownloadButton button:hover {
        transform: translateY(-3px) scale(1.05) !important;
        box-shadow: 0 10px 25px rgba(128, 0, 255, 0.6) !important;
    }
    
    /* Loading animation */
    .loading-container {
        text-align: center;
        margin: 3rem 0;
    }
    
    .loading-text {
        font-family: 'Orbitron', monospace;
        font-size: 1.4rem;
        color: var(--primary);
        margin-bottom: 2rem;
        animation: loadingPulse 1.5s ease-in-out infinite;
    }
    
    @keyframes loadingPulse {
        0%, 100% { opacity: 0.7; }
        50% { opacity: 1; }
    }
    
    .loading-orb {
        width: 80px;
        height: 80px;
        margin: 0 auto;
        border-radius: 50%;
        background: linear-gradient(45deg, var(--primary), var(--secondary), var(--accent));
        animation: orbRotate 2s linear infinite;
        position: relative;
    }
    
    .loading-orb::before {
        content: '';
        position: absolute;
        top: -5px;
        left: -5px;
        right: -5px;
        bottom: -5px;
        border-radius: 50%;
        background: linear-gradient(45deg, var(--primary), var(--secondary), var(--accent));
        filter: blur(10px);
        z-index: -1;
    }
    
    @keyframes orbRotate {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
    
    /* Success/Error messages */
    .stSuccess {
        background: linear-gradient(45deg, rgba(0, 255, 240, 0.2), rgba(0, 255, 240, 0.1)) !important;
        border: 2px solid var(--primary) !important;
        border-radius: 15px !important;
        color: var(--primary) !important;
        font-family: 'Orbitron', monospace !important;
        animation: successGlow 2s ease-out !important;
    }
    
    @keyframes successGlow {
        0% { box-shadow: 0 0 0 var(--primary); }
        100% { box-shadow: 0 0 20px var(--primary); }
    }
    
    .stError {
        background: linear-gradient(45deg, rgba(255, 0, 128, 0.2), rgba(255, 0, 128, 0.1)) !important;
        border: 2px solid var(--secondary) !important;
        border-radius: 15px !important;
        color: var(--secondary) !important;
        font-family: 'Orbitron', monospace !important;
    }
    
    /* Platform selection feedback */
    .platform-feedback {
        background: linear-gradient(45deg, rgba(0, 255, 240, 0.1), rgba(128, 0, 255, 0.1));
        border-radius: 15px;
        padding: 1rem;
        margin-top: 1rem;
        border: 1px solid rgba(0, 255, 240, 0.3);
        animation: feedbackSlide 0.5s ease-out;
    }
    
    @keyframes feedbackSlide {
        from { opacity: 0; transform: translateX(-20px); }
        to { opacity: 1; transform: translateX(0); }
    }
    
    /* Responsive design */
    @media (max-width: 768px) {
        .hero h1 { font-size: 2.5rem; }
        .section { padding: 1.5rem; }
        .main-container { padding: 1rem; }
        .generate-button { padding: 1rem 2rem; font-size: 1rem; }
    }
    
    /* Accessibility */
    @media (prefers-reduced-motion: reduce) {
        * {
            animation-duration: 0.01ms !important;
            animation-iteration-count: 1 !important;
            transition-duration: 0.01ms !important;
        }
    }
</style>
""", unsafe_allow_html=True)

# Advanced particle system
st.markdown("""
<div class="cyber-grid"></div>
<div class="particle-system">
    <div class="particle" style="left: 5%; animation-delay: 0s; width: 2px; height: 2px;"></div>
    <div class="particle" style="left: 15%; animation-delay: 3s; width: 1px; height: 1px;"></div>
    <div class="particle" style="left: 25%; animation-delay: 6s; width: 3px; height: 3px;"></div>
    <div class="particle" style="left: 35%; animation-delay: 9s; width: 2px; height: 2px;"></div>
    <div class="particle" style="left: 45%; animation-delay: 12s; width: 1px; height: 1px;"></div>
    <div class="particle" style="left: 55%; animation-delay: 15s; width: 2px; height: 2px;"></div>
    <div class="particle" style="left: 65%; animation-delay: 18s; width: 3px; height: 3px;"></div>
    <div class="particle" style="left: 75%; animation-delay: 21s; width: 1px; height: 1px;"></div>
    <div class="particle" style="left: 85%; animation-delay: 24s; width: 2px; height: 2px;"></div>
    <div class="particle" style="left: 95%; animation-delay: 27s; width: 1px; height: 1px;"></div>
</div>
""", unsafe_allow_html=True)

# Neural network background
st.markdown("""
<div class="neural-bg">
    <div class="neural-node" style="top: 20%; left: 10%;"></div>
    <div class="neural-node" style="top: 40%; left: 30%;"></div>
    <div class="neural-node" style="top: 60%; left: 70%;"></div>
    <div class="neural-node" style="top: 80%; left: 90%;"></div>
    <div class="neural-connection" style="top: 20%; left: 10%; width: 200px; transform: rotate(45deg);"></div>
    <div class="neural-connection" style="top: 40%; left: 30%; width: 300px; transform: rotate(-30deg);"></div>
    <div class="neural-connection" style="top: 60%; left: 70%; width: 150px; transform: rotate(60deg);"></div>
</div>
""", unsafe_allow_html=True)

# Main container
st.markdown('<div class="main-container">', unsafe_allow_html=True)

# Futuristic hero section
st.markdown("""
<div class="hero">
    <h1>⚡ NEURAL FORGE</h1>
    <p>Quantum-powered content transformation across infinite digital dimensions. One neural pulse, unlimited platform manifestations.</p>
</div>
""", unsafe_allow_html=True)

# Input section with enhanced styling
st.markdown("""
<div class="section">
    <h2>🧠 Neural Input Matrix</h2>
</div>
""", unsafe_allow_html=True)

master_article = st.text_area(
    "",
    height=320,
    placeholder="Initialize neural input...\n\nConnect your consciousness to the quantum field. Your thoughts will be processed through advanced AI algorithms and manifested across multiple dimensional platforms.\n\nEnter your content and watch as the digital cosmos responds to your creative energy.",
    help="Neural interface for content input - your words become quantum data"
)

# Platform selection with enhanced feedback
st.markdown("""
<div class="section">
    <h2>🚀 Dimensional Targets</h2>
</div>
""", unsafe_allow_html=True)

platforms = ["Medium", "Substack", "Dev.to", "Ko-fi"]
selected_platforms = st.multiselect(
    "",
    platforms,
    placeholder="Select quantum destinations...",
    help="Choose dimensional portals for content manifestation"
)

# Enhanced platform feedback
if selected_platforms:
    platform_icons = {
        "Medium": "📖",
        "Substack": "📧", 
        "Dev.to": "👨‍💻",
        "Ko-fi": "☕"
    }
    
    platform_display = " • ".join([f"{platform_icons.get(p, '🌟')} {p}" for p in selected_platforms])
    
    st.markdown(f"""
    <div class="platform-feedback">
        <p style="color: var(--primary); margin: 0; font-family: 'Orbitron', monospace; font-weight: 600;">
            🎯 LOCKED TARGETS: {platform_display}
        </p>
        <p style="color: #888; margin: 0.5rem 0 0 0; font-size: 0.9rem;">
            Neural pathways established • Quantum entanglement initiated
        </p>
    </div>
    """, unsafe_allow_html=True)

# Enhanced generate button
st.markdown("<br><br>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    generate_clicked = st.button(
        "⚡ INITIATE QUANTUM TRANSFORMATION",
        use_container_width=True,
        help="Activate neural processing matrix"
    )

# Generation logic with enhanced loading
if generate_clicked and master_article and selected_platforms:
    # Custom loading animation
    st.markdown("""
    <div class="loading-container">
        <div class="loading-text">🌌 QUANTUM PROCESSING INITIATED</div>
        <div class="loading-orb"></div>
        <p style="color: #888; font-family: 'Orbitron', monospace; margin-top: 1rem;">
            Neural networks analyzing • Dimensional portals opening • Content matrix transforming
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Simulate processing time for better UX
    progress_bar = st.progress(0)
    for i in range(100):
        time.sleep(0.01)  # Very brief delay for visual effect
        progress_bar.progress(i + 1)
    
    with st.spinner("Quantum transformation in progress..."):
        outputs = generate_platform_outputs(master_article, selected_platforms)
    
    progress_bar.empty()
    
    # Enhanced success message
    st.markdown("""
    <div style="text-align: center; margin: 2rem 0;">
        <div style="font-family: 'Orbitron', monospace; font-size: 1.5rem; color: var(--primary); margin-bottom: 1rem; animation: successGlow 2s ease-out;">
            ✨ QUANTUM TRANSFORMATION COMPLETE
        </div>
        <p style="color: #888; font-size: 1.1rem;">
            Your content has been successfully manifested across selected dimensional platforms
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Output section with enhanced styling
    st.markdown("""
    <div class="section">
        <h2>🔬 Quantum Manifestations</h2>
    </div>
    """, unsafe_allow_html=True)
    
    # Display outputs with enhanced cards
    for i, (platform, content) in enumerate(outputs.items()):
        # Platform icons with enhanced styling
        icons = {
            "Medium": "📖",
            "Substack": "📧", 
            "Dev.to": "👨‍💻",
            "Ko-fi": "☕"
        }
        
        # Add delay for staggered animation
        st.markdown(f"""
        <div class="output-card" style="animation-delay: {i * 0.2}s;">
            <h3>{icons.get(platform, "🌟")} {platform} Manifestation</h3>
        </div>
        """, unsafe_allow_html=True)
        
        # Enhanced content display
        st.code(content, language='markdown')
        
        # Quantum download buttons
        col1, col2, col3 = st.columns([1, 1, 2])
        with col1:
            st.download_button(
                label=f"⬇️ Extract {platform}",
                data=content,
                file_name=f"{platform.lower().replace('.', '')}_quantum.md",
                mime="text/markdown",
                key=f"quantum_download_{platform}"
            )

elif generate_clicked:
    if not master_article:
        st.error("🧠 Neural interface requires input! Connect your consciousness to the quantum field.")
    elif not selected_platforms:
        st.error("🎯 Dimensional targets required! Select at least one platform for manifestation.")

# Enhanced footer with quantum branding
st.markdown("""
<div style="text-align: center; margin-top: 5rem; padding: 3rem; border-top: 1px solid rgba(0, 255, 240, 0.3); position: relative;">
    <div style="font-family: 'Orbitron', monospace; font-size: 1.2rem; color: var(--primary); margin-bottom: 1rem;">
        NEURAL FORGE v2.0
    </div>
    <p style="color: #666; font-size: 0.9rem; margin-bottom: 0;">
        Powered by quantum neural networks • Crafted for digital pioneers exploring infinite creative dimensions
    </p>
    <div style="margin-top: 2rem; display: flex; justify-content: center; gap: 2rem; flex-wrap: wrap;">
        <span style="color: var(--primary); font-size: 0.8rem; font-family: 'Orbitron', monospace;">🔮 QUANTUM READY</span>
        <span style="color: var(--secondary); font-size: 0.8rem; font-family: 'Orbitron', monospace;">⚡ NEURAL ENHANCED</span>
        <span style="color: var(--accent); font-size: 0.8rem; font-family: 'Orbitron', monospace;">🌌 DIMENSION OPTIMIZED</span>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
