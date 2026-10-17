
import streamlit as st
import pandas as pd
import pickle

from pathlib import Path

# Project root: C:\python_projects\ML_2
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Output directory
OUTPUT_ROOT = PROJECT_ROOT / "outputs"


def load_test_evaluation(version):
    """Load saved CNN test evaluation."""

    path = OUTPUT_ROOT / version / "evaluation.pkl"

    if not path.is_file():
        return None

    with open(path, "rb") as file:
        return pickle.load(file)


def display_image(filename, caption, version="v1"):
    """Display an image if it exists."""

    image_path = OUTPUT_ROOT / version / filename

    if image_path.is_file():
        st.image(
            str(image_path),
            caption=caption,
            use_container_width=True
        )
    else:
        st.warning(f"Image not found: {image_path}")


def page_ML_performance_body():

    version = "v1"

    st.title("CNN Model Performance")

    # ---------------------------------
    # 1. Labels distribution
    # ---------------------------------

    st.write(
        "### Train, Validation and Test Set: Labels Frequencies"
    )

    display_image(
        "labels_distribution.png",
        "Labels Distribution on Train, Validation and Test Sets",
        version
    )

    st.divider()

    # ---------------------------------
    # 2. Training history
    # ---------------------------------

    st.write("### Model History")

    col1, col2 = st.columns(2)

    with col1:
        display_image(
            "model_training_acc.png",
            "Model Training Accuracy",
            version
        )

    with col2:
        display_image(
            "model_training_losses.png",
            "Model Training Losses",
            version
        )

    st.divider()

    # ---------------------------------
    # 3. Test evaluation
    # ---------------------------------

    st.write("### Generalised Performance on Test Set")

    evaluation = load_test_evaluation(version)

    if evaluation is not None:

        if isinstance(evaluation, dict):
            df = pd.DataFrame(
                list(evaluation.items()),
                columns=["Metric", "Value"]
            )

        else:
            df = pd.DataFrame({
                "Metric": ["Loss", "Accuracy"],
                "Value": evaluation
            })

        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True
        )

    else:
        st.warning(
            "Test evaluation not found. "
            "Evaluate the CNN on the test set and save evaluation.pkl."
        )
