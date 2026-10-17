import streamlit as st
import matplotlib.pyplot as plt


import streamlit as st


def page_summary_body():

    st.write("### Quick Project Summary")

    st.info("""
    **General Information**

    This dataset contains 1528 2D sagittal-view ultrasound images
    of 1519 females collected from Shenzhen People's Hospital.

    Data was used for standard/non-standard (S-NS) plane
    classification, a key step for NT measurement and
    Down Syndrome assessment.

    Standard” here means a properly angled midsagittal profile where the
    fine structures are visible and the NT can be measured reliably.
    “Non-standard” is therefore mostly a subtle quality or positioning
    difference within the same view, not a different anatomical plane.

    An external dataset with 156 images from the Longhua branch
    of Shenzhen People's Hospital was also provided to test
    AI performance.

    Annotations for nine key structures are available in
    the ObjectDetection.xlsx file:

    - Thalami
    - Midbrain
    - Palate
    - 4th ventricle
    - Cisterna magna
    - Nuchal translucency (NT)
    - Nasal tip
    - Nasal skin
    - Nasal bone
    """)

    st.info("""
    **Project Goal**

    To investigate whether artificial intelligence can identify
    fetal intracranial structures during pregnancy weeks 11–14.

    Train a machine learning model to classify ultrasound
    images into two categories:

    1. **Standard**
    2. **Non-Standard**
    """)

    st.info("""
    **Project Dataset**

    The dataset used for this project is available on
    [Kaggle](https://www.kaggle.com/datasets/orvile/dataset-for-fetus-framework).
    """)

    st.write(
        "For additional information, please visit and **read** the "
        "[Project README file]"
        "(https://github.com/omerahm69/ML_2/blob/main/README.md)."
    )

    st.success("Project summary loaded successfully.")