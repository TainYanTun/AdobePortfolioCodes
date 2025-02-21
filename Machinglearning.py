import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

# Title of the app
st.title("Interactive Machine Learning Dashboard")

# Sidebar for user inputs
st.sidebar.header("Upload Your Dataset")
uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    # Load the dataset
    data = pd.read_csv(uploaded_file)
    st.write("### Dataset Preview", data.head())

    # Preprocessing
    st.sidebar.header("Data Preprocessing")
    target_column = st.sidebar.selectbox("Select Target Column", data.columns)
    feature_columns = st.sidebar.multiselect("Select Feature Columns", data.columns, default=list(data.columns[:-1]))

    if target_column and feature_columns:
        X = data[feature_columns]
        y = data[target_column]

        # Train-test split
        test_size = st.sidebar.slider("Test Set Size", 0.1, 0.5, 0.2)
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42)

        # Model selection and training
        st.sidebar.header("Model Training")
        n_estimators = st.sidebar.slider("Number of Trees", 10, 200, 100)
        max_depth = st.sidebar.slider("Max Depth", 1, 20, 10)

        model = RandomForestClassifier(n_estimators=n_estimators, max_depth=max_depth, random_state=42)
        model.fit(X_train, y_train)

        # Model evaluation
        y_pred = model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        st.write(f"### Model Accuracy: {accuracy:.2f}")

        # Confusion matrix
        st.write("### Confusion Matrix")
        cm = confusion_matrix(y_test, y_pred)
        fig, ax = plt.subplots()
        sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", ax=ax)
        ax.set_xlabel("Predicted")
        ax.set_ylabel("Actual")
        st.pyplot(fig)

        # Feature importance
        st.write("### Feature Importance")
        importance = model.feature_importances_
        feature_importance_df = pd.DataFrame({"Feature": feature_columns, "Importance": importance})
        feature_importance_df = feature_importance_df.sort_values(by="Importance", ascending=False)
        st.bar_chart(feature_importance_df.set_index("Feature"))

else:
    st.write("Please upload a CSV file to get started.")