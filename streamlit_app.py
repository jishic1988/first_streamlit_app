
import streamlit

streamlit.title('My parents new healthy diner')

streamlit.header('Breakfast Favourites')
streamlit.text('\N{bowl with spoon}Omega3 and Blueberry oatmeal')
streamlit.text('\N{leafy green}Kale, Spinach and Rocket smoothie')
streamlit.text('\N{chicken}Hard Boiled free range egg')
streamlit.text('\N{avocado}\N{bread}Avocado Toast')
streamlit.header('\N{banana}\N{mango}Build your own fruit smoothie \N{cherries}\N{watermelon}')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
streamlit.dataframe(fruits_to_show)

streamlit.header("Fruityvice Fruit Advice!")

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response)
