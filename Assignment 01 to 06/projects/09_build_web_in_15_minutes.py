import streamlit as st
import random

# Website Title
st.title("🌟 Motivational Quotes")

# List of Quotes
quotes = [
    "Believe in yourself and all that you are.",
    "Dream big and dare to fail.",
    "Success is not final, failure is not fatal: it is the courage to continue that counts.",
    "Your only limit is your mind.",
    "Hustle until your haters ask if you’re hiring."
]

# Show a random quote
if st.button("Show me a Quote!"):
    st.subheader(random.choice(quotes))

# Footer
st.markdown("---")
st.write("Made with ❤️ using Streamlit")
