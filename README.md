🩺 Medical Insurance Prediction using Machine Learning

This project focuses on predicting *medical insurance charges* using various machine learning regression models. It uses real-world healthcare data to build predictive models based on a person's demographics and lifestyle habits. The goal is to create a cost-estimation system that can be useful for individuals, insurance companies, or health policy planners.



 📌 Problem Statement

Medical insurance charges depend on multiple factors like age, BMI, gender, number of children, smoking habit, and region.  
This project builds a predictive model that estimates how much medical insurance cost a person may incur, based on such features.



 📊 Dataset Information

- Source: [Kaggle - Medical Cost Personal Dataset](https://www.kaggle.com/datasets/mirichoi0218/insurance)
- Total Records: 1,338 entries
- Features:
  - age: Age of the individual
  - sex: Gender (male/female)
  - bmi: Body Mass Index (numeric)
  - children: Number of dependents
  - smoker: Smoking habit (yes/no)
  - region: Location (northeast, northwest, southeast, southwest)
  - charges: Actual medical insurance cost (Target variable)



🧠 ML Models Used

- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor
- Model Evaluation Metrics:
  - R² Score
  - Mean Absolute Error (MAE)
  - Root Mean Squared Error (RMSE)

---

🛠 Technologies and Tools

- *Languages:* Python  
- *Libraries:* Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn  
- *Platform:* Jupyter Notebook / Google Colab  
- *Optional UI:* Streamlit (for deploying as web app)

---

 📈 Workflow

1. Importing Libraries & Dataset
2. Data Cleaning & Preprocessing
3. Exploratory Data Analysis (EDA)
4. Encoding Categorical Features
5. Splitting Data (Train-Test)
6. Model Building & Training
7. Model Evaluation
8. (Optional) Streamlit Web App Deployment




 
