import streamlit as st

st.title('Largest Number Among Three Nos.')
a = st.number_input('Enter 1st number')
b = st.number_input('Enter 2nd number')
c = st.number_input('Enter 3rd number')
if((a>b)and(a>c)):
  result=a
  st.write(' Largest No = ', result)
elif((b>a)and(b>c)):
  result=b
  st.write(' Largest No = ', result)
elif((c>a)and(c>b)):
  result=c
  st.write(' Largest No = ', result)
