import streamlit as st
from streamlit_option_menu import option_menu

# Sidebar menu
with st.sidebar:
    menu = option_menu(
        menu_title="Vinsup",  # Title of the sidebar menu
        options=["Home", "about", "contact"],  # Menu options
    )

# Page content based on menu selection
if menu == "Home":
    st.title("Welcome to Vinsup")
    col1, col2 = st.columns(2)
    with col1:
        # Image 1 (Use a real image URL)
        st.image("https://upload.wikimedia.org/wikipedia/commons/4/4a/Motherboard_Sample.jpg")

        st.write("""
        Technology, encompassing tools and systems derived from scientific knowledge, has become deeply integrated into modern life, 
        impacting various sectors like communication, healthcare, education, and more. It offers increased efficiency and convenience 
        but also presents challenges related to dependence, pollution, and potential misuse.
        """)

    with col2:
        # Image 2 (Use another real image URL)
        st.image("https://upload.wikimedia.org/wikipedia/commons/6/6f/Artificial_Intelligence_%26_AI_%26_Machine_Learning_-_30212411048.jpg")

        st.write("""
        Technology, in its essence, is the application of scientific knowledge for practical purposes, often involving the creation 
        of tools and processes to solve problems or improve existing systems. It can be broadly categorized into different types, 
        including information technology, basic technologies, and sustainable technologies.
        """)

        st.text_input("Email")

elif menu == "about":
    st.title("About Vinsup")
    st.write("This is the About page for Vinsup. Here we describe what we do.")

elif menu == "contact":
    st.title("Contact Vinsup")
    st.write("This is the Contact page. You can reach us here.")

