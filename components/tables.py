def get_status_emoji(status):
    """Return emoji for contact status"""
    emoji_map = {
        "Identified": "🔍",
        "Contacted": "📧",
        "Meeting Scheduled": "📅",
        "Active Partner": "🌟",
        "Inactive": "💤"
    }
    return emoji_map.get(status, "❓")

def style_dataframe(df):
    """Apply retro styling to dataframe"""
    # Calculate the color intensities based on values
    styled_df = df.style.apply(lambda x: ['background-color: rgba(255, 0, 0, 0.1)' 
                                         if x.name % 2 == 0 else 
                                         'background-color: rgba(255, 0, 0, 0.2)' for i in x], 
                             axis=1)
    
    # Highlight PotentialValue column
    styled_df = styled_df.apply(lambda x: [f'background-color: {"#FF5555" if val == "High" else "#FF8888" if val == "Medium" else "#FFBBBB"}; color: white' 
                                         if i == df.columns.get_loc('PotentialValue') else '' 
                                         for i, val in enumerate(x)], 
                             axis=1)
    
    return styled_df

def display_partnership_tracker(st, filtered_partners):
    """Display the partnership tracker table"""
    st.markdown('<div class="section-header">> PARTNERSHIP TRACKER</div>', unsafe_allow_html=True)
    
    # Display the partnership table
    columns_to_display = ['PartnerName', 'PartnerType', 'EstimatedReach', 'ContactStatus', 'PotentialValue', 'LastContactDate']
    display_df = filtered_partners[columns_to_display].copy()
    
    # Add emoji indicators for status
    display_df['ContactStatus'] = display_df['ContactStatus'].apply(lambda x: f"{get_status_emoji(x)} {x}")
    
    # Style the dataframe
    st.dataframe(
        style_dataframe(display_df),
        use_container_width=True,
        height=400
    )