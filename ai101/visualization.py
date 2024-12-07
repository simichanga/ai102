import seaborn as sns
import matplotlib.pyplot as plt

def plot_pairwise(df, target_names):
    """Plot pairwise relationships in the dataset."""
    sns.pairplot(df, hue="species", palette="Set2", diag_kind="kde", corner=True)
    plt.title("Pairwise Relationships")
    plt.show()

def plot_feature_importance(model, feature_names):
    """Plot feature importance for logistic regression."""
    importance = model.coef_[0]
    plt.barh(feature_names, importance)
    plt.xlabel("Feature Importance")
    plt.title("Feature Importance")
    plt.show()
