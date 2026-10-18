# 2D Fetal Ultrasound Image Classification Using Deep Learning

# Project Overview

This project investigates the application of deep learning to classify two-dimensional (2D) fetal ultrasound images into **Standard** and **Non-Standard** categories.

Accurate acquisition of a standard midsagittal ultrasound view is important for evaluating fetal anatomy and measuring nuchal translucency (NT) during the first trimester of pregnancy.

A Convolutional Neural Network (CNN) is developed to investigate whether image classification can support the assessment of ultrasound image standardization.

The project includes exploratory data analysis, image preprocessing, CNN training, model evaluation, and a Streamlit dashboard for interactive predictions.

*The model is intended for educational and research purposes only. It is not validated for clinical diagnosis or medical decision-making.**

---

# 1. Business Case and Dataset

## Background

The dataset contains 1,528 two-dimensional sagittal-view fetal ultrasound images from 1,519 pregnant patients, collected at Shenzhen People's Hospital.

The images are used for Standard/Non-Standard (S-NS) plane classification, an important consideration in obtaining reliable nuchal translucency measurements.

A Standard image represents a properly acquired midsagittal fetal profile in which the relevant anatomical structures can be visualized and NT measurement can be performed reliably.

A Non-Standard image does not satisfy the same acquisition criteria. The distinction may involve subtle differences in positioning, image quality, and visualization of anatomical landmarks.

An additional external dataset containing 156 images from the Longhua branch of Shenzhen People's Hospital is described in the dataset information.

## Anatomical Annotations

The dataset documentation describes annotations for nine anatomical structures in `ObjectDetection.xlsx`:

1. Thalami
2. Midbrain
3. Palate
4. Fourth ventricle
5. Cisterna magna
6. Nuchal translucency (NT)
7. Nasal tip
8. Nasal skin
9. Nasal bone

These annotations provide useful anatomical context. However, the CNN developed in this project focuses on image-level classification rather than object detection.

## Dataset Source

The dataset is available on Kaggle:

