
import streamlit as st

st.title("BMI Calculator")

if "people" not in st.session_state:
    st.session_state.people = []

name = st.text_input("Enter name:")
age = st.number_input("Enter age:", min_value=1, max_value=120, value=24)
weight = st.number_input("Enter weight in kilograms:", min_value=1.0, value=85.0)
height = st.number_input("Enter height in meters:", min_value=0.1, value=1.80)

if st.button("Add Person"):
    bmi = weight / (height ** 2)

    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal weight"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"

    person = {
        "name": name,
        "age": age,
        "weight": weight,
        "height": height,
        "bmi": bmi,
        "category": category
    }

    if name.strip():
        st.session_state.people.append(person)
        st.success(f"{name} has been added.")
    else:
        st.warning("Please enter a name.")

st.header("Results")

for person in st.session_state.people:
    st.write(
        f"{person['name']}, Age: {person['age']}, "
        f"Weight: {person['weight']:.1f} kg, "
        f"Height: {person['height']:.2f} m, "
        f"BMI: {person['bmi']:.2f}, "
        f"Category: {person['category']}"
    )
