import logging
from src.formatting import display_timestamp
from src.models import Todo
from src.services import TodoService

import streamlit as st

logging.basicConfig(format="%(levelname)s:%(message)s", level=logging.DEBUG)


def main() -> None:
    """Main Streamlit App Entry"""
    st.header(f"Hello World!")
    render_sidebar()


def render_sidebar() -> None:
    """Provides Selectbox Drop Down for which view to render"""
    PAGES = {
        "Home": render_home,
        "Admin": render_admin,
    }
    choice = st.sidebar.radio("Go To Page:", PAGES.keys())
    render_func = PAGES.get(choice)
    render_func()


def render_home() -> None:
    """Show Home Page"""
    st.subheader(f"Home Page")

    st.success("Reading Todo Feed")
    todos = TodoService.list_all_todos()
    with st.expander("Raw Todo Table Data"):
        st.table(todos)

    for todo in todos:
        render_todo(todo)


def render_todo(todo: Todo) -> None:
    """Show a todo with streamlit display functions"""
    st.subheader(f"By {todo.username} at {display_timestamp(todo.created_timestamp)}")
    st.caption(
        f"Todo #{todo.todo_id} -- Updated at {display_timestamp(todo.updated_timestamp)}"
    )
    st.write(todo.body)
    if todo.completed_timestamp is not None:
        st.success(f":tada: Completed at {display_timestamp(todo.completed_timestamp)}")
    else:
        st.warning(f"Not yet completed")


def render_admin() -> None:
    """Show admin view"""
    st.subheader(f"Update the app")


if __name__ == "__main__":
    main()
