# Function to find the largest value of the three numbers

import streamlit as st

def main():
    st.title("Find the Largest Value of the Three Numbers")
    
    n1 = st.number_input("Enter the first number:")
    n2 = st.number_input("Enter the second number:")
    n3 = st.number_input("Enter the third number:")
    
    if st.button("Display Largest"):
        largest = max(n1, n2, n3)
        st.write(f"The Largest Value is: {largest}")
main()
