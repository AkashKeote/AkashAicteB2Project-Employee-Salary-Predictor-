
# Employee Salary Prediction using Machine Learning

**Disclaimer:**
This project was created only for the Edunet Foundation AICTE Internship, during the internship period, under the lead mentorship of Dr. Nanthini Mohan ([LinkedIn](https://www.linkedin.com/in/dr-nanthini-mohan-9a727a105/)).
All code, data, and documentation are for educational and demonstration purposes only.

## Student & Internship Details
- **Student Name:** Akash Keote
- **Batch:** EDUNET FOUNDATION AICTE BATCH B2 AI 2025-2026
- **AICTE Internship Student Registration ID:** STU67e3fe6b79a3f1742995051
- **Student ID (Enrolment number):** 2223CPFBTCSE008
  **Email:** keoteakash@gmail.com
- **Contact Info:** +91-9307451323
- **Nationality:** Indian
- **College:** GH Raisoni College of Engineering and Management, Nagpur
- **Year:** 4th Year, BTech CSE

## Project Features
- Data cleaning and outlier removal
- Exploratory Data Analysis (EDA) with visualizations
- Feature engineering (categorical encoding, polynomial & interaction features)
- Multiple regression models:
  - Linear Regression
  - Ridge Regression
  - Lasso Regression
  - Decision Tree Regressor
  - Random Forest Regressor
  - XGBoost Regressor (advanced, high accuracy)
  - TPOT (AutoML)
- Model comparison (R2, RMSE, MAE) with leaderboard highlight
- Cross-validation for robust evaluation
- SHAP & LIME explainability for feature importance
- Custom error analysis
- Model saving and loading (joblib)
- Predict salary for a new employee (custom input)
- Streamlit web app for interactive prediction
- (Optional) Flask API endpoint for model serving

## Dataset
- `Salary Data.csv` contains columns: Age, Gender, Education Level, Job Title, Years of Experience, Salary
- Dataset Source: [Kaggle - Salary Prediction for Beginner](https://www.kaggle.com/datasets/rkiattisak/salaly-prediction-for-beginer?resource=download)

## Usage Instructions
1. **Install dependencies:**
   - Python 3.8+
   - Install required packages:
     ```bash
     pip install pandas numpy matplotlib seaborn scikit-learn xgboost shap joblib streamlit tpot lime
     ```
2. **Run the notebook:**
   - Open `akash.ipynb` in Jupyter Notebook or VSCode.
   - Run all cells sequentially.
   - The notebook will:
     - Clean and analyze the data
     - Train and compare multiple models
     - Show feature importance and explainability
     - Save the best model
     - Allow you to predict salary for a new employee
3. **Run the Streamlit app:**
   - In terminal: `streamlit run streamlit_app.py`
   - Use the web interface for interactive predictions.

## Results
- The notebook compares all models and highlights the best one (usually XGBoost or TPOT/Random Forest).
- SHAP & LIME plots show which features most influence salary predictions.
- Cross-validation ensures the model is robust and not overfitting.

## Customization
- You can change the input features for new employee prediction at the end of the notebook.
- Try adding/removing features or tuning model parameters for even better results.

## Acknowledgments
I learned all these concepts from:
- **Dr. Nanthini Mohan** (Lead Mentor, Edunet Foundation AICTE Internship)  
  [LinkedIn](https://www.linkedin.com/in/dr-nanthini-mohan-9a727a105/)
- **Chai aur Code** (YouTube Channel)
- **Code With Harry** (YouTube Channel)

Thank you for your guidance, tutorials, and inspiration throughout my learning journey!

## License & Citation
- **License:** See LICENSE file (custom, Akash Keote, Edunet Foundation AICTE Internship only)
- **Citation:** If you use this work, please cite: Akash, "Employee Salary Prediction using ML", 2025.

---

**This project is ready for submission and demonstrates advanced ML workflow, model comparison, explainability, and professional documentation.**

---

## 🚀 Live Demo
[Click here to try the Employee Salary Prediction App!](https://edunet-akashkeote-mla-project.streamlit.app/)

---

