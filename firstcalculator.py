import streamlit as st
import pandas as pd
from calculator import add,sub,mul,div,mod,power
col1,col2=st.columns([3,1])
with col1:
    st.title("🧮 Simple Calculator")
with col2:
    st.image("icon.png",width=100)
st.divider()
st.subheader(":red[Developed by Smita kol👧]")
dataframe=pd.DataFrame({"Operation":["Addition","Subtraction","Multiplication","Division","Module","Power"],
                        "Symbol":["➕","➖","✖️ ","/","➗ ","**"]})
st.write("Arithmetic operations",dataframe)
num1=st.number_input("Enter first number")
num2=st.number_input("Enter second number")
operation=st.selectbox("Select operation",("Addition","Subtraction","Multiplication","Division","Module","Power"))
if st.button("Calculate"):
    if operation=="Addition":
        result=add(num1,num2)
        st.success(f"The result of {num1} + {num2} is {result}")
    elif operation=="Subtraction":
        result=sub(num1,num2)
        st.success(f"The result of {num1} - {num2} is {result}")
    elif operation=="Multiplication":
        result=mul(num1,num2)
        st.success(f"The result of {num1} * {num2} is {result}")
    elif operation=="Division":
            result=div(num1,num2)
            st.success(f"The result of {num1} / {num2} is {result}")
    elif operation=="Module":
         result=mod(num1,num2)
         st.success(f"The result of {num1} % {num2} is {result}")
    elif operation=="Power":
         result=power(num1,num2)
         st.success(f"The result of {num1} ** {num2} is {result}")
    else:
        st.error("Invalid operation")
st.subheader(":green[Thank you for using the calculator !]")       
st.divider()
pages = ["Simple Calculator","Percentage / GST calculator","Age calculator","BMI calculator","Loan EMI calculator","Home","About","Save Results","Save Results as PDF","History"]
pg = st.sidebar.radio("Menu",pages)
