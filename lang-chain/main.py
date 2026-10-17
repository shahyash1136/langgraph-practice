import langchain_helper as lch
import streamlit as st

st.title("Pets Name generator")
animal_type = st.sidebar.selectbox(
    "What is your pet?", ("Cat", "Dog", "Cow", "Hamster", "Horse", "Snake")
)

pet_color = st.sidebar.text_area(
    label=f"What color is your {animal_type}?", max_chars=15
)

if pet_color:
    response = lch.generate_pet_name(animal_type, pet_color)
    st.markdown(response)
