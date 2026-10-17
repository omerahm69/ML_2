import streamlit as st
import matplotlib.pyplot as plt


def page_visual_study_finding_body():

    st.write("### Visual Study Findings")

    st.info ( f"""**Visual Study Findings**\n
        * After analyzing the dataset, here are the findings to visually differentiate a Standard and Non-Standard ultrasound images:
            - Standard images show clear visibility of fine structures and allow reliable NT measurement.
            - Non-standard images exhibit subtle quality or positioning differences within the same view. * """
)
    st.write("---")
    st.write("### Sample Images")

    col1, col2 = st.columns(2)
    with col1:
        st.image("./jupyter_notebooks/outputs/v1/avg_var_standard.png", caption="Standard Ultrasound Image", use_container_width=True)
    with col2:
        st.image("./jupyter_notebooks/outputs/v1/avg_var_non_standard.png", caption="Non-Standard Ultrasound Image", use_container_width=True)
    st.write("---")
    st.write("### Image Analysis Techniques")

    st.markdown("""
    - **Image Montage**: Created to visually scan large numbers of 2D ultrasound images side-by-side.
    - **Average Image**: Shows the typical structure of each class (standard vs non-standard).
    - **Image Variability**: Highlights areas of inconsistency (noise, disease presence).
    - **Difference of Averages**: Emphasized faint patterns of non-standard images that are hard to spot in raw images.
    """)

    st.image("./jupyter_notebooks/outputs/v1/avg_diff.png", caption="Difference Between Average Standard and Non-Standard Ultrasound Images", use_container_width=True)