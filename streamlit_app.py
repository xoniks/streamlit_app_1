import streamlit as st

num_1 = st.number_input('Insert a number',key=1)
num_2 = st.number_input('Insert a number',key=2)


def add_two(num_one, num_two):
    result = num_one + num_two
    return result

def divide_two(num_one, num_two):
    if num_2==0:
        return "Division with zero"
    else:
        return num_one/num_two


total_sum = add_two(num_1, num_2)
total_divide = divide_two(num_1, num_2)

if st.button('Sum '):
    st.write('The result is ', total_sum)

if st.button('Divide '):
    st.write('The result is ', total_divide)