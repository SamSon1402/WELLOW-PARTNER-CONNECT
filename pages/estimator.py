import streamlit as st
import plotly.express as px
from utils.estimator import display_lead_estimator

def display_estimator_page(filtered_partners):
    """Display the lead generation estimator page"""
    leads_by_type, total_estimated_leads = display_lead_estimator(st, filtered_partners)
    
    # Display results
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
            color_discrete_sequence=["#FF0000", "#FF3333", "#FF5555", "#FF7777", "#FF9999"]
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Display the total in a game-like score display
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