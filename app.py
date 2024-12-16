import streamlit as st

# Page configuration
st.set_page_config(page_title="Bakery Production Optimization Project", page_icon="🥖", layout="wide")

# Sidebar
st.sidebar.title("Menu")
menu = st.sidebar.radio("Navigation", ["Home", "Objectives and Methodology", "Tools and Results", "Visualizations and Models", "Power BI Dashboard"])

# GitHub repository button in the sidebar
if st.sidebar.button('View on GitHub'):
    st.sidebar.markdown("[GitHub Repository](https://github.com/Jotis86/Bakery-Production-Optimization-Project)")

# Always visible image
st.image("images/Bakery_2.png")

# Home
if menu == "Home":
    st.title("🥖 Bakery Production Optimization Project 🍞")
    st.markdown("""
    Welcome to the Bakery Production Optimization Project application! This application provides an overview of the project, including objectives, methodology, tools used, results, and more.

    ### About the Project
    Production in a bakery can be challenging due to the perishable nature of the products and variability in demand. This project aims to develop a machine learning model to help predict optimal production quantities, minimizing waste and improving efficiency.

    ### Issues Addressed
    - **Financial Losses**: Unsold products generate significant losses.
    - **Resource Waste**: Inefficient production results in wasted ingredients and labor.
    - **Environmental Impact**: Excess production contributes to a larger environmental footprint.

    ### Expected Benefits
    - **Reduction of Losses**: Minimize financial losses by adjusting production to actual demand.
    - **Operational Efficiency**: Improve resource use efficiency and production planning.
    - **Sustainability**: Reduce environmental impact by decreasing product waste.

    ### Application Structure
    Use the menu on the left to navigate through the different sections of the project, where you will find details about the objectives, methodology, tools used, results obtained, visualizations generated, and the interactive Power BI dashboard.
    """)


# Objectives and Methodology
elif menu == "Objectives and Methodology":
    st.title("🎯 Objectives and ⚙️ Methodology")
    st.markdown("""
    ### 🎯 Objectives
    The primary objective of this project is to develop a machine learning model to predict the optimal production quantities in a bakery. This aims to minimize waste, reduce financial losses, conserve resources, and lower the environmental footprint. The project addresses the following key issues:
    - **Financial Losses**: Unused products lead to significant financial losses.
    - **Resource Waste**: Inefficient production results in wasted ingredients and labor.
    - **Environmental Impact**: Excess production contributes to a larger environmental footprint.

    By leveraging historical sales, production, and demand data, the project seeks to create a predictive model that can accurately forecast production needs, thereby optimizing the bakery's operations.

    ### ⚙️ Methodology
    The methodology followed in this project includes the following steps:

    - **📥 Data Loading and Cleaning**: Historical sales, production, and demand data are loaded and cleaned to ensure data quality.
    - **🔍 Exploratory Data Analysis (EDA)**: Distributions and relationships between variables are visualized to better understand the dataset.
    - **🛠️ Data Preprocessing**: Numerical data is standardized and categorical variables are encoded to prepare the data for model training.
    - **🧠 Model Development and Evaluation**: Several machine learning models are developed and evaluated to predict optimal production quantities.
    - **📊 Visualization Generation**: Visualizations are generated to interpret the results and facilitate decision-making.
    - **🔮 Prediction of Optimal Production Quantities**: The trained models are used to predict optimal production quantities.
    """)

# Tools and Results
elif menu == "Tools and Results":
    st.title("🛠️ Tools and 📊 Results")
    st.markdown("""
    ### 🛠️ Tools Used
    The tools used in this project include:

    - **Python 🐍**: Main programming language used for project development.
    - **Pandas 🐼**: Library used for data manipulation and analysis.
    - **Matplotlib 📉 and Seaborn 🐟**: Libraries used for data visualization.
    - **Scikit-learn 🤖**: Library used for data preprocessing and machine learning model development.
    - **Power BI 📊**: Tool used to create interactive dashboards.

    ### 📊 Results
    The project results showed a significant reduction in unsold products, minimizing losses and improving production efficiency. The developed models allowed for accurate prediction of optimal production quantities, resulting in better planning and resource management.

    #### Key Results:
    - **Reduction of Losses**: A significant reduction in unsold products was achieved, minimizing financial losses.
    - **Improvement in Production Efficiency**: Production was optimized, resulting in more efficient use of resources and a smaller environmental footprint.
    - **Accurate Predictions**: The developed models allowed for accurate prediction of production needs, facilitating decision-making and production planning.
    """)

# Visualizations and Models
elif menu == "Visualizations and Models":
    st.title("📊 Visualizations and 🧠 Models")
    st.markdown("""
    ### 📊 Visualizations
    The visualizations generated in the project include:
    """)

    # Checkboxes to select the graphs
    sales_hour = st.checkbox("Sales trends by hour of the day 🕒")
    sales_day = st.checkbox("Sales trends by day of the week 📅")
    sales_month = st.checkbox("Quantity sold by month 📆")
    waste_year_family = st.checkbox("Waste by year and family 📉")
    waste_family = st.checkbox("Waste by family 🍞")

    # Show selected graphs
    if sales_hour:
        st.image("images/Sales by Hour.png", caption="Sales trends by hour of the day 🕒")
    if sales_day:
        st.image("images/Sales by day week.png", caption="Sales trends by day of the week 📅")
    if sales_month:
        st.image("images/Total mounth.png", caption="Quantity sold by month 📆")
    if waste_year_family:
        st.image("images/Merma by family and year.png", caption="Waste by year and family 📉")
    if waste_family:
        st.image("images/Merma by family.png", caption="Waste by family 🍞")

    st.markdown("""
    ### 🧠 Models and Metrics
    #### Model 1: Based on Product Families and Days of the Week
    - **Models Used**: Linear Regression, Decision Tree, Random Forest, Gradient Boosting
    - **Evaluation Metrics**: Mean Squared Error (MSE), Mean Absolute Error (MAE), Root Mean Squared Error (RMSE), R-squared (R2)

    #### Model 2: Based on Individual Products and Days of the Week
    - **Model Used**: Random Forest
    - **Evaluation Metrics**: Mean Squared Error (MSE), Mean Absolute Error (MAE), Root Mean Squared Error (RMSE), R-squared (R2)
    """)

# Power BI Dashboard
elif menu == "Power BI Dashboard":
    st.title("📊 Power BI Dashboard")
    st.markdown("""
    An interactive dashboard was created in Power BI to analyze the results of the predictive models and compare them with the orders placed by the manager. This dashboard allows for graphical comparison of the model predictions with actual order data, facilitating decision-making and production planning.

    ### Dashboard Features:
    - **Comparison of Predictions and Actual Orders**: Charts showing the differences between the quantities predicted by the models and the quantities actually ordered by the manager.
    - **Trend Analysis**: Visualization of sales and production trends over time.
    - **Interactivity**: Filters and slicers that allow users to explore the data dynamically and customize their view.
    """)
    st.image("images/Powerbi.png")

# Run the application with: streamlit run app.py