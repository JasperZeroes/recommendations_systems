"""

    Streamlit webserver-based Recommender Engine.

    Author: Explore Data Science Academy.

    Note:
    ---------------------------------------------------------------------
    Please follow the instructions provided within the README.md file
    located within the root of this repository for guidance on how to use
    this script correctly.

    NB: !! Do not remove/modify the code delimited by dashes !!

    This application is intended to be partly marked in an automated manner.
    Altering delimited code may result in a mark of 0.
    ---------------------------------------------------------------------

    Description: This file is used to launch a minimal streamlit web
	application. You are expected to extend certain aspects of this script
    and its dependencies as part of your predict project.

	For further help with the Streamlit framework, see:

	https://docs.streamlit.io/en/latest/

"""
# Streamlit dependencies
import streamlit as st

# Data handling dependencies
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy as sp
from sklearn.metrics.pairwise import cosine_similarity

# Custom Libraries
from utils.data_loader import load_movie_titles
from recommenders.collaborative_based import collab_model
from recommenders.content_based import content_model

# Data Loading
title_list = load_movie_titles('resources/data/movies.csv')
# load additional files
# imdb_df = pd.read_csv('resources/data/imdb_data.csv')
ratings_df = pd.read_csv('resources/data/ratings.csv')
movie_df = pd.read_csv('resources/data/movies.csv')
# App declaration


