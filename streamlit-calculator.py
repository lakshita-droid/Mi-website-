import streamlit as st

def main():
    st.title("Simple Calculator")
    
    # Input fields for two numbers
    st.subheader("Enter two numbers:")
    col1, col2 = st.columns(2)
    
    with col1:
        num1 = st.number_input("First Number", value=0.0)
    
    with col2:
        num2 = st.number_input("Second Number", value=0.0)
    
    # Operation buttons
    st.subheader("Choose an operation:")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        add_button = st.button("Add (+)")
    
    with col2:
        subtract_button = st.button("Subtract (-)")
    
    with col3:
        multiply_button = st.button("Multiply (×)")
    
    with col4:
        divide_button = st.button("Divide (÷)")
    
    # Result section
    st.subheader("Result:")
    result = None
    operation = ""
    
    # Perform calculations based on button clicks
    if add_button:
        result = num1 + num2
        operation = "+"
    elif subtract_button:
        result = num1 - num2
        operation = "-"
    elif multiply_button:
        result = num1 * num2
        operation = "×"
    elif divide_button:
        if num2 != 0:
            result = num1 / num2
            operation = "÷"
        else:
            st.error("Error: Cannot divide by zero!")
            result = None
    
    # Display the result
    if result is not None:
        st.success(f"{num1} {operation} {num2} = {result}")
        
        # Display calculation history in session state
        if 'history' not in st.session_state:
            st.session_state.history = []
        
        st.session_state.history.append(f"{num1} {operation} {num2} = {result}")
        
        # Show calculation history
        if st.session_state.history:
            st.subheader("Calculation History:")
            for calc in st.session_state.history:
                st.text(calc)

if __name__ == "__main__":
    main()
