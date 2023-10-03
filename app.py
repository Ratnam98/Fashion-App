import streamlit as st
from multimodalsearch import MultiModalSearch

st.set_page_config(layout='wide',page_title="Fashion App")

def main():
    
    st.markdown("<h1 style='text-align: center; color:green;'>Fashion Cloth Search App</h1>",unsafe_allow_html=True)

    multimodal_search=MultiModalSearch()
    query=st.text_input("Enter Your Query",placeholder="Show me some good clothes")
    if st.button("Search"):
        if len(query)>0:
            results=multimodal_search.search(query)
            st.info("Your query was " +query)
            st.subheader("Search Results")
            col1 ,col2 ,col3=st.columns([1,1,1])
            
            with col1:
                st.write(f"Score: {round(results[0].score*100,2)}%")
                st.image(results[0].content,use_column_width=True)
            with col2:
                st.write(f"Score: {round(results[1].score*100,2)}%")
                st.image(results[1].content,use_column_width=True)
            with col3:
                st.write(f"Score: {round(results[2].score*100,2)}%")
                st.image(results[2].content,use_column_width=True)
        else:
            st.warning("Enter your query....")
            



if __name__ == "__main__":
    main()