import streamlit as st
from snowflake.snowpark.context import get_active_session

# In-Snowflake, this gives you a session using the owning role
session = get_active_session()

# Run a SQL query and display it
df = session.sql("SELECT * FROM sales ORDER BY order_date LIMIT 100").to_pandas()
st.dataframe(df)
