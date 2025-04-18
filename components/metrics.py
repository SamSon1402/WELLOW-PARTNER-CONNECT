def metric_card(title, value, column):
    """Create a retro-styled metric card"""
    column.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">{title}</div>
        <div class="metric-value">{value}</div>
    </div>
    """, unsafe_allow_html=True)

def display_metrics(st, filtered_partners):
    """Display all metric cards in a row"""
    col1, col2, col3, col4 = st.columns(4)
    
    # Calculate metrics
    total_partners = len(filtered_partners)
    total_reach = filtered_partners['EstimatedReach'].sum()
    active_partners = len(filtered_partners[filtered_partners['ContactStatus'] == 'Active Partner'])
    high_value = len(filtered_partners[filtered_partners['PotentialValue'] == 'High'])
    
    # Display metrics
    metric_card("TOTAL PARTNERS", total_partners, col1)
    metric_card("TOTAL REACH", f"{total_reach:,}", col2)
    metric_card("ACTIVE PARTNERS", active_partners, col3)
    metric_card("HIGH VALUE", high_value, col4)