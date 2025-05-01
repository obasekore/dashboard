import os
import streamlit as st
import pymysql
from dotenv import load_dotenv

load_dotenv()
username = os.environ.get("username")
password = os.environ.get("password")
host = os.environ.get("host")
port = os.environ.get("port")
database = os.environ.get("database")


@st.cache_resource
def get_connection():
    return pymysql.connect(
        host=username,
        user=password,
        password=host,
        database=database,
        charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor,
    )


conn = get_connection()


# Simple query
def get_plans():
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM plans")
        return cursor.fetchall()


st.set_page_config("Dashboard")

st.title("Welcome")

users = get_plans()
for user in users:
    st.write(f"{user['id']}: {user['plan']}")
# conn = st.connection("my_database")
# df = conn.query("select * from plans")
# st.dataframe(df)
