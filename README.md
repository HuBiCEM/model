# HuBiCEM - Hunar Bin Cost Evaluation Model

**Repository:** [HuBiCEM](https://github.com/HuBuCEM/model)  
**Authors:** Abdullah Ahmad, Abdullah Bajwa  
**License:** See [LICENSE](LICENSE)  

## 📌 About

**HuBiCEM (Hunar Bin Cost Evaluation Model)** is an advanced **cost evaluation model** that individually estimates the **performance of every developer** instead of evaluating the team as a whole. Unlike traditional models, HuBiCEM:

- Evaluates **performance in different skill categories**.
- Uses **Linear Regression** to predict individual performance in upcoming sprints.
- Provides **detailed cost and time estimates**.

This tool consists of:
1. **train.py** → Trains a HuBiCEM model on project data.
2. **predict.py** → Predicts project completion time and cost.

## 📊 Features

- 🏗 **Sprint-Based Task Evaluation**  
- ⚡ **Per-Developer Performance Estimation**  
- 🔎 **Regression-Based Predictions**  
- 📉 **HuBi Table Generation (Linear Regression Applied to Each Developer)**  
- 📊 **Cost and Time Estimation for Future Sprints**  
- 🔍 **Detailed `report.txt` Summary**

---

## 🛠 Installation

Make sure you have **Python 3.7+** installed. Then install required dependencies:

```bash
pip install pandas numpy scikit-learn
```

## 🚀 Usage

### **1️⃣ Training the Model**
Train the model using a CSV file containing sprint-wise developer performance.

```bash
python src/train.py
```

### **2️⃣ Predicting Future Sprint Costs**
Once the model is trained, use it to estimate the cost and duration of the remaining sprints.

```bash
python src/predict.py
```

---


### **📌 "Input Format" for `train.py`**

#### **📄 Input Format (CSV)**
```
Sprint Number,Task,Category,Developer,Expected Time (Hours),Actual Time (Hours),Performance Comment
1,Project Setup & Planning,General,Abdullah Ahmad,10,12,Good
1,Database Schema Design,Database,Muhammad Umer,15,18,Delayed
...
```
✅ **Columns Explanation:**
- **Sprint Number** → Sprint number (e.g., `1, 2, 3...`)
- **Task** → The task assigned in that sprint.
- **Category** → Task category (e.g., `Frontend, Backend, AI/ML`).
- **Developer** → Name of the developer assigned to this task.
- **Expected Time (Hours)** → Estimated time for completion.
- **Actual Time (Hours)** → Actual time taken.
- **Performance Comment** → Performance feedback (e.g., `Good, Delayed, Needs Improvement`).

---

### **📌 "Input Format" for `predict.py`**

#### **📄 Input Format (`trained.csv`)**
```
#,Employee,Frontend,Backend,Database,AI/ML,Server,Security
1,Abdullah Ahmad,e1.2 + 3.4,e0.9 + 1.8,e1.5 - 0.5,e2.0 + 2.1,e1.1 + 0.9,""
2,Muhammad Umer,e1.3 + 2.0,e1.0 - 1.2,e0.7 + 3.1,"","",""
...
```
✅ **Columns Explanation:**
- **#** → Serial number.
- **Employee** → Name of the developer.
- **Category Columns** (e.g., `Frontend, Backend, AI/ML`) → Each category contains an **equation** in the form `ex + c` (e.g., `"e1.5 + 3.2"`).

---

### **📌 "Output Format" for `predict.py`**
#### **📄 Output 1: `prediction.csv`**
```
#,Employee,Frontend,Backend,Database,AI/ML,Server,Security
1,Abdullah Ahmad,12.4,14.1,9.5,15.2,11.0,8.3
2,Muhammad Umer,10.3,12.0,14.2,9.0,13.1,7.5
...
```
✅ **Each column now has actual predicted hours instead of formula.**

#### **📄 Output 2: `report.txt`**
```
🔹 Project Estimated Hours: 1450.75 hours
🔹 Estimated Duration: 3.2 months
🔹 Estimated Total Cost: $72,500.50
```

---



## 📂 File Structure

```
HuBiCEM/
│── src/
│   ├── train.py          # Trains HuBiCEM Model
│   ├── predict.py        # Predicts time & cost using trained model
│
│── examples/
│   ├── 1-train.sh        # Example script for training
│   ├── 2-predict.sh      # Example script for prediction
│   ├── README.md         # Usage Doc for example scripts
│
│── LICENSE               # License file
│── README.md             # This file
```

---

## 📑 Input & Output Example

### **📝 Input Data Format (`sprints.csv`)**
```
Sprint Number,Task,Category,Developer,Expected Time (Hours),Actual Time (Hours),Performance Comment
1,Project Setup & Planning,General,Abdullah Ahmad,10,12,Good
1,Database Schema Design,Database,Muhammad Umer,15,18,Delayed
...
```

### **🔄 Training (`train.py`)**
```bash
python src/train.py
```
- Reads sprint CSV.
- Extracts **unique categories**.
- **Trains Linear Regression** on each developer.
- Generates **HuBi Table** (e.g., `"e1.2 + 3.4"` formula for predictions).
- Saves **trained.csv**.

---

### **📊 Prediction (`predict.py`)**
```bash
python src/predict.py
```
- Reads **trained.csv**.
- **Predicts actual hours** required for future sprints.
- Generates:
  - `prediction.csv` (detailed breakdown).
  - `report.txt` (summary of estimated time & cost).

#### **📄 Sample `report.txt`**
```
🔹 Project Estimated Hours: 1450.75 hours
🔹 Estimated Duration: 3.2 months
🔹 Estimated Total Cost: $72,500.50
```

---

## 📜 License

This project is licensed under the **HuBiCEM License**.  
- ✅ **Allowed:** Use this model freely for personal and commercial use.  
- 🚫 **Not Allowed:** Publish or present this research under any other name.  

See **[LICENSE](LICENSE)** for details.

---

## 👨‍💻 Contributors
- **Abdullah Ahmad** ([@MAbdullahAhmad](https://github.com/MAbdullahAhmad))  
- **Abdullah Bajwa** ([@Abdullah007bajwa](https://github.com/Abdullah007bajwa))

💡 **Ideas?** Feel free to **open an issue** or **contribute!** 🚀