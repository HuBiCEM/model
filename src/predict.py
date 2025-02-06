import pandas as pd
import os

def validate_csv(file_path, required_columns):
    """Validate CSV format to ensure required columns exist"""
    try:
        df = pd.read_csv(file_path)
        if not all(col in df.columns for col in required_columns):
            print("Error: CSV file is missing required columns. Please check the file format.")
            return None
        return df
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return None

def predict_hours(trained_df):
    """Predict hours required based on trained regression formulas"""
    predictions = []
    total_estimated_hours = 0

    for index, row in trained_df.iterrows():
        employee = row["Employee"]
        formula_dict = {"Employee": employee}

        for category in trained_df.columns[2:]:  # Ignore first two columns (#, Employee)
            formula = row[category]

            if pd.isna(formula) or formula == "":
                formula_dict[category] = ""
                continue

            try:
                parts = formula.split("+") if "+" in formula else formula.split("-")
                e_value = float(parts[0][1:])  # Extract coefficient
                c_value = float(parts[1]) if len(parts) > 1 else 0
                estimated_hours = round(e_value * 10 + c_value, 2)  # Assume avg expected time per task = 10h
                total_estimated_hours += estimated_hours
                formula_dict[category] = estimated_hours
            except Exception as e:
                print(f"Error parsing formula {formula}: {e}")
                formula_dict[category] = ""

        predictions.append(formula_dict)

    return pd.DataFrame(predictions), total_estimated_hours

def write_report(total_hours, project_duration=None, total_cost=None):
    """Generate report.txt summarizing project estimations"""
    with open("report.txt", "w") as file:
        file.write(f"🔹 Project Estimated Hours: {total_hours:.2f} hours\n")
        if project_duration:
            file.write(f"🔹 Estimated Duration: {project_duration:.2f} months\n")
        if total_cost:
            file.write(f"🔹 Estimated Total Cost: ${total_cost:.2f}\n")

    print("\n📄 Report saved as 'report.txt'.")

def main():
    """Main function for prediction process"""
    file_path = "trained.csv"

    if not os.path.exists(file_path):
        file_path = input("Enter the path to the trained CSV file: ")

    required_columns = ["#", "Employee"]
    trained_df = validate_csv(file_path, required_columns)

    if trained_df is None:
        return

    print("\n🔄 Predicting estimated hours...")
    predicted_df, total_hours = predict_hours(trained_df)

    # Save predictions
    predicted_df.to_csv("prediction.csv", index=False)
    print("✅ Predictions saved in 'prediction.csv'.")

    # Report file
    write_report(total_hours)

    # Ask for optional inputs
    project_duration = None
    total_cost = None

    print("\n🕒 Enter available hours per month for each developer (0 to skip):")
    total_available_hours = 0

    for employee in trained_df["Employee"]:
        try:
            hours = float(input(f"  - {employee}: "))
            if hours > 0:
                total_available_hours += hours
        except ValueError:
            print("Invalid input, skipping...")

    if total_available_hours > 0:
        project_duration = total_hours / total_available_hours
        print(f"\n📅 Estimated Project Duration: {project_duration:.2f} months")

    print("\n💰 Enter cost per hour for each developer (0 to skip):")
    total_cost = 0

    for employee in trained_df["Employee"]:
        try:
            cost = float(input(f"  - {employee} (per hour rate): $"))
            if cost > 0:
                total_cost += cost * total_hours / len(trained_df["Employee"])
        except ValueError:
            print("Invalid input, skipping...")

    if total_cost > 0:
        print(f"\n💵 Estimated Total Cost: ${total_cost:.2f}")

    # Finalize report
    write_report(total_hours, project_duration, total_cost)

    print("\n🚀 Prediction completed! Check 'prediction.csv' and 'report.txt'.")
    print("👋 Goodbye! Have a great day!")

if __name__ == "__main__":
    main()
