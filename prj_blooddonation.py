import streamlit as st
import pandas as pd
import mysql.connector
from mysql.connector import Error

#Create connection
def test_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Mysql@1985",  # Replace with your password
            database="db_blooddonation"  # Replace with your database name
        )
        if connection.is_connected():
            print("Connection successful!")
            return connection
    except Error as e:
        print(f"Error: {e}")
 
#test_connection()
#fetch records
def fetchData():
    conn = test_connection()
    if conn:
        try:
            query = "SELECT * FROM donors"
            donors = pd.read_sql(query, conn)
            return donors
        except Error as e:
            st.error(f"Error while fetching donor data: {str(e)}")
        finally:
            conn.close()
    else:
        return pd.DataFrame()  # Return an empty DataFrame if connection fails

#insert data to donor table
def insert_donor(name,age,blood_type,contact):
    conn=test_connection()
    cursor=conn.cursor()
    query="insert into donors(name,age,blood_type,contact) values(%s,%s,%s,%s);"
    cursor.execute(query,(name,age,blood_type,contact))
    conn.commit()
    conn.close()

st.title("Blood donation camp")
st.subheader("Registered users")
df=fetchData()
st.dataframe(df)
st.subheader("Registration - Form")
with st.form("regisration-Form"):
    name=st.text_input("Full Name")
    age=st.number_input("Age",min_value=18,max_value=60)
    blood_type=st.selectbox("blood type",["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"])
    contact=st.text_input("Contact number")
    submit=st.form_submit_button("register")
    if submit:
        insert_donor(name,age,blood_type,contact)
        st.success("Success fully registerd")
        st.rerun()
        fetchData()
st.subheader("Filter by Blood type")
with st.form("Form"):
    donors_df = fetchData()
    blood_type=st.selectbox("blood type",["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"])
    submit=st.form_submit_button("Search")
    filtered_donors = donors_df[donors_df["blood_type"] == blood_type]
    st.write(f"Showing donors with blood type: {blood_type}")
    st.dataframe(filtered_donors)
