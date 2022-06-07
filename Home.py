import streamlit as st


st.set_page_config(layout="wide")

st.title("TNView")


markdown = """
Web App URL: <https://tnview.gishub.org>
TNView webiste: <https://tnview.utk.edu>
Contact: [Dr. Qiusheng Wu](https://wetlands.io)
"""

st.sidebar.info(markdown)

st.sidebar.image("https://i.imgur.com/qXqRBda.png")