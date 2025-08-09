
CHURN PREDICTION MODEL

Introduction

A churn predictor algorithm assists in predicting if the bank's customer will leave the bank or not by considering other demographic factors. The dataset for this system includes the following columns:

Input

RowNumber: shows the record (row) number and has no effect on the output.
CustomerId: contains random values and has no effect on customer leaving the bank.
Surname: the surname of a customer has no impact on their decision to leave the bank.
CreditScore: can have an effect on customer churn, since a customer with a higher credit score is less likely to leave the bank.
Geography: the location of the customer which can affect their decision to leave the bank.
Gender: male or female customer of the bank, which may or may not play a role in customer churn.
Age: this is certainly relevant, since older customers are less likely to leave their bank than younger ones.
Tenure: refers to the number of years that the customer has been a client of the bank.
NumOfProducts: refers to the number of products that a customer has purchased through the bank.
HasCrCard: denotes whether or not a customer has a credit card.
IsActiveMember: shows if the customer is using theri account actively or not.
EstimatedSalary: as with balance, people with lower salaries are more likely to leave the bank compared to those with higher salaries.
Exited: whether or not the customer left the bank. (Yes = 1, No = 0)
Model Details

The dataset is taken from https://www.kaggle.com/code/simgeerek/churn-prediction-using-machine-learning/input. The features considered to build a MI model are CreditScore, Geography, Gender, Age, Tenure, Balance, NumOfProducts, HasCrCard, IsActiveMember, EstimatedSalary.

Steps involved

Data cleaning and Exploratory Data Analysis (EDA) - Checked for null values, plotted graphs to visualise the variation.
Data Preprocessing and Feature Engineering - Columns like RowNumber, CustomerId, and Surname are dropped, as they are irrelevant for the model. Using Standard scaler, numeric coumns are scaled.
Model Training - Random Forest Classifier is used to train the model.
Model Evaluation - Evaluate the model’s performance using metrics like Accuracy, Classification Report, Confusion Matrix, ROC curves and AUC.
Business Questions

How does the credit score and the other demographic factors of the customers vary?
Graphs have been plotted to show the variations in customers' credit score, age, gender, and geography. Based on the results, it is concluded that both genders have almost the same average credit score. Additionally, customers from France in the age group of 40–50 are the most numerous among all the bank's customers.

How does customer tenure and account balance affect the customer churn?
A Correlation matrix has been plotted to check the relationship between each feature, and it is clearly visible that Tenure is negatively correlated, while Balance is positively correlated with customer churn.

How does the churn prediction model utilize customer activity and product usage patterns to forecast churn?
To forecast churn, the model utilizes various features, such as the client's geography. If the client is located near the bank, they are more likely to have an account, and this also depends on the country's policies. The tenure and age of the customer are also important factors; the longer a client stays with the bank, the more familiar they are with the processes and the more likely they are to remain. On the other hand, older customers, whose income may have stopped, are more likely to close their accounts. The number of products a customer has also plays a significant role in churn, as customers who have benefited from more products are more likely to stay.

Technologies used

Languages: Python
Libraries: Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn
Tools: Jupyter Notebook
License

This project is licensed under the MIT License.