def main():

    # DO NOT REMOVE the 'Recommender System' option below, however,
    # you are welcome to add more options to enrich your app.
    page_options = ["Company Profile", "About the Project", "Solution Overview", "Recommender System",
                    "Movies Heatmap", "Team"]

    # -------------------------------------------------------------------
    # ----------- !! THIS CODE MUST NOT BE ALTERED !! -------------------
    # -------------------------------------------------------------------
    page_selection = st.sidebar.selectbox("Choose Option", page_options)
    if page_selection == "Recommender System":
        # Header contents
        st.write('# Movie Recommender Engine')
        st.write('### EXPLORE Data Science Academy Unsupervised Predict')
        st.image('resources/imgs/Image_header.png', use_column_width=True)
        # Recommender System algorithm selection
        sys = st.radio("Select an algorithm",
                       ('Content Based Filtering',
                        'Collaborative Based Filtering'))

        # User-based preferences
        st.write('### Enter Your Three Favorite Movies')
        movie_1 = st.selectbox('Fisrt Option', title_list[14930:15200])
        movie_2 = st.selectbox('Second Option', title_list[25055:25255])
        movie_3 = st.selectbox('Third Option', title_list[21100:21200])
        fav_movies = [movie_1, movie_2, movie_3]

        # Perform top-10 movie recommendation generation
        if sys == 'Content Based Filtering':
            if st.button("Recommend"):
                try:
                    with st.spinner('Crunching the numbers...'):
                        top_recommendations = content_model(movie_list=fav_movies,
                                                            top_n=10)
                    st.title("We think you'll like:")
                    for i, j in enumerate(top_recommendations):
                        st.subheader(str(i+1)+'. '+j)
                except:
                    st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")

        if sys == 'Collaborative Based Filtering':
            if st.button("Recommend"):
                try:
                    with st.spinner('Crunching the numbers...'):
                        top_recommendations = collab_model(movie_list=fav_movies,
                                                           top_n=10)
                    st.title("We think you'll like:")
                    for i, j in enumerate(top_recommendations):
                        st.subheader(str(i+1)+'. '+j)
                except:
                    st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")

    # -------------------------------------------------------------------

    # ------------- SAFE FOR ALTERING/EXTENSION -------------------

    if page_selection == "Company Profile":
        #st.title("TriTech Inc. Company Profile")
        st.image("resources/imgs/tritech.jpeg", width=400)
        st.write("""
        TriTech Inc. was established in April 2015 to provide digital technology solutions for a wide range of domain businesses. Our founding mission was to cultivate professional relationships with our customers to provide reliable cutting edge technological solutions for their requirements. """)
        st.write("\n")
        st.write("""The team at TriTech Inc. is equipped with a wide range of cross-domain skillset developed over years of experience not only in information technology but also in business processes, financial services, construction and telecommunications across a range of various subdomains.
        This business experience makes service offerings uniquely positioned to provide solutions promising better cost savings, operational efficiency and productivity gains for each of our customers, regardless of their industry.
        """)
        st.write("\n")
        st.write("""As a well established technology-agnostic company, we pride ourselves on providing a detailed suite of futuristic solutions. These comprise of digital automation consultancy, technology transformation services, custom AI solutions and Machine Learning software as well as enterprise architecture establishment.
        Our team consistently delivers state-of-the-art services across different domains including, integrated digital business solutions, AI & ML applications, IOT and digital transformation and/or management services.
        """)
        st.write("\n")
        st.write("""At TriTech Inc., we guarantee rapid, reliable and robust turn-key digital solutions that will transform your business.""")
    if page_selection == "Solution Overview":
        st.title("Solution Overview")
        st.info("This page details our solution comprehensively")
        st.markdown("#### Collaborative-based vs Content-based filtering")
        st.markdown(
            "**We used 2 different approaches to do our movie recommendation solution:**")
        st.write("+ **Collaborative-based filtering**")
        st.write("""With this approach, the application will recommend movies to a specific user based on how they rated movies compared to other users. \n If for example a user gave a 5 star rating Toy Story 1 then the application will recommend movies based on what other users watched who rated Toy Story 1 at 5 star.
        """)
        st.write("+ **Content-based filtering**")
        st.write("""In conrast, with content based filtering, the application will recommend movies based on the movies content. If the user rated Drama or Comedy movies at 5 star then the a user will be recommended with Drama or Comedy that they have not watched. \n Alternatively, a movie can be recommended if the user liked movies by a certain Director, Production House or movies with a specific Actor.
        """)
        st.markdown("""
        #### We used the models below to test our movie recommendations:
           + KNNBasic
           + KNNMeans
           + KNNWithZScore
           + SVD
           + Baseline
           + NormalPredictor
            """)
        st.markdown("""
        ##### The image below displays how different models perfomed based on the RMSE score \n
            """)
        st.image("resources/imgs/model_comparison.png")
        st.write("""
        The SVD model gave an RMSE score of 0.813.
        A low RMSE score means the model performs well because it means the difference between what our movie application recommended 
        and what the user actually liked is low. \n
            """)
        st.write("""
        With this in mind, we can understand that our graph tells us that SVD model was the best performing model to do our prediction meaning it gave the best results. \n
            """)
        st.markdown("""
        #### Singular Value Decomposition (SVD)
        SVD is a technique that is used to break down a large matrix into smaller, simpler pieces. The idea behind this is to make it easier to understand and work with the data that is contained within that matrix. \n
        SVD is also used to reduce the dimensionality of the data which can help to improve the efficiency of the algorithm and also help to improve the model's generalization capabilities. \n
        """)
    if page_selection == "Movies Heatmap":
        st.title("Movie Heatmap")
        st.info(
            "This page shows a heatmap of the movie ratings for a few titles in the dataset")
        df_out = ratings_df.join(movie_df.set_index('movieId'), on='movieId')

        # Create a neat version of the utility matrix to assist with plotting book titles
        #df_out['rating'] = df_out['rating'].astype(int)
        util_matrix_neat = df_out.iloc[:100].pivot_table(index=['movieId'],
                                                         columns=['title'],
                                                         values='rating')

        fig, ax = plt.subplots(figsize=(20, 10))
        # We select only the first 100 users for ease of computation and visualisation.
        # You can play around with this value to see more of the utility matrix.
        _ = sns.heatmap(util_matrix_neat[:100], annot=False, ax=ax).set_title(
            'Movies Ratings')
        st.pyplot(fig)
    if page_selection == "About the Project":
        st.title("A movie recommendation system")
        st.info(
            "This page provides a comprehensive and detailed description of the movie recommendation system")
        st.image("resources/imgs/dc_marvel.webp")
        st.markdown("""
        In today’s technology driven world, recommender systems are socially and 
        economically critical for ensuring that individuals can make appropriate 
        choices surrounding the content they engage with on a daily basis. One 
        application where this is especially true surrounds movie content recommendations; 
        where intelligent algorithms can help viewers find great titles from tens of 
        thousands of options.""")

        st.markdown("""...ever wondered how Netflix, Amazon Prime, Showmax, Disney and the likes somehow 
        know what to recommend to you?
        \n ...it's not just a guess drawn out of the hat. There is an algorithm behind it.
        \n With this context, EDSA is challenging you to construct a recommendation algorithm 
        based on content or collaborative filtering, capable of accurately predicting how a 
        user will rate a movie they have not yet viewed based on their historical preferences.
        \n What value is achieved through building a functional recommender system?
        Providing an accurate and robust solution to this challenge has immense economic potential, 
        with users of the system being exposed to content they would like to view or purchase - 
        generating revenue and platform affinity.""")

    if page_selection == "About TriTech Inc.":
        st.info(
            "Below is detailed information about the our business and the team")
    if page_selection == "Team":
        st.title(
            "About the team")
        st.info(
            "Read the profile of TriTech Inc. leadership team below")
        tab1, tab2, tab3, tab4 = st.tabs(
            ["Chima", "Kazeem", "Thepe", "Dotun"])

        with tab1:
            st.subheader("Chima Enyeribe")
            st.markdown("#### Chief Executive Officer")
            st.image("resources/imgs/Jasper.jpg", width=200)
            st.write("""
            Chima Enyeribe is the founder and CEO of TriTech Inc., a position he has held since the company's inception in April 2015. Prior to founding TriTech, Chima worked for Zen Bank in Nigeria, providing financial service solutions to individuals and corporates across 19 countries in Africa, Latin America and Asia.
            Under his leadership, the Bank serviced over 5 million customers and had $3 million of assets under management.
            Chima is a seasoned business leader with experience in engineering, financial services and construction. Since founding TriTech, Chima has played a pivotal role in the strengthening the company's financial position, strategy formulation and successful listing on the Nigerian and Ghanaian Stock Exchanges.
            """)
            st.markdown("jasperobed@gmail.com")
        with tab2:
            st.subheader("Kazeem Okunola")
            st.markdown("#### Chief Financial Officer")
            st.image("resources/imgs/kazeem.webp", width=200)
            st.write("""
            Kazeem is a co-founder and Chief Financial Officer of TriTech Inc. Kazeem previously worked at Central Bank of Nigeria where he held the positions of Deputy Chief Financial Officer and Executive Risk and Compliance Officer, prior to him co-founding TriTech Inc. and becoming the Chief Financial officer in 2015.
            Before working at the Central Bank of Nigeria, Kazeem was employed as a Finance Director of MSC Telco Holdings, and an executive director of the company's main board. He has also held various other roles at MSC Telco Holdings.
            In addition to his, extensive financial industry experience, Kazeem has also worked in the consulting and services. He brings with him extensive financial strategy, financial management and accounting experience, with a strong background in enterprise risk management and financial controls.
            """)
            st.markdown("achieverk2@gmail.com")
        with tab3:
            st.subheader("Thepe Mashala")
            st.markdown("#### Chief Operations Officer")
            st.image("resources/imgs/8324.jpg", width=200)
            st.write("""
            Thepe Mashala joined TriTech Inc. in March 2018. Prior to his appointment as the Chief Operations Officer, he led the establishment of Blue Sky Group's strategic M&A business, the launch of the Group's flagship Advanced Data Analytics platform, and
            helped shape the Group's strategic direction across a range of key topics.
            Before joining TriTech Inc., Thepe led the Southern Africa Digital Practice for McKinsey & Company, where he focused on Digital Business Building and operational transformations for telecommunications businesses, financial services, and SMME sector clients.
            """)
            st.markdown("tpmashala@gmail.com")
        with tab4:
            st.subheader("Dotun Olasogba")
            st.markdown("#### Chief Digital Officer")
            st.image("resources/imgs/dotun.jpeg", width=200)
            st.write("""
            Dotun joined TriTech Inc. in 2020 from MMB, where he led the debt-based financing business and was responsible for financing solutions, digital transformation and M&A execution.
            Dotun's experience and leadership capacity is important to the company's digital portfolio optimisation drive, itself key to the strategy. This includes the digital transformation
            realisation programme, which aims to reduce legacy systems, simplify the digital operations portfolio, reduce risk, improve digital footprint and take advantage of expansion opportunities.
            """)
            st.markdown("dotunolasogba@yahoo.com")
        # You may want to add more sections here for aspects such as an EDA,
        # or to provide your business pitch.


if __name__ == '__main__':
    main()
