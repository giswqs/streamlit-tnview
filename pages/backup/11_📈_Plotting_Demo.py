import streamlit as st

st.title("Plotting Demo")

markdown = """
Web App URL: <https://tnview.gishub.org>
TNView website: <https://tnview.utk.edu>
Contact: [Dr. Qiusheng Wu](https://wetlands.io)
"""

st.sidebar.info(markdown)
st.sidebar.image("https://i.imgur.com/qXqRBda.png")
