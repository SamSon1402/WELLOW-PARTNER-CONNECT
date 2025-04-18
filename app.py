import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import random
from datetime import datetime, timedelta
import time
import os
import matplotlib.colors as mcolors
import matplotlib.pyplot as plt
import math

# Set page configuration
st.set_page_config(
    page_title="Wellow Partner Connect", 
    page_icon="🎮", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# ----- CUSTOM CSS FOR RETRO GAMING STYLE -----
retro_css = """
<style>
@import url('https://fonts.googleapis.com/css2?family=VT323&family=Press+Start+2P&family=Space+Mono:wght@400;700&display=swap');

:root {
    --wellow-pink: #E5174D;
    --wellow-yellow: #FFCC33;
    --retro-black: #0F0F0F;
    --retro-red: #FF0000;
    --retro-blue: #0000FF;
    --pixel-border: 4px solid black;
}

.main .block-container {
    padding-top: 2rem;
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

.game-button:hover {
    background-color: var(--wellow-pink);
    transform: scale(1.05);
}

/* Custom dataframe styling */
.retro-dataframe {
    font-family: 'Space Mono', monospace;
    border: var(--pixel-border);
}

.retro-dataframe th {
    background-color: var(--retro-red);
    color: white;
    font-weight: bold;
    padding: 10px;
}

.retro-dataframe td {
    padding: 8px;
    border: 2px solid black;
}

.retro-dataframe tr:nth-child(even) {
    background-color: rgba(255, 204, 51, 0.2);
}

/* Sidebar styling */
.css-1d391kg, .css-163ttbj {
    background-color: var(--retro-black);
}

.sidebar .sidebar-content {
    background-color: var(--retro-black);
    color: white;
}

section[data-testid="stSidebar"] {
    background-color: var(--retro-black);
    border-right: var(--pixel-border);
    padding: 1rem;
}

section[data-testid="stSidebar"] .stSelectbox label, 
section[data-testid="stSidebar"] .stMultiSelect label,
section[data-testid="stSidebar"] .stSlider label {
    font-family: 'VT323', monospace;
    font-size: 1.5rem;
    color: var(--wellow-yellow);
}

/* Slider styling */
.stSlider > div > div {
    background-color: var(--wellow-pink) !important;
}

/* Expander styling */
.streamlit-expanderHeader {
    font-family: 'VT323', monospace;
    font-size: 1.3rem;
    background-color: rgba(255, 0, 0, 0.2);
    border: 2px solid var(--retro-black);
}

/* Chart container */
.chart-container {
    border: var(--pixel-border);
    padding: 10px;
    background-color: rgba(255, 255, 255, 0.1);
    margin-bottom: 15px;
}

/* For the game loading effect */
.loading-text {
    font-family: 'Press Start 2P', monospace;
    font-size: 1.5rem;
    color: var(--wellow-yellow);
    text-align: center;
    margin: 20px 0;
    animation: blink 1s infinite;
}

@keyframes blink {
    0% { opacity: 1; }
    50% { opacity: 0; }
    100% { opacity: 1; }
}

/* Text styling */
p, div, span {
    font-family: 'Space Mono', monospace;
}

h1, h2, h3, h4, h5, h6 {
    font-family: 'VT323', monospace;
}

/* Chart title styling */
.plotly .gtitle {
    font-family: 'VT323', monospace !important;
    font-size: 1.5rem !important;
}

/* Tooltip styling */
.tooltip {
    position: relative;
    display: inline-block;
    cursor: help;
}

.tooltip .tooltiptext {
    font-family: 'Space Mono', monospace;
    visibility: hidden;
    width: 200px;
    background-color: var(--retro-black);
    color: #fff;
    text-align: center;
    border: 2px solid var(--wellow-yellow);
    padding: 5px;
    position: absolute;
    z-index: 1;
    bottom: 125%;
    left: 50%;
    margin-left: -100px;
    opacity: 0;
    transition: opacity 0.3s;
}

.tooltip:hover .tooltiptext {
    visibility: visible;
    opacity: 1;
}

/* Pixelated logo styling */
.pixel-logo {
    image-rendering: pixelated;
    image-rendering: -moz-crisp-edges;
    image-rendering: crisp-edges;
    border: var(--pixel-border);
}

</style>
"""
st.markdown(retro_css, unsafe_allow_html=True)

# ----- HELPER FUNCTIONS -----

def load_wellow_logo():
    logo_path = './assets/wellow_logo.png'
    if os.path.exists(logo_path):
        logo_html = f"""
        <div style="display: flex; justify-content: center; margin-bottom: 20px;">
            <img src="./assets/wellow_logo.png" class="pixel-logo" alt="Wellow Logo" width="150px">
        </div>
        """
    else:
        # Fallback if logo not found
        logo_html = """
        <div style="display: flex; justify-content: center; margin-bottom: 20px;">
            <div style="background-color: #E5174D; width: 150px; height: 150px; display: flex; 
                        justify-content: center; align-items: center; border: 4px solid black;">
                <span style="font-family: 'Press Start 2P'; color: #FFCC33; font-size: 60px;">W</span>
            </div>
        </div>
        """
    return logo_html

def title_with_logo():
    st.markdown(load_wellow_logo(), unsafe_allow_html=True)
    st.markdown('<div class="custom-title">WELLOW PARTNER CONNECT</div>', unsafe_allow_html=True)
    st.markdown('<div style="text-align: center; font-family: \'Press Start 2P\'; font-size: 16px; margin-bottom: 30px;">STRATEGIC PARTNERSHIP DASHBOARD</div>', unsafe_allow_html=True)

def section_header(title):
    st.markdown(f'<div class="section-header">> {title}</div>', unsafe_allow_html=True)

def metric_card(title, value, column):
    column.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">{title}</div>
        <div class="metric-value">{value}</div>
    </div>
    """, unsafe_allow_html=True)

def game_button(label, key=None):
    button_html = f"""
    <div class="game-button" id="{key if key else ''}">
        {label}
    </div>
    """
    return button_html

def get_partner_type_color(partner_type):
    colors = {
        "University": "#FF5555",  # Red
        "Corporate": "#FF0000",   # Bright Red
        "Relocation Agency": "#FF3333",  # Slightly different red
        "Language School": "#CC0000",  # Darker red
        "Association": "#FF8888"  # Lighter red
    }
    return colors.get(partner_type, "#FF0000")  # Default to red if type not found

def get_status_emoji(status):
    emoji_map = {
        "Identified": "🔍",
        "Contacted": "📧",
        "Meeting Scheduled": "📅",
        "Active Partner": "🌟",
        "Inactive": "💤"
    }
    return emoji_map.get(status, "❓")

def style_dataframe(df):
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

def pixel_bar_chart(data, x_col, y_col, title, color_col=None):
    # Create a standard bar chart
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
            color_discrete_sequence=["#FF0000"]  # Default to red
        )
    
    # Update layout for retro gaming feel
    fig.update_layout(
        font_family="VT323",
        title_font_size=24,
        title_font_family="VT323",
        title_x=0.5,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0.05)',
        xaxis_title_font_size=18,
        yaxis_title_font_size=18,
        legend_title_font_size=18,
        xaxis=dict(
            title_font_family="VT323",
            tickfont_family="VT323",
            tickfont_size=14,
            gridcolor='rgba(0,0,0,0.1)',
        ),
        yaxis=dict(
            title_font_family="VT323",
            tickfont_family="VT323",
            tickfont_size=14,
            gridcolor='rgba(0,0,0,0.1)',
        ),
        legend=dict(
            font_family="VT323",
            font_size=14
        ),
        margin=dict(l=40, r=40, t=60, b=40),
    )
    
    # Make bars look more "pixel-like"
    fig.update_traces(marker_line_width=2, marker_line_color="black", opacity=0.8)
    
    return fig

def pixel_pie_chart(data, names, values, title):
    # Create a standard pie chart
    fig = px.pie(
        data, names=names, values=values, 
        title=title,
        color_discrete_sequence=[get_partner_type_color(pt) for pt in data[names].unique()]
    )
    
    # Update layout for retro gaming feel
    fig.update_layout(
        font_family="VT323",
        title_font_size=24,
        title_font_family="VT323",
        title_x=0.5,
        paper_bgcolor='rgba(0,0,0,0)',
        legend=dict(
            font_family="VT323",
            font_size=14
        ),
        margin=dict(l=40, r=40, t=60, b=40),
    )
    
    # Make pie look more "pixel-like"
    fig.update_traces(marker_line_width=2, marker_line_color="black")
    
    return fig

def create_plotly_map(wellow_df, partners_df, filtered_types=None):
    # Filter partners by type if specified
    if filtered_types and len(filtered_types) > 0:
        filtered_partners = partners_df[partners_df['PartnerType'].isin(filtered_types)]
    else:
        filtered_partners = partners_df
    
    # Create base map using Plotly
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
    
    # Add partners with colors by type
    for partner_type in filtered_partners['PartnerType'].unique():
        type_partners = filtered_partners[filtered_partners['PartnerType'] == partner_type]
        
        fig.add_trace(go.Scattermapbox(
            lat=type_partners['Latitude'],
            lon=type_partners['Longitude'],
            mode='markers',
            marker=dict(
                size=10,
                color=get_partner_type_color(partner_type),
                opacity=0.7,
            ),
            text=type_partners.apply(lambda row: f"{row['PartnerName']}<br>Type: {row['PartnerType']}<br>Reach: {row['EstimatedReach']}<br>Status: {row['ContactStatus']}", axis=1),
            hoverinfo='text',
            name=partner_type
        ))
    
    # Update map layout
    fig.update_layout(
        mapbox_style="carto-darkmatter",  # Dark theme for retro feel
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

def loading_effect():
    loading_placeholder = st.empty()
    progress_placeholder = st.empty()
    
    loading_placeholder.markdown('<div class="loading-text">LOADING GAME DATA...</div>', unsafe_allow_html=True)
    progress_bar = progress_placeholder.progress(0)
    
    for i in range(101):
        progress_bar.progress(i)
        time.sleep(0.01)
    
    loading_placeholder.markdown('<div class="loading-text">PRESS START!</div>', unsafe_allow_html=True)
    time.sleep(1)
    loading_placeholder.empty()
    progress_placeholder.empty()

# ----- LOAD DATA -----
try:
    # Updated file paths for Google Colab with tunnel
    wellow_locations = pd.read_csv('/content/wellow_locations.csv')
    partners = pd.read_csv('/content/partners.csv')
    
    # Print confirmation message
    st.sidebar.success("Data loaded successfully!")
except FileNotFoundError as e:
    st.error(f"Data files not found: {str(e)}")
    st.error("Please make sure the data files exist at /content/wellow_locations.csv and /content/partners.csv")
    st.stop()

# ----- SIDEBAR -----
with st.sidebar:
    st.markdown('<h1 style="font-family: \'Press Start 2P\', monospace; color: #FFCC33; font-size: 1rem; text-align: center; margin-bottom: 20px;">WELLOW CONTROL PANEL</h1>', unsafe_allow_html=True)
    
    # Add retro gaming "press start" effect
    st.markdown('<div style="text-align: center; margin-bottom: 20px;">', unsafe_allow_html=True)
    st.markdown(game_button("PRESS START", "start-button"), unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Partner type filter
    st.markdown('<h2 style="font-family: \'VT323\', monospace; color: #FFCC33; font-size: 1.5rem;">SELECT PARTNER TYPE</h2>', unsafe_allow_html=True)
    partner_types = sorted(partners['PartnerType'].unique())
    selected_types = st.multiselect("", partner_types, default=partner_types, label_visibility="collapsed")
    
    # Contact status filter
    st.markdown('<h2 style="font-family: \'VT323\', monospace; color: #FFCC33; font-size: 1.5rem;">SELECT STATUS</h2>', unsafe_allow_html=True)
    contact_statuses = sorted(partners['ContactStatus'].unique())
    selected_statuses = st.multiselect("", contact_statuses, default=contact_statuses, label_visibility="collapsed")
    
    # Potential value filter
    st.markdown('<h2 style="font-family: \'VT323\', monospace; color: #FFCC33; font-size: 1.5rem;">SELECT VALUE</h2>', unsafe_allow_html=True)
    potential_values = ["High", "Medium", "Low"]
    selected_values = st.multiselect("", potential_values, default=potential_values, label_visibility="collapsed")
    
    # Reset filters button
    st.markdown('<div style="text-align: center; margin-top: 20px;">', unsafe_allow_html=True)
    reset_button = st.button("RESET FILTERS", key="reset_filters")
    st.markdown('</div>', unsafe_allow_html=True)
    
    if reset_button:
        selected_types = partner_types
        selected_statuses = contact_statuses
        selected_values = potential_values

# Apply filters
filtered_partners = partners[
    partners['PartnerType'].isin(selected_types) &
    partners['ContactStatus'].isin(selected_statuses) &
    partners['PotentialValue'].isin(selected_values)
]

# ----- MAIN PAGE -----
title_with_logo()

# Display a "loading game" effect for fun
# Uncomment if you want the loading effect
# loading_effect()

# ----- PARTNER OVERVIEW SECTION -----
section_header("PARTNER OVERVIEW")

# Key metrics
col1, col2, col3, col4 = st.columns(4)
metric_card("TOTAL PARTNERS", len(filtered_partners), col1)
metric_card("TOTAL REACH", f"{filtered_partners['EstimatedReach'].sum():,}", col2)
metric_card("ACTIVE PARTNERS", len(filtered_partners[filtered_partners['ContactStatus'] == 'Active Partner']), col3)
metric_card("HIGH VALUE", len(filtered_partners[filtered_partners['PotentialValue'] == 'High']), col4)

# Charts for partner distribution
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

# Additional charts
chart_col3, chart_col4 = st.columns(2)

with chart_col3:
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    
    # Status distribution pie chart
    status_counts = filtered_partners['ContactStatus'].value_counts().reset_index()
    status_counts.columns = ['ContactStatus', 'Count']
    
    fig = px.pie(
        status_counts, 
        names='ContactStatus', 
        values='Count',
        title='PARTNER STATUS DISTRIBUTION',
        color_discrete_sequence=["#FF0000", "#FF3333", "#FF6666", "#FF9999", "#FFCCCC"]
    )
    
    # Update layout for retro gaming feel
    fig.update_layout(
        font_family="VT323",
        title_font_size=24,
        title_font_family="VT323",
        title_x=0.5,
        paper_bgcolor='rgba(0,0,0,0)',
        legend=dict(
            font_family="VT323",
            font_size=14
        )
    )
    
    # Make pie look more "pixel-like"
    fig.update_traces(marker_line_width=2, marker_line_color="black")
    
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

with chart_col4:
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    
    # Potential value distribution
    value_counts = filtered_partners['PotentialValue'].value_counts().reset_index()
    value_counts.columns = ['PotentialValue', 'Count']
    
    # Ensure High, Medium, Low order
    value_order = {"High": 3, "Medium": 2, "Low": 1}
    value_counts['Order'] = value_counts['PotentialValue'].map(value_order)
    value_counts = value_counts.sort_values('Order', ascending=False).drop('Order', axis=1)
    
    fig = pixel_bar_chart(
        value_counts,
        'PotentialValue',
        'Count',
        'POTENTIAL VALUE DISTRIBUTION'
    )
    
    # Assign specific red shades
    fig.update_traces(marker_color=["#FF0000", "#FF5555", "#FF9999"])
    
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

# ----- PARTNER MAP SECTION -----
section_header("PARTNER MAP")

# Create and display the map
map_fig = create_plotly_map(wellow_locations, filtered_partners, selected_types)
st.plotly_chart(map_fig, use_container_width=True)

# ----- LEAD GENERATION ESTIMATOR -----
section_header("LEAD GENERATION ESTIMATOR")

st.markdown("""
<div style="font-family: 'Space Mono', monospace; background-color: rgba(255, 0, 0, 0.1); padding: 15px; border: 3px solid black; margin-bottom: 20px;">
    <p>Configure your partnership targets to estimate potential resident leads. 
    These calculations use hypothetical conversion rates for illustration purposes.</p>
</div>
""", unsafe_allow_html=True)

# Define hypothetical conversion rates
conversion_rates = {
    "University": 0.02,  # 2% of university reach might become leads
    "Corporate": 0.05,   # 5% of corporate reach might become leads
    "Relocation Agency": 0.08,  # 8% of relocation agency reach might become leads
    "Language School": 0.03,  # 3% of language school reach might become leads
    "Association": 0.01   # 1% of association reach might become leads
}

# Calculate average reach by partner type
avg_reach_by_type = filtered_partners.groupby('PartnerType')['EstimatedReach'].mean().to_dict()

# Create input sliders for each partner type
col1, col2 = st.columns(2)

target_partners = {}
with col1:
    st.markdown('<div style="border: 3px solid black; padding: 15px; background-color: rgba(0,0,0,0.1);">', unsafe_allow_html=True)
    st.markdown('<h3 style="font-family: \'VT323\', monospace; font-size: 1.5rem;">TARGET PARTNERSHIPS</h3>', unsafe_allow_html=True)
    
    for partner_type in sorted(partner_types):
        max_partners = len(partners[partners['PartnerType'] == partner_type])
        target_partners[partner_type] = st.slider(
            f"{partner_type}",
            min_value=0,
            max_value=max_partners,
            value=max(1, max_partners//5),  # Default to 20% of available partners
            step=1
        )
    
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div style="border: 3px solid black; padding: 15px; background-color: rgba(0,0,0,0.1);">', unsafe_allow_html=True)
    st.markdown('<h3 style="font-family: \'VT323\', monospace; font-size: 1.5rem;">CONVERSION ASSUMPTIONS</h3>', unsafe_allow_html=True)
    
    for partner_type in sorted(partner_types):
        st.markdown(f"""
        <div style="display: flex; justify-content: space-between; font-family: 'Space Mono', monospace; margin-bottom: 10px;">
            <div>{partner_type}:</div>
            <div>{conversion_rates[partner_type]*100:.1f}% conversion rate</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown('<div style="font-size: 0.8rem; margin-top: 15px;">* These conversion rates are hypothetical estimates for demo purposes</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Calculate estimated leads
total_estimated_leads = 0
leads_by_type = {}

for partner_type in partner_types:
    estimated_leads = target_partners[partner_type] * avg_reach_by_type.get(partner_type, 0) * conversion_rates[partner_type]
    leads_by_type[partner_type] = estimated_leads
    total_estimated_leads += estimated_leads

# Display the results
st.markdown('<div style="border: 3px solid black; padding: 15px; background-color: rgba(255,0,0,0.15); margin-top: 20px;">', unsafe_allow_html=True)
st.markdown('<h3 style="font-family: \'VT323\', monospace; font-size: 1.5rem; text-align: center;">ESTIMATED ANNUAL LEADS</h3>', unsafe_allow_html=True)

col1, col2 = st.columns([2, 1])

with col1:
    # Create a horizontal bar chart for leads by partner type
    leads_df = pd.DataFrame({
        'PartnerType': list(leads_by_type.keys()),
        'EstimatedLeads': list(leads_by_type.values())
    })
    leads_df = leads_df.sort_values('EstimatedLeads', ascending=True)
    
    fig = px.bar(
        leads_df, 
        y='PartnerType',
        x='EstimatedLeads',
        orientation='h',
        title='ESTIMATED LEADS BY PARTNER TYPE',
        color='PartnerType',
        color_discrete_map={k: get_partner_type_color(k) for k in leads_df['PartnerType']}
    )
    
    # Update layout for retro gaming feel
    fig.update_layout(
        font_family="VT323",
        title_font_size=20,
        title_font_family="VT323",
        title_x=0.5,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        xaxis_title="Estimated Leads",
        yaxis_title="",
        xaxis=dict(
            title_font_family="VT323",
            tickfont_family="VT323",
            tickfont_size=14,
            gridcolor='rgba(0,0,0,0.1)'
        ),
        yaxis=dict(
            title_font_family="VT323",
            tickfont_family="VT323",
            tickfont_size=14
        ),
        margin=dict(l=10, r=10, t=40, b=10),
        showlegend=False
    )
    
    # Make bars look more "pixel-like"
    fig.update_traces(marker_line_width=2, marker_line_color="black")
    
    st.plotly_chart(fig, use_container_width=True)

with col2:
    # Display the total in a big, game-like score display
    st.markdown(f"""
    <div style="
        font-family: 'Press Start 2P', monospace; 
        font-size: 3rem; 
        text-align: center; 
        background-color: black; 
        color: #FF0000; 
        padding: 20px; 
        border: 4px solid #FFCC33;
        margin-top: 40px;
    ">
        {int(total_estimated_leads)}
    </div>
    <div style="text-align: center; font-family: 'VT323', monospace; font-size: 1.5rem; margin-top: 10px;">
        TOTAL LEADS
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# ----- PARTNERSHIP TRACKER -----
section_header("PARTNERSHIP TRACKER")

# Display the partnership table
columns_to_display = ['PartnerName', 'PartnerType', 'EstimatedReach', 'ContactStatus', 'PotentialValue', 'LastContactDate', 'NextAction']
display_df = filtered_partners[columns_to_display].copy()

# Add emoji indicators for status
display_df['ContactStatus'] = display_df['ContactStatus'].apply(lambda x: f"{get_status_emoji(x)} {x}")

# Style the dataframe
st.dataframe(
    style_dataframe(display_df),
    use_container_width=True,
    height=400
)

# ----- FOOTER -----
st.markdown("""
<div style="margin-top: 50px; text-align: center; font-family: 'Press Start 2P', monospace; font-size: 0.7rem; color: gray;">
    WELLOW PARTNER CONNECT - RETRO EDITION © 2025
</div>
""", unsafe_allow_html=True)