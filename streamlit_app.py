import streamlit
streamlit.title('My parents new healthy diner')

streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avacado Toast')

streamlit.header('🍌🍓 Build Your Own Fruit Smoothy 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)

# put a pick list here
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
# display the table on the page
streamlit.dataframe(my_fruit_list)
