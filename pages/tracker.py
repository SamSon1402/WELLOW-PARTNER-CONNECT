import streamlit as st
from components.tables import display_partnership_tracker

def display_tracker_page(filtered_partners):
    """Display the partnership tracker page"""
    display_partnership_tracker(st, filtered_partners)