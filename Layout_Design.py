import streamlit as st


def main():
    """Basics on st.beta columns/layout"""

    menu = ["Home", "Search", "About"]

    choice = st.sidebar.selectbox("Menu", menu)

    if choice == 'Home':
        st.subheader("Home")
        st.success("Full layout")
        st.text("Sidebar")

        #Using st.columns  (st.beta is no more in use)
        col1,col2,col3 = st.columns([2,2,1])
    #Method 1
        col1.success("First column")
        col1.button("Hello from C1")

        col2.success("Second column")
        col2.button("Hello From C2")

        col3.success("Third column")
        #st.write(dir(col3))
        col3.button("Hello From C3")

#Method 2 " Context Manager
        with col1:
            search = st.text_area("enter Text Here")
            if st.button("Submit"):
                st.write(search.upper())


        with col2:
            year = st.number_input("Year", 1995,2020)


    elif choice == 'Search':
        st.subheader("Search")

    else:
        st.subheader("About")

if __name__ == '__main__':
    main()






