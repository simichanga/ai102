# AI & Data Science 101
This project introduces foundational concepts in data science and artificial intelligence by working with the Iris dataset, a classic dataset in machine learning. The goal is to predict the species of Iris flowers based on their features using a supervised machine learning model.

## Project Structure
The project is organized into separate modules for better readability and maintainability:

```plaintext
ai_data_science_101/
│
├── main.py                # Entry point for the project
├── data_processing.py     # Data loading and preprocessing
├── model.py               # Model training and evaluation
└── visualization.py       # Visualization utilities
```

## Dataset
The Iris dataset is a well-known dataset for machine learning. It contains 150 samples with the following features:

<ol>
Sepal length (cm)   <br>
Sepal width (cm)    <br>
Petal length (cm)   <br>
Petal width (cm)    <br>
</ol>

Each sample is labeled with one of three species:

<ol>
Setosa      <br>
Versicolor  <br>
Virginica   <br>
</ol>

The dataset is included in the scikit-learn library and does not require additional downloads.

## Getting Started
Install the required libraries:
```bash
pip install pandas numpy matplotlib seaborn scikit-learn
```

## Steps in the Project
### 1. Data Loading

The Iris dataset is loaded using scikit-learn and converted into a pandas.DataFrame for better analysis.
Initial exploration reveals feature statistics and target classes.

### 2. Data Visualization

Pairwise relationships between features are visualized using seaborn.pairplot. This helps understand how features are distributed and correlated.

### 3. Data Preprocessing

The dataset is split into training (70%) and testing (30%) subsets using train_test_split.
Feature scaling is applied using StandardScaler to normalize the feature values for better model performance.

### 4. Model Training

A Logistic Regression model is trained on the training dataset.
Logistic regression is chosen for its simplicity and interpretability.

### 5. Model Evaluation

The model's performance is evaluated on the test dataset using:
Accuracy Score
Classification Report (Precision, Recall, F1-score)

### 6. Feature Importance

The contribution of each feature to the model's predictions is visualized using a bar chart.
- Features
- Visualizations
- Pairwise feature relationships to explore correlations.
- Feature importance to understand the impact of each input on the model's predictions.
- Metrics
- Accuracy: Measures the percentage of correct predictions.
- Classification Report: Provides precision, recall, and F1-scores for each class.
- Expected Output

When you run the project, you will:

- View the first few rows of the dataset and the target classes.
- See a pairwise plot of the dataset features.
- Obtain metrics for the trained model, including accuracy and a classification report.
- Visualize the feature importance for model predictions.
