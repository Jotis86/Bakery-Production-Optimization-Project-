# 🥖 Bakery Production Optimization Project 🍞

![Bakery Image](images/Bakery_2.png)

![Commits](https://img.shields.io/github/commit-activity/m/Jotis86/Bakery-Production-Optimization-Project-)
![Issues Abiertas](https://img.shields.io/github/issues/Jotis86/Bakery-Production-Optimization-Project-)
![Pull Requests](https://img.shields.io/github/issues-pr/Jotis86/Bakery-Production-Optimization-Project-)
![Forks](https://img.shields.io/github/forks/Jotis86/Bakery-Production-Optimization-Project-)
![Tamaño del Repositorio](https://img.shields.io/github/repo-size/Jotis86/Bakery-Production-Optimization-Project-)
![Autor](https://img.shields.io/badge/autor-Juan%20Duran%20Bon-blue)
![Licencia](https://img.shields.io/github/license/Jotis86/Bakery-Production-Optimization-Project-)

## 🎯 Objectives
The primary objective of this project is to develop a machine learning model to predict the optimal production quantities in a bakery. This aims to minimize waste, reduce financial losses, conserve resources, and lower the environmental footprint. The project addresses the following key issues:
- **Financial Losses**: Unused products lead to significant financial losses.
- **Resource Waste**: Inefficient production results in wasted ingredients and labor.
- **Environmental Impact**: Excess production contributes to a larger environmental footprint.

By leveraging historical sales, production, and demand data, the project seeks to create a predictive model that can accurately forecast production needs, thereby optimizing the bakery's operations.

## ⚙️ Functionality
- 📥 Data loading and cleaning.
- 🔍 Exploratory Data Analysis (EDA).
- 🛠️ Data preprocessing.
- 🧠 Development and evaluation of machine learning models.
- 📊 Generation of visualizations to interpret results.
- 🔮 Prediction of optimal production quantities.

## 🛠️ Tools Used
- Python 🐍: Main programming language.
- Pandas 🐼: For data manipulation and analysis.
- Matplotlib 📉 and Seaborn 🐟: For data visualization.
- Scikit-learn 🤖: For data preprocessing and machine learning model development.
- Power BI 📊: For creating interactive dashboards.

## 🛠️ Development Process
### Library Import 📚
Importing necessary libraries for data manipulation, visualization, and machine learning.

### Data Loading 📥
Reading CSV files containing historical sales, production, and demand data.

### Data Exploration 🔍
Viewing the first and last rows, data summary, and descriptive statistics to understand the dataset.

### Data Cleaning 🧹
Handling missing values, correcting errors, removing duplicates, and transforming data to ensure quality.

### Exploratory Data Analysis 📊
Visualizing distributions and relationships between variables, such as:
- Sales trends by day of the week 📅
- Correlation between variables 📈
- Grouping of products by families 🍞

### Data Preprocessing 🛠️
Standardizing numerical data and one-hot encoding categorical data to prepare for model training.

### Model Development 🧠
Defining and training two machine learning models:

#### Model 1: Based on Product Families and Days of the Week
This model groups products into families and makes predictions based on these groupings along with the day of the week.

**Explanation of Model 1:**
- **Feature Selection and Target Variable**: Selecting relevant features and the target variable (Quantity) for each product family.
- **Data Splitting**: Dividing the data into training and test sets to evaluate model performance.
- **Data Scaling**: Applying Min-Max Scaling to normalize the data and ensure all features are on the same scale.
- **Model Definition**: Defining several machine learning models, including Linear Regression, Decision Tree, Random Forest, and Gradient Boosting, each with specific hyperparameters.
- **Hyperparameter Tuning**: Using RandomizedSearchCV to find the best hyperparameters for each model, optimizing their performance.
- **Prediction and Evaluation**: Making predictions on the test set and evaluating the models using metrics such as Mean Squared Error (MSE), Mean Absolute Error (MAE), Root Mean Squared Error (RMSE), and R-squared (R2).
- **Predictions for Desired Dates**: Making predictions for specific dates using the best model, allowing for more precise production planning.

#### Model 2: Based on Individual Products and Days of the Week
This model makes predictions for each product individually, also considering the day of the week.

**Explanation of Model 2:**
- **Selection of Specific Products**: Identifying critical products for the bakery and analyzing them individually.
- **Grouping by Families**: Grouping products by families to facilitate analysis and prediction.
- **Handling Insufficient Data**: Imputing the quantity with the family mean for products with few records to ensure data consistency.
- **Data Splitting**: Dividing the data into training and test sets to evaluate model performance.
- **Data Scaling**: Applying Min-Max Scaling to normalize the data and ensure all features are on the same scale.
- **Model Training**: Using a Random Forest Regressor model, trained with the scaled data, to make predictions.
- **Model Evaluation**: Evaluating the model using metrics such as Mean Squared Error (MSE), Mean Absolute Error (MAE), Root Mean Squared Error (RMSE), and R-squared (R2).
- **Predictions for Desired Dates**: Making predictions for specific dates using the trained model, allowing for more precise production planning.

### Final Predictions 🔮
Applying the best-performing model to predict optimal production quantities and saving the results.

## 📈 Results
The results showed a significant reduction in unsold products, minimizing losses and improving production efficiency.

## 📝 Conclusions
- The methodology used allowed for optimized production and reduced waste.
- The model based on individual products showed better performance compared to the model based on product families.
- Further improvement in data preprocessing and feature selection is recommended to increase model accuracy.

## 📊 Visualizations
- Sales trends by day of the week 📅
- Correlation between variables 📈
- Grouping of products by families 🍞

## 🧠 Models and Metrics
### Model 1: Based on Product Families and Days of the Week
- **Models Used**: Linear Regression, Decision Tree, Random Forest, Gradient Boosting
- **Evaluation Metrics**: Mean Squared Error (MSE), Mean Absolute Error (MAE), Root Mean Squared Error (RMSE), R-squared (R2)

### Model 2: Based on Individual Products and Days of the Week
- **Model Used**: Random Forest
- **Evaluation Metrics**: Mean Squared Error (MSE), Mean Absolute Error (MAE), Root Mean Squared Error (RMSE), R-squared (R2)

## 📊 Power BI Dashboard
An interactive dashboard was created in Power BI to analyze the results of the predictive models and compare them with the orders placed by the manager. This dashboard allows for graphical comparison of the model predictions with actual order data, facilitating decision-making and production planning.

### Dashboard Features:
- **Comparison of Predictions and Actual Orders**: Charts showing the differences between the quantities predicted by the models and the quantities actually ordered by the manager.
- **Trend Analysis**: Visualization of sales and production trends over time.
- **Interactivity**: Filters and slicers that allow users to explore the data dynamically and customize their view.

## 🗂️ Project Structure
- **Data**: Contains the data used in the project.
- **Notebooks**: Includes notebooks for loading and merging dataframes, EDA, and model development.
- **Power BI Dashboard**: Folder with the interactive dashboard created in Power BI.
- **Project Summary**: Folder with the project presentation in PowerPoint and PDF formats.
- **Images**: Contains images used in the project documentation.

## 📬 Contact
For any inquiries, feel free to reach out to me through the following channels:

📧 **Email**: [jotaduranbon@gmail.com](mailto:jotaduranbon@gmail.com)  
💼 **LinkedIn**: [Juan Duran Bon](https://www.linkedin.com/in/juan-duran-bon)

## 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
