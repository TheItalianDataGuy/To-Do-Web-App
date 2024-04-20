import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)


st.image(image=r"C:\Users\andre\PycharmProjects\web_app\pythonProject\png.jpg",
         width=100)
st.title("My To-Do app")
st.subheader("This is my To-Do app.")
st.write("This app is to increase your productivity.")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="", placeholder="Add a new To-Do...",
              on_change=add_todo, key="new_todo")
