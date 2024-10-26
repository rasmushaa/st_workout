import streamlit as st


st.title('You are at the Main Page!')


col1, col2, col3 = st.columns(3)

with col1 as col:
    if st.button(label='', icon=":material/settings:"):
        st.switch_page('pages/menu.py')

with col3 as col:
    st.button(label='', icon=":material/logout:")

with st.empty().container():
    st.write(st.session_state.user.id)
    st.write(st.session_state.user.name)
    st.write(st.session_state.user.role)
    st.write(st.session_state.user.is_logged_in)