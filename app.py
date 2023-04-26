import streamlit as st
import hydralit_components as hc

# define what option labels and icons to display
option_data = [
   { 'label':"1"},
   {'label':"2"},
   { 'label':"3"},
   { 'label':"4"},
   {'label':"5"},
   { 'label':"6"},
   { 'label':"7"}

]

# override the theme, else it will use the Streamlit applied theme
over_theme = {'txc_inactive': 'white','menu_background':'#2953b3','txc_active':'#2953b3','option_active':'white'}
# font_fmt = {'font-class':'h2','font-size':'150%'}

# display a horizontal version of the option bar
op = hc.option_bar(option_definition=option_data,title='Feedback Response',key='PrimaryOption',override_theme=over_theme,horizontal_orientation=True)

# display a version version of the option bar
# op2 = hc.option_bar(option_definition=option_data,title='Feedback Response',key='PrimaryOption',override_theme=over_theme,font_styling=font_fmt,horizontal_orientation=False)
