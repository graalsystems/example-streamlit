import streamlit as st


def main():
    st.title('Streamlit App')

    # Text input example
    user_input = st.text_input('Enter your name', 'Type here...')
    st.write('Hello,', user_input)

    # Slider example
    age = st.slider('Select your age', 0, 100, 25)
    st.write('Your age is', age)

    # Checkbox example
    agree = st.checkbox('I agree to the terms and conditions')
    if agree:
        st.write('Thank you for agreeing!')

    # Button example
    if st.button('Click me'):
        st.write('Button clicked!')

    # Selectbox example
    options = ['Option 1', 'Option 2', 'Option 3']
    chosen_option = st.selectbox('Choose an option', options)
    st.write('You selected:', chosen_option)


if __name__ == '__main__':
    main()
