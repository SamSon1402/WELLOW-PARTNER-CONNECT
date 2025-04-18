import plotly.graph_objects as go

def create_plotly_map(wellow_df, partners_df, filtered_types=None):
    """Create a plotly map with Wellow locations and partners"""
    # Filter partners by type if specified
    if filtered_types and len(filtered_types) > 0:
        filtered_partners = partners_df[partners_df['PartnerType'].isin(filtered_types)]
    else:
        filtered_partners = partners_df
    
    # Create base map
    fig = go.Figure()
    
    # Add Wellow locations
    fig.add_trace(go.Scattermapbox(
        lat=wellow_df['Latitude'],
        lon=wellow_df['Longitude'],
        mode='markers',
        marker=dict(
            size=15,
            color='#E5174D',  # Wellow pink
            opacity=0.8,
            symbol='circle'
        ),
        text=wellow_df['Name'],
        hoverinfo='text',
        name='Wellow Locations'
    ))
    
    # Add partners by type
    for partner_type in filtered_partners['PartnerType'].unique():
        type_partners = filtered_partners[filtered_partners['PartnerType'] == partner_type]
        
        # Get color for partner type
        color = {
            "University": "#FF5555",
            "Corporate": "#FF0000",
            "Relocation Agency": "#FF3333",
            "Language School": "#CC0000",
            "Association": "#FF8888"
        }.get(partner_type, "#FF0000")
        
        fig.add_trace(go.Scattermapbox(
            lat=type_partners['Latitude'],
            lon=type_partners['Longitude'],
            mode='markers',
            marker=dict(
                size=10,
                color=color,
                opacity=0.7,
            ),
            text=type_partners.apply(lambda row: f"{row['PartnerName']}<br>Type: {row['PartnerType']}<br>Reach: {row['EstimatedReach']}", axis=1),
            hoverinfo='text',
            name=partner_type
        ))
    
    # Update map layout
    fig.update_layout(
        mapbox_style="carto-darkmatter",
        mapbox=dict(
            center=dict(lat=48.8566, lon=2.3522),  # Paris center
            zoom=11
        ),
        margin=dict(l=0, r=0, t=0, b=0),
        legend=dict(
            font=dict(family="VT323", size=14),
            bgcolor="rgba(0,0,0,0.5)",
            bordercolor="#FFCC33",
            borderwidth=2
        ),
        height=600
    )
    
    return fig

def display_partner_map(st, wellow_locations, filtered_partners, selected_types):
    """Display the partner map section"""
    st.markdown('<div class="section-header">> PARTNER MAP</div>', unsafe_allow_html=True)
    
    # Create and display map
    map_fig = create_plotly_map(wellow_locations, filtered_partners, selected_types)
    st.plotly_chart(map_fig, use_container_width=True)