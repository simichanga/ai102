from data_processing import load_data, preprocess_data
from model import train_model, evaluate_model
from visualization import plot_pairwise, plot_feature_importance

def main():
    # Step 1: Load the data
    df, target_names = load_data()
    print("Dataset Loaded:")
    print(df.head())
    print("\nTarget Classes:", target_names)
    
    # Step 2: Visualize the data
    print("\nVisualizing pairwise relationships...")
    plot_pairwise(df, target_names)
    
    # Step 3: Preprocess the data
    X_train, X_test, y_train, y_test = preprocess_data(df)
    
    # Step 4: Train the model
    print("\nTraining the model...")
    model = train_model(X_train, y_train)
    
    # Step 5: Evaluate the model
    print("\nEvaluating the model...")
    evaluate_model(model, X_test, y_test)
    
    # Step 6: Visualize feature importance
    feature_names = df.columns[:-1]
    print("\nVisualizing feature importance...")
    plot_feature_importance(model, feature_names)

if __name__ == "__main__":
    main()
