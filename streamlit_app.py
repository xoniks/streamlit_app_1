import streamlit as st

num_1 = st.number_input('Insert a number',key=1)
num_2 = st.number_input('Insert a number',key=2)


def add_two(num_one, num_two):
    result = num_one + num_two
    return result


total = add_two(num_1, num_2)

if st.button('Sum '):
    st.write('The result is ', total)
