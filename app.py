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
# op = hc.option_bar(option_definition=option_data,title='Feedback Response',key='PrimaryOption',override_theme=over_theme,horizontal_orientation=True)


current_option_index = st.session_state.get("current_option_index", 0)

if st.button("Next"):
    current_option_index = (current_option_index + 1) % len(option_data)
    st.session_state.current_option_index = current_option_index
    op = hc.option_bar(option_data, first_select=current_option_index,override_theme=over_theme,horizontal_orientation=True)



if op == "1":
    st.write("hello 1")
elif op == "2":
    st.write("hello 2")
elif op == "3":
    st.write("hello 3")
elif op == "4":
    st.write("hello 4")
elif op == "5":
    st.write("hello 5")
elif op == "6":
    st.write("hello 6")
elif op == "7":
    st.write("hello 7")