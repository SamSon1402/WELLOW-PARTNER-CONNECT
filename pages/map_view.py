import streamlit as st
from components.maps import display_partner_map

def display_map_page(wellow_locations, filtered_partners, selected_types):
    """Display the geospatial map page"""
    display_partner_map(st, wellow_locations, filtered_partners, selected_types)