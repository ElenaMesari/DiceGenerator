import streamlit as st
import random

# Page Configuration
st.set_page_config(page_title="Dice Roller", page_icon="🎲",) 
st.title("🎲Dice Generator")

st.markdown("""
    <style>
    .stApp {
        background-color: #232B2B
    }
    </style>
""", unsafe_allow_html=True)


# Dice Images
dice_faces = {
    1: "🎲 1️⃣",
    2: "🎲 2️⃣",
    3: "🎲 3️⃣",
    4: "🎲 4️⃣",
    5: "🎲 5️⃣",
    6: "🎲 6️⃣"
}

# Rolling Function
if st.button("Roll Dice 🎲"):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("🎲 Dice 1")
        st.write(f"### {dice_faces[dice1]}")
    
    with col2:
        st.subheader("🎲 Dice 2")
        st.write(f"### {dice_faces[dice2]}")


    st.success(f"**Total: {dice1 + dice2}**")
