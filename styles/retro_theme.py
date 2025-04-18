def get_retro_css():
    """Return CSS for retro gaming theme"""
    return """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=VT323&family=Press+Start+2P&family=Space+Mono:wght@400;700&display=swap');

    :root {
        --wellow-pink: #E5174D;
        --wellow-yellow: #FFCC33;
        --retro-black: #0F0F0F;
        --retro-red: #FF0000;
        --retro-blue: #0000FF;
        --pixel-border: 4px solid black;
        --coral-pink: #F88379;
    }

    /* Main layout */
    .main {
        background-color: var(--coral-pink) !important;
    }

    .main .block-container {
        padding-top: 2rem;
        background-color: var(--coral-pink);
    }

    /* Custom title */
    .custom-title {
        font-family: 'Press Start 2P', monospace;
        font-size: 2.2rem;
        color: var(--wellow-yellow);
        text-shadow: 4px 4px 0px var(--retro-black);
        background-color: var(--wellow-pink);
        padding: 20px;
        border: var(--pixel-border);
        margin-bottom: 20px;
        text-align: center;
    }

    /* Section headers */
    .section-header {
        font-family: 'VT323', monospace;
        font-size: 2rem;
        background-color: var(--retro-red);
        color: white;
        padding: 10px;
        border: var(--pixel-border);
        margin-top: 15px;
        margin-bottom: 15px;
    }

    /* Metric cards */
    .metric-card {
        font-family: 'Press Start 2P', monospace;
        background-color: var(--retro-black);
        color: white;
        padding: 15px;
        border: var(--pixel-border);
        margin-bottom: 10px;
        text-align: center;
    }

    .metric-title {
        font-size: 1rem;
        color: var(--wellow-yellow);
        margin-bottom: 10px;
    }

    .metric-value {
        font-size: 1.5rem;
        color: white;
    }

    /* Game-like buttons */
    .game-button {
        font-family: 'Press Start 2P', monospace;
        background-color: var(--retro-red);
        color: white;
        padding: 10px 15px;
        border: var(--pixel-border);
        text-align: center;
        cursor: pointer;
        display: inline-block;
        margin: 5px;
    }

    /* Sidebar styling */
    section[data-testid="stSidebar"] {
        background-color: var(--retro-black);
        border-right: var(--pixel-border);
        padding: 1rem;
    }

    /* Chart container */
    .chart-container {
        border: var(--pixel-border);
        padding: 10px;
        background-color: rgba(255, 255, 255, 0.1);
        margin-bottom: 15px;
    }
    </style>
    """

def apply_retro_theme(st):
    """Apply retro gaming theme to Streamlit app"""
    st.markdown(get_retro_css(), unsafe_allow_html=True)