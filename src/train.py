import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import os

def validate_csv(file_path):
    """Validate CSV format to ensure required columns exist"""
    required_columns = ["Sprint Number", "Task", "Category", "Developer", "Expected Time (Hours)", "Actual Time (Hours)", "Performance Comment"]
    try:
        df = pd.read_csv(file_path)
        if not all(col in df.columns for col in required_columns):
            print("Error: CSV file is missing required columns. Please check the file format.")
            return None
        return df
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return None

def extract_unique_categories(df):
    """Extract unique categories from dataset"""
    return list(df["Category"].unique())

def train_regression(df, employees, categories):
    """Train regression model for each employee in each category"""
    results = []

    for employee in employees:
        employee_data = df[df["Developer"] == employee]
        formula_dict = {"Employee": employee}

        for category in categories:
            category_data = employee_data[employee_data["Category"] == category]

            if len(category_data) < 2:  # Skip if not enough data for regression
                formula_dict[category] = ""
                continue

            # Regression Model Training
            X = category_data[["Expected Time (Hours)"]].values.reshape(-1, 1)  # X = Expected Time
            y = category_data["Actual Time (Hours)"].values  # y = Actual Time

            model = LinearRegression()
            model.fit(X, y)

            e_value = round(model.coef_[0], 2)  # Get slope
            c_value = round(model.intercept_, 2)  # Get intercept

            # Format equation as "eX + C" (e.g., "e1.5 + 2.3")
            if c_value >= 0:
                formula_dict[category] = f"e{e_value} + {c_value}"
            else:
                formula_dict[category] = f"e{e_value} - {abs(c_value)}"

        results.append(formula_dict)

    return results

def main():
    """Main function to process CSV and train regression models"""
    file_path = input("Enter the path to the sprint CSV file: ")

    if not os.path.exists(file_path):
        print("Error: File not found.")
        return

    df = validate_csv(file_path)
    if df is None:
        return

    categories = extract_unique_categories(df)
    employees = df["Developer"].unique()

    print("Training regression models...")
    trained_data = train_regression(df, employees, categories)

    # Convert list of dicts to DataFrame
    trained_df = pd.DataFrame(trained_data)

    # Add column numbering
    trained_df.insert(0, "#", range(1, len(trained_df) + 1))

    # Save the trained model to CSV
    output_file = "trained.csv"
    trained_df.to_csv(output_file, index=False)

    print(f"Training complete. Results saved in '{output_file}'.")

if __name__ == "__main__":
    main()
