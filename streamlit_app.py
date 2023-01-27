
import streamlit
import pandas
streamlit.title('My Parents new healthy diner')
streamlit.header('🥣 Breakfast Menu')
streamlit.text('🥗 Omega 3 blueberry menu')
streamlit.text('🥑Spinatch smoothie')
streamlit.text('🐔 Harb boiled egg ')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

my_fruit_list = my_fruit_list.set_index('Fruit')


# Let's put a pick list here so they can pick the fruit they want to include 
fruit_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruit_selected_data=my_fruit_list.loc[fruit_selected]


# Display the table on the page.
streamlit.dataframe(fruit_selected_data)







