import streamlit as st
import pandas as pd
import datetime

# Streamlit App Title
st.title("💰 Budget & Expense Tracker")
st.subheader("Manage your finances effectively")

# Session State Initialization
if 'transactions' not in st.session_state:
    st.session_state['transactions'] = []
if 'budget' not in st.session_state:
    st.session_state['budget'] = 0.0

# Set Budget
st.sidebar.header("Set Monthly Budget")
st.session_state['budget'] = st.sidebar.number_input("Enter your monthly budget:", min_value=0.0, format="%.2f")

# Input for New Expense
st.header("📌 Add a New Expense")
date = st.date_input("Date", datetime.date.today())
category = st.selectbox("Category", ["Food", "Transport", "Entertainment", "Bills", "Shopping", "Other"])
description = st.text_input("Description")
amount = st.number_input("Amount", min_value=0.0, format="%.2f")

if st.button("➕ Add Expense"):
    if description and amount > 0:
        st.session_state['transactions'].append({
            "Date": date,
            "Category": category,
            "Description": description,
            "Amount": amount
        })

# Display Transactions
st.header("📋 Expense History")
if st.session_state['transactions']:
    df = pd.DataFrame(st.session_state['transactions'])
    st.dataframe(df)
else:
    st.write("No transactions added yet.")

# Expense Summary
st.header("📊 Expense Summary")
total_expense = sum(item['Amount'] for item in st.session_state['transactions'])
st.write(f"### 💸 Total Expense: ${total_expense:.2f}")
st.write(f"### 🎯 Remaining Budget: ${st.session_state['budget'] - total_expense:.2f}")

# Expense Breakdown
st.subheader("📂 Expense Breakdown by Category")
if st.session_state['transactions']:
    df_grouped = df.groupby("Category")["Amount"].sum()
    st.bar_chart(df_grouped)
else:
    st.write("No data to display.")
