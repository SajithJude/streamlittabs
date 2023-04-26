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

# display a tab for each option
for option in option_data:
    with st.tabs(f"{option['label']}"):
        st.header(f"You selected option {option['label']}")
        st.write(f"https://picsum.photos/200/300?random={option['label']}")

# display the option bar component
st.write(op)
