import streamlit as st
import pandas as pd
import numpy as np

# import visualization package
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import seaborn as sns
import plotly.express as px

@st.cache
def load_data(data):
    df = pd.read_csv(data)
    df = df.iloc[:,1:]
    return df


def run_eda_app():
    st.subheader("From Exploratory Data Analysis")
    df = load_data("human_capital.csv")
    df_descriptive = load_data("type_null.csv")
    age_viz = load_data("age_viz_composition.csv")
    # st.dataframe(df)

    submenu = st.sidebar.selectbox("SubMenu",["Description","Plots"])
    if submenu == "Description":
        st.dataframe(df)

        with st.expander("Dataset Summary"):
            st.dataframe(df_descriptive)
        
        with st.expander("Descriptive Summary"):
            st.dataframe(df.describe())

        with st.expander("Promotion Distribution"):
            st.dataframe(df["is_promoted"].value_counts())

        with st.expander("Gender Distribution"):
            st.dataframe(df["gender"].value_counts())

    elif submenu == "Plots":
        st.subheader("Plots")

        # layouts
        col1,col2 = st.columns([2,1])

        with col1:
            with st.expander("Dist Plot of Gender"):
                # fig = plt.figure()
                # sns.countplot(x=df['gender'])
                # st.pyplot(fig)

                gen_df = df['gender'].value_counts().to_frame()
                gen_df = gen_df.reset_index()
                gen_df.columns = ['Gender Type', 'Counts']
                # st.dataframe(gen_df)

                p1 = px.pie(gen_df, names='Gender Type', values='Counts')
                st.plotly_chart(p1, use_container_width=True)
            
            # for Class Distribution
            with st.expander("Dist Plot of Education"):
                fig = plt.figure()
                sns.countplot(x=df['education'])
                st.pyplot(fig)

        with col2:
            with st.expander("Gender Distribution"):
                st.dataframe(gen_df)

            with st.expander("Education Distribution"):
                st.dataframe(df['education'].value_counts().to_frame())

        with st.expander("Frequency Distribution of Age"):
            p2 = px.bar(age_viz, x='age_viz', y='values', text='label')
            st.plotly_chart(p2)

        with st.expander("Correlation Plot"):
            columns = df.select_dtypes(include=['int64','float64']).columns.to_list()
            corr_matrix = df[columns].corr()
            fig = plt.figure(figsize=(20,10))
            sns.heatmap(corr_matrix, annot=True, cmap="crest", linewidth=.5, annot_kws={"size":15})
            st.pyplot(fig)

    else:
        st.write("Gorila Coklat")

