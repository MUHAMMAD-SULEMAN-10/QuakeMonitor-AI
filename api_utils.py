# api_utils.py
import pandas as pd

def fetch_earthquakes(min_magnitude, hours, region_bbox=None, detailed=False):
    # Dummy empty DataFrame
    return pd.DataFrame({
        'time': [], 'place': [], 'magnitude': [], 'depth': [],
        'magnitude_category': [], 'risk_level': [], 'time_ago': [], 'url': []
    })

def get_groq_summary(prompt):
    return "🤖 AI Summary will appear here."
