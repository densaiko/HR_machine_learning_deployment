# main Python app
import streamlit as st
import streamlit.components.v1 as stc

#import our app
from eda_app import run_eda_app
from ml_app import run_ml_app

html_temp = """
            <div style="background-color:#3872fb;padding:10px;border-radius:10px">
		    <h1 style="color:white;text-align:center;">Forum Tentor Indonesia </h1>
		    <h4 style="color:white;text-align:center;">HR Team </h4>
		    </div>
            """

desc_temp = """
            ### Employee Promotion Prediction App
            This app will be used by the HR team to predict whether the employee get a promotion or not
            #### Data Source
            - https://raw.githubusercontent.com/densaiko/data_science_learning/main/dataset/Human%20Capital.csv
            #### App Content
            - Exploratory Data Analysis
            - Machine Learning Section
            """


def main():
    # st.title("Main App")
    stc.html(html_temp)

    menu = ["Home","Machine Learning","Exploratory Data Analysis"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("Home")
        st.markdown(desc_temp, unsafe_allow_html=True)
    elif choice == "Machine Learning":
        run_ml_app()
    elif choice == "Exploratory Data Analysis":
        run_eda_app()
    

if __name__ == '__main__':
    main()
