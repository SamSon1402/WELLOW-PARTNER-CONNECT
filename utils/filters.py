def setup_sidebar_filters(st, partners_df):
    """Set up sidebar filters"""
    st.sidebar.markdown('<h1 style="font-family: \'Press Start 2P\', monospace; color: #FFCC33; font-size: 1rem; text-align: center; margin-bottom: 20px;">WELLOW CONTROL PANEL</h1>', unsafe_allow_html=True)
    
    # Add start button
    st.sidebar.markdown('<div style="text-align: center; margin-bottom: 20px;">', unsafe_allow_html=True)
    st.sidebar.markdown(game_button("PRESS START", "start-button"), unsafe_allow_html=True)
    st.sidebar.markdown('</div>', unsafe_allow_html=True)
    
    # Partner type filter
    st.sidebar.markdown('<h2 style="font-family: \'VT323\', monospace; color: #FFCC33; font-size: 1.5rem;">SELECT PARTNER TYPE</h2>', unsafe_allow_html=True)
    partner_types = sorted(partners_df['PartnerType'].unique())
    selected_types = st.sidebar.multiselect("", partner_types, default=partner_types, label_visibility="collapsed")
    
    # Contact status filter
    st.sidebar.markdown('<h2 style="font-family: \'VT323\', monospace; color: #FFCC33; font-size: 1.5rem;">SELECT STATUS</h2>', unsafe_allow_html=True)
    contact_statuses = sorted(partners_df['ContactStatus'].unique())
    selected_statuses = st.sidebar.multiselect("", contact_statuses, default=contact_statuses, label_visibility="collapsed")
    
    # Potential value filter
    st.sidebar.markdown('<h2 style="font-family: \'VT323\', monospace; color: #FFCC33; font-size: 1.5rem;">SELECT VALUE</h2>', unsafe_allow_html=True)
    potential_values = ["High", "Medium", "Low"]
    selected_values = st.sidebar.multiselect("", potential_values, default=potential_values, label_visibility="collapsed")
    
    # Reset filters button
    st.sidebar.markdown('<div style="text-align: center; margin-top: 20px;">', unsafe_allow_html=True)
    reset_button = st.sidebar.button("RESET FILTERS", key="reset_filters")
    st.sidebar.markdown('</div>', unsafe_allow_html=True)
    
    if reset_button:
        selected_types = partner_types
        selected_statuses = contact_statuses
        selected_values = potential_values
    
    return selected_types, selected_statuses, selected_values

def game_button(label, key=None):
    """Create a game-like button"""
    button_html = f"""
    <div class="game-button" id="{key if key else ''}">
        {label}
    </div>
    """
    return button_html