[Dataset for Fetus Framework](https://www.kaggle.com/datasets/orvile/dataset-for-fetus-framework)

The dataset is not included in this GitHub repository because of its size. Users should obtain it separately and review the applicable dataset terms.

---

## 2. Project Objectives

The primary objective is to develop and evaluate a supervised deep learning model capable of classifying fetal ultrasound images into:

- **Standard**
- **Non-Standard**

The project also aims to:

- Explore visual characteristics of the two image categories.
- Analyze class distribution and image variability.
- Prepare ultrasound images for CNN training.
- Evaluate classification performance using an independent test dataset.
- Provide an interactive dashboard for uploading and classifying images.

## 3. Conventional Data Analysis

Exploratory data analysis is used to understand the dataset before model development.

The visual study includes:

- Class distribution analysis.
- Mean and standard deviation images.
- Comparison of average images between the two categories.
- Image montages illustrating within-class variability.
- Investigation of image dimensions and visual characteristics.

These analyses help characterize the available data and identify potential differences between Standard and Non-Standard images.

---

## 4. Machine Learning Solution

### Model Architecture

A Convolutional Neural Network (CNN) is used for supervised binary image classification.

The model includes:

- Convolutional layers for feature extraction.
- Max-pooling layers for spatial downsampling.
- A flattening layer.
- A fully connected dense layer.
- Dropout regularization.
- A two-neuron Softmax output layer.

The network predicts one of two classes:

| Class |	| Label |

  0    	Non-Standard
  1   	   Standard


### Image Preprocessing

Images are resized to 256 × 256 pixels, converted to RGB format, and normalized by dividing pixel values by 255.

The dataset is organized into training, validation, and test subsets.

### Model Evaluation

Model performance is assessed using:

- Training and validation accuracy.
- Training and validation loss.
- Test-set accuracy and loss.
- Classification reports and confusion matrices, where available.

Particular attention is given to generalization performance and possible class imbalance.

The model's predicted Softmax scores are displayed in the dashboard. These scores should not automatically be interpreted as calibrated probabilities.

---

## 5. Hypothesis and Validation

### Hypothesis

A Convolutional Neural Network can learn image features that distinguish Standard from Non-Standard fetal ultrasound images.

### Validation Strategy

The hypothesis is evaluated by:

1. Preparing labeled ultrasound images.
2. Dividing the dataset into training, validation, and test sets.
3. Training the CNN using the training data.
4. Monitoring validation performance during training.
5. Evaluating the final model on unseen test images.
6. Investigating misclassifications and class-specific performance.

A successful evaluation requires more than high training accuracy. The model must demonstrate reliable performance on independent test data.

---

## 6. Mapping Business Requirements to ML Tasks

### Requirement 1: Visual Study

**Business requirement:** Investigate visual differences between Standard and Non-Standard ultrasound images.

**Mapped tasks:**

- Display mean and standard deviation images.
- Compare average images between classes.
- Generate image montages.
- Analyze class distributions.

### Requirement 2: Image Classification

**Business requirement:** Develop a model that predicts whether an ultrasound image is Standard or Non-Standard.

**Mapped tasks:**

- Train a CNN classifier.
- Evaluate predictive performance.
- Generate a predicted class and associated model score.
- Integrate the model into an interactive Streamlit dashboard.

---

## 7. Dashboard Design

The Streamlit dashboard is organized into five main pages.

### Page 1: Project Summary

Introduces the project, dataset, clinical background, and classification objective.

### Page 2: Hypothesis and Validation

Describes the machine learning hypothesis and the approach used to validate it.

### Page 3: Visual Study Findings

Presents the exploratory image analysis, including:

- Mean and standard deviation images.
- Differences between average images.
- Image montages for both classes.

### Page 4: ML Performance Metrics

Presents model evaluation results, including:

- Class distribution across datasets.
- Training and validation accuracy.
- Training and validation loss.
- Final test evaluation metrics.

### Page 5: Live Predictions

Allows users to:

- Upload an ultrasound image in JPG or PNG format.
- Run the trained CNN model.
- View the predicted Standard or Non-Standard class.
- Inspect the model's output scores.

---

## 8. Repository Structure

```text
ML_2/
├── app.py
├── app_pages/
│   ├── page_summary.py
│   ├── page_hypothesis.py
│   ├── page_visual_study_findings.py
│   ├── page_ML_performance.py
│   └── page_live_predictions.py
├── jupyter_notebooks/
│   ├── Data Collection.ipynb
│   ├── Data visualization.ipynb
│   └── Modelling and Evaluating.ipynb
├── src/
│   ├── data_management.py
│   └── machine_learning/
│       ├── evaluate_clf.py
│       └── predictive_analysis.py
├── requirements.txt
├── setup.sh
├── heroku.yml
├── README.md
└── .gitignore
```

Generated outputs, trained models, and datasets are excluded from version control where appropriate.

---

## 9. Installation and Local Setup

### Clone the Repository

```bash
git clone https://github.com/omerahm69/ML_2.git
cd ML_2
```

### Create a Virtual Environment

On Windows:

```powershell
python -m venv venv_clean
.\venv_clean\Scripts\Activate.ps1
```

### Install Dependencies

```powershell
python -m pip install -r requirements.txt
```

### Start JupyterLab

```powershell
jupyter lab
```

Open the notebooks in `jupyter_notebooks/` to explore the data analysis and model development workflow.

### Run the Streamlit Dashboard

```powershell
python -m streamlit run app.py
```

**Important:** The dashboard requires the relevant generated analysis outputs and trained CNN model. These are not necessarily included in the repository and must be created or supplied separately at the paths expected by the application.

---

## 10. GitHub Codespaces

GitHub Codespaces provides a cloud-based development environment.

To use it:

1. Fork the repository or open it directly on GitHub.
2. Click **Code**.
3. Select the **Codespaces** tab.
4. Create a codespace on the `main` branch.
5. Wait for the development environment to initialize.
6. Open the `jupyter_notebooks/` directory.
7. Select an available Python kernel.
8. Install missing dependencies if necessary.

Check the active Python version using:

```python
import sys
print(sys.version)
```

The available Python version depends on the Codespaces environment and configuration.

---

## 11. Technologies and Libraries

The project uses:

- Python
- TensorFlow / Keras
- NumPy
- Pandas
- Matplotlib
- Seaborn
- Scikit-learn
- Pillow
- JupyterLab
- Streamlit
- Git and GitHub

Deployment-related configuration files are also included in the repository.

---

## 12. Project Limitations

The following limitations should be considered:

- The dataset may contain class imbalance.
- Images may differ in acquisition conditions and quality.
- Good training or validation performance does not guarantee generalization.
- Evaluation on external clinical datasets is important before considering practical use.
- Softmax scores do not necessarily represent calibrated confidence.
- The model performs image classification, not anatomical structure localization or NT measurement.

The system is a research prototype and must not be used as a substitute for qualified clinical assessment.

---

## 13. Project Repository

GitHub: [omerahm69/ML_2](https://github.com/omerahm69/ML_2)

Dataset: [Kaggle — Dataset for Fetus Framework](https://www.kaggle.com/datasets/orvile/dataset-for-fetus-framework)
