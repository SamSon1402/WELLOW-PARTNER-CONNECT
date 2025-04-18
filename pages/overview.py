import streamlit as st
from components.metrics import display_metrics
from components.charts import display_partner_charts

def display_overview_page(wellow_locations, filtered_partners):
    """Display the partner overview page"""
    # Section header
    st.markdown('<div class="section-header">> PARTNER OVERVIEW</div>', unsafe_allow_html=True)
    
    # Key metrics
    display_metrics(st, filtered_partners)
    
    # Partner distribution charts
    display_partner_charts(st, filtered_partners)