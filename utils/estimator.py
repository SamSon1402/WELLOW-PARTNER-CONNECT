import pandas as pd
import plotly.express as px

def calculate_estimated_leads(filtered_partners, target_partners):
    """Calculate estimated leads based on selected targets"""
    # Define hypothetical conversion rates
    conversion_rates = {
        "University": 0.02,  # 2% conversion rate
        "Corporate": 0.05,   # 5% conversion rate
        "Relocation Agency": 0.08,  # 8% conversion rate
        "Language School": 0.03,  # 3% conversion rate
        "Association": 0.01   # 1% conversion rate
    }
    
    # Calculate average reach by partner type
    avg_reach_by_type = filtered_partners.groupby('PartnerType')['EstimatedReach'].mean().to_dict()
    
    # Calculate leads by type and total
    total_estimated_leads = 0
    leads_by_type = {}
    
    for partner_type, target_count in target_partners.items():
        estimated_leads = target_count * avg_reach_by_type.get(partner_type, 0) * conversion_rates.get(partner_type, 0.01)
        leads_by_type[partner_type] = estimated_leads
        total_estimated_leads += estimated_leads
    
    return leads_by_type, total_estimated_leads

def display_lead_estimator(st, filtered_partners):
    """Display the lead generation estimator"""
    st.markdown('<div class="section-header">> LEAD GENERATION ESTIMATOR</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div style="font-family: 'Space Mono', monospace; background-color: rgba(255, 0, 0, 0.1); padding: 15px; border: 3px solid black; margin-bottom: 20px;">
        <p>Configure your partnership targets to estimate potential resident leads. 
        These calculations use hypothetical conversion rates for illustration purposes.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Create input sliders for each partner type
    col1, col2 = st.columns(2)
    
    partner_types = sorted(filtered_partners['PartnerType'].unique())
    target_partners = {}
    
    with col1:
        st.markdown('<div style="border: 3px solid black; padding: 15px; background-color: rgba(0,0,0,0.1);">', unsafe_allow_html=True)
        st.markdown('<h3 style="font-family: \'VT323\', monospace; font-size: 1.5rem;">TARGET PARTNERSHIPS</h3>', unsafe_allow_html=True)
        
        for partner_type in partner_types:
            max_partners = len(filtered_partners[filtered_partners['PartnerType'] == partner_type])
            target_partners[partner_type] = st.slider(
                f"{partner_type}",
                min_value=0,
                max_value=max_partners,
                value=max(1, max_partners//5),  # Default to 20%
                step=1
            )
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Calculate and display results
    leads_by_type, total_estimated_leads = calculate_estimated_leads(filtered_partners, target_partners)
    
    return leads_by_type, total_estimated_leads