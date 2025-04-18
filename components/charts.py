import plotly.express as px

def get_partner_type_color(partner_type):
    """Return color for partner type"""
    colors = {
        "University": "#FF5555",
        "Corporate": "#FF0000",
        "Relocation Agency": "#FF3333",
        "Language School": "#CC0000",
        "Association": "#FF8888"
    }
    return colors.get(partner_type, "#FF0000")

def pixel_bar_chart(data, x_col, y_col, title, color_col=None):
    """Create a retro-styled bar chart"""
    if color_col:
        fig = px.bar(
            data, x=x_col, y=y_col, 
            title=title,
            color=color_col,
            color_discrete_map={k: get_partner_type_color(k) for k in data[color_col].unique()}
        )
    else:
        fig = px.bar(
            data, x=x_col, y=y_col, 
            title=title,
            color_discrete_sequence=["#FF0000"]
        )
    
    # Update layout for retro gaming feel
    fig.update_layout(
        font_family="VT323",
        title_font_size=24,
        title_font_family="VT323",
        title_x=0.5,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0.05)',
        xaxis=dict(
            title_font_family="VT323",
            tickfont_family="VT323",
        ),
        yaxis=dict(
            title_font_family="VT323",
            tickfont_family="VT323",
        )
    )
    
    # Make bars look more "pixel-like"
    fig.update_traces(marker_line_width=2, marker_line_color="black", opacity=0.8)
    
    return fig

def display_partner_charts(st, filtered_partners):
    """Display partner distribution charts"""
    chart_col1, chart_col2 = st.columns(2)
    
    with chart_col1:
        st.markdown('<div class="chart-container">', unsafe_allow_html=True)
        
        # Partner type distribution
        partner_type_counts = filtered_partners['PartnerType'].value_counts().reset_index()
        partner_type_counts.columns = ['PartnerType', 'Count']
        
        fig = pixel_bar_chart(
            partner_type_counts,
            'PartnerType',
            'Count',
            'PARTNER TYPE DISTRIBUTION',
            'PartnerType'
        )
        st.plotly_chart(fig, use_container_width=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    with chart_col2:
        st.markdown('<div class="chart-container">', unsafe_allow_html=True)
        
        # Reach by partner type
        reach_by_type = filtered_partners.groupby('PartnerType')['EstimatedReach'].sum().reset_index()
        
        fig = pixel_bar_chart(
            reach_by_type,
            'PartnerType',
            'EstimatedReach',
            'ESTIMATED REACH BY PARTNER TYPE',
            'PartnerType'
        )
        st.plotly_chart(fig, use_container_width=True)
        
        st.markdown('</div>', unsafe_allow_html=True)