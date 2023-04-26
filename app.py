import streamlit as st
import hydralit_components as hc

# define what option labels to display
option_data = [
   {'label':"1"},
   {'label':"2"},
   {'label':"3"},
   {'label':"4"},
   {'label':"5"},
   {'label':"6"},
   {'label':"7"},
]

# override the theme, else it will use the Streamlit applied theme
over_theme = {'txc_inactive': 'white','menu_background':'purple','txc_active':'yellow','option_active':'blue'}

# set the current state of the option bar
if "current_state" not in st.session_state:
    st.session_state.current_state = 0

# display a version version of the option bar
op = hc.option_bar(option_definition=option_data, first_select=st.session_state.current_state, title='Feedback Response', key='PrimaryOption', override_theme=over_theme, horizontal_orientation=True)

# check if the "Next" button has been clicked
tab1, tab2, tab3 = st.tabs(["", "", ""])

with tab1:
   st.header("A cat")
   st.image("https://static.streamlit.io/examples/cat.jpg", width=200)

with tab2:
   st.header("A dog")
   st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

with tab3:
   st.header("An owl")
   st.image("https://static.streamlit.io/examples/owl.jpg", width=200)