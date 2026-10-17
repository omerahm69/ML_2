
import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import tensorflow as tf

from PIL import Image
from pathlib import Path


# ------------------------------------
# Configuration
# ------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent

MODEL_PATH = (
    PROJECT_ROOT
    / "jupyter_notebooks"
    / "outputs"
    / "v1"
    / "my_model.keras"
)

IMG_SIZE = (256, 256)

# Verify against the class mapping used during training
CLASS_NAMES = ["Non-Standard", "Standard"]


# ------------------------------------
# Load trained CNN
# ------------------------------------

@st.cache_resource
def load_model():

    if not MODEL_PATH.is_file():
        raise FileNotFoundError(
            f"Model file not found: {MODEL_PATH}"
        )

    model = tf.keras.models.load_model(
        str(MODEL_PATH),
        compile=False
    )

    return model


# ------------------------------------
# Image preprocessing
# ------------------------------------

def preprocess_image(img):

    img = img.convert("RGB")

    img = img.resize(
        IMG_SIZE,
        Image.Resampling.LANCZOS
    )

    img_array = np.asarray(
        img,
        dtype=np.float32
    )

    # Must match the preprocessing used during training
    img_array = img_array / 255.0

    input_tensor = np.expand_dims(
        img_array,
        axis=0
    )

    return input_tensor


# ------------------------------------
# CNN prediction
# ------------------------------------

def predict_image(model, input_tensor):

    prediction = model.predict(
        input_tensor,
        verbose=0
    )

    output = np.asarray(prediction[0]).flatten()

    if len(output) == 1:

        # Binary sigmoid output
        p_standard = float(output[0])

        if not np.isfinite(p_standard) or not 0 <= p_standard <= 1:
            raise ValueError("Invalid sigmoid output.")

        probabilities = np.array([
            1 - p_standard,
            p_standard
        ])

    elif len(output) == 2:

        # Two-class softmax output
        probabilities = output.astype(float)

        if (
            np.any(~np.isfinite(probabilities))
            or np.any(probabilities < 0)
            or not np.isclose(
                probabilities.sum(),
                1.0,
                atol=1e-3
            )
        ):
            raise ValueError(
                "Expected two valid class probabilities."
            )

    else:
        raise ValueError(
            f"Unexpected model output shape: {prediction.shape}"
        )

    predicted_index = int(np.argmax(probabilities))

    predicted_class = CLASS_NAMES[predicted_index]

    confidence = float(probabilities[predicted_index])

    return probabilities, predicted_class, confidence


# ------------------------------------
# Probability chart
# ------------------------------------

def plot_predictions_probabilities(probabilities):

    prob_df = pd.DataFrame({
        "Class": CLASS_NAMES,
        "Probability": probabilities
    })

    fig = px.bar(
        prob_df,
        x="Class",
        y="Probability",
        range_y=[0, 1.1],
        width=600,
        height=350,
        text="Probability",
        template="plotly_white"
    )

    fig.update_traces(
        texttemplate="%{text:.1%}",
        textposition="outside"
    )

    fig.update_layout(
        title="CNN Prediction Probabilities",
        xaxis_title="Ultrasound Image Classification",
        yaxis_title="Probability"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


# ------------------------------------
# Streamlit page
# ------------------------------------

def page_live_predictions_body():

    st.title("Live Ultrasound Image Classification")

    st.write(
        "Upload a first-trimester ultrasound image "
        "to classify it as **Standard** or **Non-Standard**."
    )

    uploaded_file = st.file_uploader(
        "Upload Ultrasound Image",
        type=["jpg", "jpeg", "png"]
    )

    if uploaded_file is None:
        return

    try:

        image = Image.open(uploaded_file)

        st.image(
            image,
            caption="Uploaded Ultrasound Image",
            use_container_width=True
        )

        with st.spinner("Analyzing ultrasound image..."):

            model = load_model()

            input_tensor = preprocess_image(image)

            probabilities, predicted_class, confidence = (
                predict_image(model, input_tensor)
            )

        st.subheader(
            f"Prediction: {predicted_class}"
        )

        st.metric(
            label="Prediction Confidence",
            value=f"{confidence:.2%}"
        )

        plot_predictions_probabilities(probabilities)

        st.caption(
            "This CNN prediction is experimental and "
            "is not a validated clinical assessment. "
            "The displayed confidence is a model score, "
            "not a clinically calibrated probability."
        )

    except Exception as e:

        st.error("Unable to complete prediction.")
        st.exception(e)

