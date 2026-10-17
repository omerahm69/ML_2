import streamlit as st
import matplotlib.pyplot as plt

def page_project_hypothesis_body():
    st.write("### Project Hypothesis and Validation")

    st.success("""
    * **Hypothesis:** A deep learning model, particularly a Convolutional Neural Network (CNN), can effectively classify 2D sagittal-view ultrasound images into standard images and non-stadard plane which is a key step for NT measurement and Down Syndrome assessment.

    * **Rationale:**The task is first-trimester (11-14 weeks) midsagittal views for NT measurement.“Standard” here means a properly angled midsagittal profile where the fine structures are visible and the NT can be measured reliably. “Non-standard” is therefore mostly a subtle quality or positioning difference within the same view, not a different anatomical plane.

    * **Validation Approach:**
        - A balanced dataset was used with sufficient examples of both classes.
        - Transfer learning techniques were applied to improve model
            performance.

    * **Observations:**
        - Image montages suggest distinguishable visual patterns between
            standard and non-standard ultrasound images.
        - However, statistical analyses such as average image, variability
            image, and difference between class averages did not reveal a distnictt pattern.
    """)