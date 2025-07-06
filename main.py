# main.py
import streamlit as st
from prompts import PLATFORM_PROMPTS
from reformatter import generate_platform_outputs
import os
from dotenv import load_dotenv

load_dotenv()

# Page config
st.set_page_config(
    page_title="Content Reformatter • Cosmic Edition",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for outer space theme
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    .stApp {
        background: linear-gradient(135deg, #0c0c0c 0%, #1a1a2e 25%, #16213e 50%, #1a1a2e 75%, #0c0c0c 100%);
        font-family: 'Inter', sans-serif;
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Main container */
    .main-container {
        max-width: 1200px;
        margin: 0 auto;
        padding: 2rem 1rem;
    }
    
    /* Hero section */
    .hero {
        text-align: center;
        margin-bottom: 3rem;
        padding: 2rem 0;
    }
    
    .hero h1 {
        font-size: 3.5rem;
        font-weight: 700;
        background: linear-gradient(45deg, #64ffda, #bb86fc, #03dac6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 1rem;
        text-shadow: 0 0 30px rgba(100, 255, 218, 0.3);
    }
    
    .hero p {
        font-size: 1.2rem;
        color: #a0a0a0;
        max-width: 600px;
        margin: 0 auto;
        line-height: 1.6;
    }
    
    /* Section styling */
    .section {
        background: rgba(255, 255, 255, 0.05);
        border-radius: 16px;
        padding: 2rem;
        margin-bottom: 2rem;
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
    }
    
    .section h2 {
        color: #64ffda;
        font-size: 1.5rem;
        font-weight: 600;
        margin-bottom: 1rem;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    
    /* Custom text area */
    .stTextArea textarea {
        background: rgba(0, 0, 0, 0.4) !important;
        color: #ffffff !important;
        border: 1px solid rgba(100, 255, 218, 0.3) !important;
        border-radius: 12px !important;
        font-family: 'Inter', sans-serif !important;
        font-size: 14px !important;
        line-height: 1.6 !important;
        padding: 1rem !important;
    }
    
    .stTextArea textarea:focus {
        border-color: #64ffda !important;
        box-shadow: 0 0 0 2px rgba(100, 255, 218, 0.2) !important;
    }
    
    /* Platform selection */
    .stMultiSelect > div > div {
        background: rgba(0, 0, 0, 0.4) !important;
        border: 1px solid rgba(100, 255, 218, 0.3) !important;
        border-radius: 12px !important;
    }
    
    .stMultiSelect > div > div > div {
        color: #ffffff !important;
    }
    
    /* Custom button */
    .generate-btn {
        background: linear-gradient(45deg, #64ffda, #bb86fc);
        color: #000000;
        border: none;
        border-radius: 12px;
        padding: 1rem 2rem;
        font-size: 1.1rem;
        font-weight: 600;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(100, 255, 218, 0.3);
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    .generate-btn:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(100, 255, 218, 0.5);
    }
    
    /* Output section */
    .output-card {
        background: rgba(0, 0, 0, 0.6);
        border-radius: 12px;
        padding: 1.5rem;
        margin-bottom: 1.5rem;
        border: 1px solid rgba(100, 255, 218, 0.2);
    }
    
    .output-card h3 {
        color: #bb86fc;
        font-size: 1.2rem;
        font-weight: 600;
        margin-bottom: 1rem;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    
    /* Code blocks */
    .stCode {
        background: rgba(0, 0, 0, 0.8) !important;
        border: 1px solid rgba(100, 255, 218, 0.2) !important;
        border-radius: 8px !important;
    }
    
    /* Download buttons */
    .stDownloadButton button {
        background: linear-gradient(45deg, #03dac6, #64ffda) !important;
        color: #000000 !important;
        border: none !important;
        border-radius: 8px !important;
        padding: 0.5rem 1rem !important;
        font-weight: 500 !important;
        transition: all 0.3s ease !important;
    }
    
    .stDownloadButton button:hover {
        transform: translateY(-1px) !important;
        box-shadow: 0 4px 12px rgba(3, 218, 198, 0.4) !important;
    }
    
    /* Spinner styling */
    .stSpinner {
        color: #64ffda !important;
    }
    
    /* Success/Error messages */
    .stSuccess {
        background: rgba(3, 218, 198, 0.1) !important;
        border: 1px solid rgba(3, 218, 198, 0.3) !important;
        color: #03dac6 !important;
    }
    
    .stError {
        background: rgba(255, 82, 82, 0.1) !important;
        border: 1px solid rgba(255, 82, 82, 0.3) !important;
        color: #ff5252 !important;
    }
    
    /* Floating particles animation */
    .particles {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        pointer-events: none;
        z-index: -1;
    }
    
    .particle {
        position: absolute;
        background: #64ffda;
        border-radius: 50%;
        animation: float 20s infinite linear;
    }
    
    @keyframes float {
        0% { transform: translateY(100vh) rotate(0deg); opacity: 0; }
        10% { opacity: 1; }
        90% { opacity: 1; }
        100% { transform: translateY(-100vh) rotate(360deg); opacity: 0; }
    }
    
    /* Responsive design */
    @media (max-width: 768px) {
        .hero h1 { font-size: 2.5rem; }
        .section { padding: 1.5rem; }
        .main-container { padding: 1rem; }
    }
</style>
""", unsafe_allow_html=True)

# Floating particles background
st.markdown("""
<div class="particles">
    <div class="particle" style="left: 10%; animation-delay: 0s; width: 2px; height: 2px;"></div>
    <div class="particle" style="left: 20%; animation-delay: 2s; width: 1px; height: 1px;"></div>
    <div class="particle" style="left: 30%; animation-delay: 4s; width: 3px; height: 3px;"></div>
    <div class="particle" style="left: 40%; animation-delay: 6s; width: 2px; height: 2px;"></div>
    <div class="particle" style="left: 50%; animation-delay: 8s; width: 1px; height: 1px;"></div>
    <div class="particle" style="left: 60%; animation-delay: 10s; width: 2px; height: 2px;"></div>
    <div class="particle" style="left: 70%; animation-delay: 12s; width: 3px; height: 3px;"></div>
    <div class="particle" style="left: 80%; animation-delay: 14s; width: 1px; height: 1px;"></div>
    <div class="particle" style="left: 90%; animation-delay: 16s; width: 2px; height: 2px;"></div>
</div>
""", unsafe_allow_html=True)

# Main container
st.markdown('<div class="main-container">', unsafe_allow_html=True)

# Hero section
st.markdown("""
<div class="hero">
    <h1>✨✨Content Reformatter✨✨</h1>
    <p>Transform your content across the digital universe. One article, multiple platforms, infinite possibilities.</p>
</div>
""", unsafe_allow_html=True)

# Input section
st.markdown("""
<div class="section">
    <h2>📝 Master Article</h2>
</div>
""", unsafe_allow_html=True)

master_article = st.text_area(
    "",
    height=300,
    placeholder="Paste your master article here...\n\nThis is where your content journey begins. Write or paste your article, and watch as it transforms for different platforms.",
    help="Enter your original article content that will be reformatted for different platforms"
)

# Platform selection section
st.markdown("""
<div class="section">
    <h2> Platforms</h2>
</div>
""", unsafe_allow_html=True)

platforms = ["Medium", "Substack", "Dev.to", "Ko-fi"]
selected_platforms = st.multiselect(
    "",
    platforms,
    placeholder="Choose your Platforms...",
    help="Select which platforms you want to optimize your content for"
)

# Platform descriptions
if selected_platforms:
    st.markdown("""
    <div style="margin-top: 1rem; padding: 1rem; background: rgba(255, 255, 255, 0.05); border-radius: 8px; border-left: 3px solid #64ffda;">
        <p style="color: #a0a0a0; margin: 0; font-size: 0.9rem;">
            <strong>Selected:</strong> """ + ", ".join(selected_platforms) + """
        </p>
    </div>
    """, unsafe_allow_html=True)

# Generate button
st.markdown("<br>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    generate_clicked = st.button(
        "🚀 INITIATE TRANSFORMATION",
        use_container_width=True,
        help="Generate optimized content for selected platforms"
    )

# Generation logic
if generate_clicked and master_article and selected_platforms:
    st.markdown("""
    <div style="text-align: center; margin: 2rem 0;">
        <p style="color: #64ffda; font-size: 1.1rem; font-weight: 500;">
            🌟 Cosmic AI is reformatting your content...
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    with st.spinner("Transforming content across the digital cosmos..."):
        outputs = generate_platform_outputs(master_article, selected_platforms)

    # Success message
    st.success("✨ Transformation complete! Your content has been optimized for the selected platforms.")
    
    # Output section
    st.markdown("""
    <div class="section">
        <h2>📡 Generated Content</h2>
    </div>
    """, unsafe_allow_html=True)
    
    # Display outputs
    for platform, content in outputs.items():
        # Platform icons
        icons = {
            "Medium": "📖",
            "Substack": "📧", 
            "Dev.to": "👨‍💻",
            "Ko-fi": "☕"
        }
        
        st.markdown(f"""
        <div class="output-card">
            <h3>{icons.get(platform, "📝")} {platform} Version</h3>
        </div>
        """, unsafe_allow_html=True)
        
        # Content display
        st.code(content, language='markdown')
        
        # Download button
        col1, col2, col3 = st.columns([1, 1, 2])
        with col1:
            st.download_button(
                label=f"⬇️ Download {platform}",
                data=content,
                file_name=f"{platform.lower().replace('.', '')}_version.md",
                mime="text/markdown",
                key=f"download_{platform}"
            )

elif generate_clicked:
    if not master_article:
        st.error("🌌 The cosmos awaits your content! Please enter your master article.")
    elif not selected_platforms:
        st.error("🚀 Choose your destinations! Select at least one platform to launch your content.")

# Footer
st.markdown("""
<div style="text-align: center; margin-top: 4rem; padding: 2rem; border-top: 1px solid rgba(255, 255, 255, 0.1);">
    <p style="color: #666; font-size: 0.9rem;">
        Made with 🌟 for content creators exploring the digital universe
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)