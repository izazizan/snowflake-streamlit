import streamlit
import pandas

streamlit.title('Sample Text')
fruits = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

streamlit.multiselect("Select some fruits: ", list(fruits.index))
streamlit.dataframe(fruits)
