import streamlit as st
import time


myBar = st.progress(0)
for num in range(100):
    time.sleep(0.01)  # Simulate some work being done
    myBar.progress(num + 1)
    
with st.spinner("Loading..."):
    time.sleep(1)
st.success("Done!")
st.error("Error!")
st.warning("Warning!")
st.info("Info!")

e = RuntimeError('Error!')
st.exception(e)

st.snow()
st.balloons()
    
    
    
    