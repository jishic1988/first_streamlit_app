
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
streamlit.dataframe(my_fruit_list)
