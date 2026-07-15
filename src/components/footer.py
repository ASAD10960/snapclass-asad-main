import streamlit as st


def footer_home():
    logo_url = "https://imgs.search.brave.com/1eqLJPTQkW2lcKB77iORNch-JTRNajTzbCR4mweQYiY/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9pLnBp/bmltZy5jb20vb3Jp/Z2luYWxzL2YwLzVm/LzA0L2YwNWYwNGNi/MDY0NjAzM2RjZWRh/OWMwYjRjNDA3OWI1/LmpwZw"
    
    st.markdown(f"""
        <div style="margin-top:2rem; display:flex; gap:6px; justify-content:center; items-align:center">
        <p style="font-weight:bold; color:white;"> Created with ❤️ by </p>  
        <img src='{logo_url}' style='max-height:25px' />
        </div>
                
                """, unsafe_allow_html=True)


def footer_dashboard():
    logo_url = "https://imgs.search.brave.com/1eqLJPTQkW2lcKB77iORNch-JTRNajTzbCR4mweQYiY/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9pLnBp/bmltZy5jb20vb3Jp/Z2luYWxzL2YwLzVm/LzA0L2YwNWYwNGNi/MDY0NjAzM2RjZWRh/OWMwYjRjNDA3OWI1/LmpwZw"
    
    st.markdown(f"""
        <div style="margin-top:2rem; display:flex; gap:6px; justify-content:center; items-align:center">
        <p style="font-weight:bold; color:black;"> Created with ❤️ by </p>  
        <img src='{logo_url}' style='max-height:25px' />
        </div>
                
                """, unsafe_allow_html=True)