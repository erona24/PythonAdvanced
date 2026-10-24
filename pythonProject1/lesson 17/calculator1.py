import streamlit as st


def kalkulo(num1, num2, operations):
    if operations == "mbledhje":
        result = num1 + num2
    elif operations == "zbritje":
        result = num1 - num2
    elif operations == "pjesetim":
        result = num1 / num2
    else:
        result = num1 * num2

    return result


def main():
    st.title("simple calc")

    num1 = st.number_input("sheno vleren e pare")

    num2 = st.number_input("sheno vleren e dyte")

    operations = st.radio("select an option", ["mbledhje", "zbritje", "shumezim", "pjesetim"])

    result = kalkulo(num1, num2, operations)

    st.write(result)


if __name__ == "__main__":
    main()