import streamlit as st
import random
import time

# App Title and Introduction
st.title("🎡 Spin the Wheel of Fun!")
st.markdown("Ready to try your luck? Click the button below and see what exciting surprise awaits!")
st.markdown("---")

# List of Prizes
prizes = [
    "🍫 You win a delicious Chocolate!",
    "💪 Time for 10 powerful Pushups!",
    "📚 Dive into a book: Read 1 Page!",
    "🎵 Get groovy: Dance for 1 Minute!",
    "🎨 Unleash your creativity: Draw Something in 2 Minutes!",
    "🚶‍♂️ Stretch your legs: Take a 5-minute walk!",
    "🧘‍♀️ Find your calm: Take 3 Deep Breaths!",
    "🥤 Refresh yourself: Drink a Glass of Water!",
    "📞 Connect: Call a Friend and say Hi!",
    "🌟 You're a star! Enjoy this Big Smile! 😄",
]

# Function to simulate spinning effect
def spin_wheel():
    with st.spinner('The wheel is spinning... 🌀'):
        time.sleep(2)  # Spinning effect
    selected_prize = random.choice(prizes)
    return selected_prize

# Personalized greeting
name = st.text_input("What's your name? (Optional)", "")
if name:
    st.markdown(f"Hello {name}! Ready to spin the wheel? 🎯")
else:
    st.markdown("Ready to spin the wheel? 🎯")

# Initialize session state for spins
if 'spins' not in st.session_state:
    st.session_state.spins = 0

# Layout
col1, col2, col3 = st.columns([1, 3, 1])

with col2:
    if st.button('🎯 Spin the Wheel!'):
        st.session_state.spins += 1

        # Spin the wheel
        prize = spin_wheel()

        # Display result
        st.markdown("---")
        st.balloons()
        st.success(f"🎉 **Congratulations!** You landed on: **{prize}**")

        # Show total spins
        st.markdown(f"**Total Spins Today:** {st.session_state.spins}")
        st.markdown("---")

# Footer
st.markdown('---')
st.caption('Made with ❤️ using Streamlit | Spin again for more fun!')
