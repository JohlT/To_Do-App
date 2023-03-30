import streamlit as st
import functions

To_Do = functions.get_To_Do()

st.set_page_config(layout="wide")

def add_todo():
    to_do = st.session_state['new_todo'] + "\n"
    To_Do.append(to_do)
    functions.store_To_Do(To_Do)


st.title("My Todo App")
st.subheader("Staying Organized and Consistant")
st.write("<b>This app is to increase your productivity</b>", unsafe_allow_html=True)

st.text_input(label="", placeholder="Add new item", on_change=add_todo, key='new_todo')

for index, todo in enumerate(To_Do):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        To_Do.pop(index)
        functions.store_To_Do(To_Do)
        del st.session_state[todo]
        st._rerun()
    



