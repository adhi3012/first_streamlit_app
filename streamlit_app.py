import streamlit
import snowflake.connector

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * FROM fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("The fruit load list contains")
streamlit.dataframe(my_data_rows)
fruit_choice = streamlit.text_input('What fruit would you like to add')
streamlit.write('The user entered ', fruit_choice)


streamlit.title('My Parents New Healthy Diner')
streamlit.header('π₯£ Breakfast Menu')
streamlit.text('π₯ Omega 3 & Blueberry Oatmeal')
streamlit.text('πkale. Spinach & Rocket Smoothie')
streamlit.text('π₯π Hard-Boiled Free-Range Egg')

streamlit.header('ππ₯­ Build Your Own Fruit Smoothie π₯π')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

my_fruit_list = my_fruit_list.set_index('Fruit')

#lets put a pick list here so they can pick they wanna include
fruits_selected = streamlit.multiselect("pick some fruits:",list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

streamlit.header("Fruityvice Fruit Advice!")
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)
import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+ fruit_choice)

# take json version of the response and normalise it
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# output it the screen as a table
streamlit.dataframe(fruityvice_normalized)


my_cur.execute("insertinto fruit_load_list values ('from streamlit')")
