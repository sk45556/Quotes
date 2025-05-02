import streamlit as st
import os

FILE_NAME = "quotes.txt"

# Title
st.title("📜 Favorite Quotes App")

# Option selector
option = st.radio("Choose an action:", ("Add a Quote", "View All Quotes", "Search Quotes by Name"))

# Function to add quote
def add_quote(name, quote):
    with open(FILE_NAME, "a", encoding="utf-8") as f:
        f.write(f"{name}::{quote}\n")
    st.success("Quote added successfully!")

# Function to read all quotes
def get_all_quotes():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r", encoding="utf-8") as f:
        return [line.strip().split("::") for line in f.readlines()]

# Add a quote
if option == "Add a Quote":
    st.subheader("Add Your Favorite Quote")
    name = st.text_input("Your Name")
    quote = st.text_area("Your Favorite Quote")

    if st.button("Submit"):
        if name and quote:
            add_quote(name, quote)
        else:
            st.warning("Please enter both name and quote.")

# View all quotes
elif option == "View All Quotes":
    st.subheader("All Saved Quotes")
    quotes = get_all_quotes()
    if quotes:
        for name, quote in quotes:
            st.markdown(f"**{name}** says: _\"{quote}\"_")
    else:
        st.info("No quotes saved yet.")

# Search quotes by name
elif option == "Search Quotes by Name":
    st.subheader("Search Quotes")
    search_name = st.text_input("Enter the name to search for")

    if st.button("Search"):
        quotes = get_all_quotes()
        found = [q for q in quotes if q[0].lower() == search_name.lower()]
        if found:
            for name, quote in found:
                st.markdown(f"**{name}** says: _\"{quote}\"_")
        else:
            st.warning("No quotes found for that name.")