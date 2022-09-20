import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

markdown = """
Web App URL: <https://tnview.gishub.org>
TNView website: <https://tnview.utk.edu>
Contact: [Dr. Qiusheng Wu](https://wetlands.io)
"""

st.sidebar.info(markdown)
st.sidebar.image("https://i.imgur.com/qXqRBda.png")


st.title("Split-panel Map")

with st.expander("See source code"):
    with st.echo():
        m = leafmap.Map()
        m.split_map(
            left_layer='ESA WorldCover 2020 S2 FCC', right_layer='ESA WorldCover 2020'
        )
        m.add_legend(title='ESA Land Cover', builtin_legend='ESA_WorldCover')

m.to_streamlit(height=700)
