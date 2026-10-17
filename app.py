
import streamlit as st

from app_pages.multipages import MultiPage

st.set_page_config(
    page_title="First-trimester (11–14 weeks) midsagittal views for NT measurement",
    page_icon="🍒",
    layout="wide"
)

# Import application pages
from app_pages.page_summary import page_summary_body
from app_pages.page_visual_study_findings import page_visual_study_finding_body
from app_pages.page_hypothesis import page_project_hypothesis_body
from app_pages.page_ML_performance import page_ML_performance_body
from app_pages.page_live_predictions import page_live_predictions_body

# Initialize multipage application
app = MultiPage(app_name="")

# Register pages
app.add_page("Quick Project Summary", page_summary_body)
app.add_page("Project Hypothesis", page_project_hypothesis_body)
app.add_page("Visual Study Findings", page_visual_study_finding_body)
app.add_page("ML Performance", page_ML_performance_body)
app.add_page("Live Predictions", page_live_predictions_body)

# Launch application
app.run()
