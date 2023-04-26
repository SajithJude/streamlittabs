import streamlit as st
import hydralit_components as hc

# define what option labels and icons to display
option_data = [
   {'icon': "bi bi-hand-thumbs-up", 'label':"Agree"},
   {'icon':"fa fa-question-circle",'label':"Unsure"},
   {'icon': "bi bi-hand-thumbs-down", 'label':"Disagree"},
]

# override the theme, else it will use the Streamlit applied theme
over_theme = {'txc_inactive': 'white','menu_background':'purple','txc_active':'yellow','option_active':'blue'}
font_fmt = {'font-class':'h2','font-size':'150%'}

# set the current state of the option bar
current_state = 0

# display a version version of the option bar
op = hc.option_bar(option_definition=option_data[current_state:],title='Feedback Response',key='PrimaryOption',override_theme=over_theme,font_styling=font_fmt,horizontal_orientation=True)

# check if the "Next" button has been clicked
if st.button("Next"):
    # update the current state of the option bar
    current_state += 1
    # display a horizontal version of the option bar with the updated state
    op = hc.option_bar(option_definition=option_data[current_state:],title='Feedback Response',key='PrimaryOption',override_theme=over_theme,font_styling=font_fmt,horizontal_orientation=True)
