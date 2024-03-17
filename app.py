import streamlit as st
import os

def main():
    st.title("Hello World!")
    st.write("Hello yourself. Trying to get this thing deployed.")
    sample_key = os.environ.get('KEY')
    st.write(sample_key)

if __name__ == "__main__":
    main()
