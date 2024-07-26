import streamlit as st
import duckdb
import pandas as pd
import openpyxl
from io import StringIO

conn = duckdb.connect(":memory:")

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
	stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
	conn.read_csv(stringio).to_table("assiduite")
	cur = conn.cursor()
	st.write(cur.sql("select * from assiduite"))