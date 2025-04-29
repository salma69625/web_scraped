import streamlit as st
import pandas as pd
df = pd.read_csv("books_cleaned_with_category.csv")
num_rate=df['Rating'].value_counts().sort_index()
rate=df.groupby('Rating')['Price'].mean()
num=df['Category'].value_counts()
avg=df.groupby('Category')['Price'].mean().sort_values(ascending=False)
top_5=df[['Title', 'Price']].sort_values(by='Price', ascending=False)
cheapest_5=df[['Title', 'Price']].sort_values(by='Price')
st.title("Analyze data of web scraping 📊")
st.sidebar.title("DATA OVERVIEW")
total_books=len(df)
average_price=df["Price"].mean()
Max=df["Price"].max()
Min=df["Price"].min()
c1,c2,c3,c4=st.columns(4)
c1.metric("Total_books",total_books)
c2.metric("Highest_price",Max)
c3.metric("average_price",average_price)
c4.metric("lowest_price",Min)
#---------------------------------
st.header("1.DATAFRAME ✔️")
selected_category = st.sidebar.selectbox("Choose the category", df["Category"].unique())
selected_rate=st.sidebar.slider("Choose the rating",1,5,1)
filtered_books = df[(df["Category"] == selected_category) & (df["Rating"]==selected_rate) ]
st.dataframe(filtered_books)
c1.image("avg_price_by_rating.png",caption='avg_price_by_rating.png')
c2.image("price_vs_rating_swarm.png",caption='price_vs_rating_swarm.png')
c3.image("rating_distribution.png",caption='rating_distribution.png')
c4.image("top_categories_vertical.png",caption='top_categories_vertical.png')
st.header("2.TOP_5 🔝")
st.dataframe(top_5.head())
st.header("3.CHEAPEST_5")
st.dataframe(cheapest_5.head())
st.header("4.NUMBER OF BOOKS PER RATING")
st.dataframe(num_rate)
st.header("5.AVERAGE PRICE BY RATING")
st.dataframe(rate)
st.header("6.NUMBER OF BOOKS IN EACH CATEGORY")
st.dataframe(num)
st.header("7.AVERAGE PRICE IN EACH CATEGORY")
st.dataframe(avg)
st.sidebar.write("Download File")
st.sidebar.download_button(
    label="Download File",
    data=df.to_csv(index=False),
    file_name="books_cleaned_with_category.csv",
    mime='text/csv'
)
