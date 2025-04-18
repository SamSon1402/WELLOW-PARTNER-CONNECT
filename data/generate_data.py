import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

def generate_wellow_locations():
    """Generate synthetic data for Wellow locations in Paris"""
    locations = [
        {"Name": "Wellow Paris 13th", "Address": "25 Rue du Château des Rentiers, 75013 Paris", "Latitude": 48.8267, "Longitude": 2.3679},
        {"Name": "Wellow Paris 15th", "Address": "123 Rue de Vaugirard, 75015 Paris", "Latitude": 48.8417, "Longitude": 2.3197},
        {"Name": "Wellow Montreuil", "Address": "45 Rue de Paris, 93100 Montreuil", "Latitude": 48.8582, "Longitude": 2.4344},
        {"Name": "Wellow Saint-Denis", "Address": "12 Place Victor Hugo, 93200 Saint-Denis", "Latitude": 48.9361, "Longitude": 2.3556},
        {"Name": "Wellow Paris 11th", "Address": "78 Boulevard Voltaire, 75011 Paris", "Latitude": 48.8643, "Longitude": 2.3783}
    ]
    return pd.DataFrame(locations)

def generate_partners(n=75):
    """Generate synthetic data for potential partners"""
    partner_types = ["University", "Corporate", "Relocation Agency", "Language School", "Association"]
    statuses = ["Identified", "Contacted", "Meeting Scheduled", "Active Partner", "Inactive"]
    values = ["High", "Medium", "Low"]
    
    data = []
    for i in range(n):
        partner_type = random.choice(partner_types)
        data.append({
            "PartnerName": f"Partner {i+1}",
            "PartnerType": partner_type,
            "Address": f"{random.randint(1, 150)} Avenue de Paris, 750{random.randint(10, 20)} Paris",
            "EstimatedReach": random.randint(100, 5000),
            "Latitude": 48.85 + random.uniform(-0.1, 0.1),
            "Longitude": 2.35 + random.uniform(-0.1, 0.1),
            "ContactStatus": random.choice(statuses),
            "PotentialValue": random.choice(values),
            "LastContactDate": (datetime.now() - timedelta(days=random.randint(0, 90))).strftime('%Y-%m-%d')
        })
    return pd.DataFrame(data)

if __name__ == "__main__":
    # Generate and save data
    wellow_locations = generate_wellow_locations()
    wellow_locations.to_csv('data/wellow_locations.csv', index=False)
    print(f"Generated {len(wellow_locations)} Wellow locations")
    
    partners = generate_partners(75)
    partners.to_csv('data/partners.csv', index=False)
    print(f"Generated {len(partners)} potential partners")