import logging
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

import streamlit as st


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

def render_admin() -> None:
    """Show admin view"""
    st.subheader(f"Update the app")



if __name__ == "__main__":
    main()