
import streamlit as st
import random
import time
from gtts import gTTS
import pygame
import os

# Initialize pygame mixer for sound effects
pygame.mixer.init()

# App Title and Introduction
st.title("🎡 Spin the Wheel of Fun!")
st.markdown("Ready to try your luck? Click the button below and see what exciting surprise awaits!")
st.markdown("---")

# List of Prizes or Tasks with Emojis for better visual appeal
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

# Function to simulate a spinning effect with visual feedback
def spin_wheel():
    with st.spinner('The wheel is spinning... 🌀'):
        time.sleep(2)  # Simulate spinning for 2 seconds
    selected_prize = random.choice(prizes)
    return selected_prize

# Function to play a sound effect
def play_sound(effect_path):
    try:
        pygame.mixer.music.load(effect_path)  # Load the sound file
        pygame.mixer.music.play()  # Play the sound
    except Exception as e:
        st.error(f"Error loading sound: {str(e)}")

# Function for text-to-speech (TTS)
def speak_prize(prize_text):
    tts = gTTS(text=prize_text, lang='en')
    tts.save("prize.mp3")
    pygame.mixer.music.load("prize.mp3")
    pygame.mixer.music.play()

# Show a personalized greeting based on user input
name = st.text_input("What's your name? (Optional)", "")
if name:
    st.markdown(f"Hello {name}! Ready to spin the wheel? 🎯")
else:
    st.markdown("Ready to spin the wheel? 🎯")

# Track the number of spins
if 'spins' not in st.session_state:
    st.session_state.spins = 0

# Improved Layout with Columns for the Button and Result
col1, col2, col3 = st.columns([1, 3, 1])  # Adjust column widths for centering

with col2:
    if st.button('🎯 Spin the Wheel!'):
        st.session_state.spins += 1
        
        # Play the "spin" sound effect (replace with the actual sound file path)
        play_sound("mixkit-cheering-crowd-loud-whistle-610.wav")  # Update with your actual file path
        
        # Simulate wheel spinning with a delay
        prize = spin_wheel()
        
        # Show the prize with a celebratory effect
        st.markdown("---")
        st.balloons()  # Add some celebratory balloons!
        st.success(f"🎉 **Congratulations!** You landed on: **{prize}**")
        
        # Play the "win" sound effect (using your cheering sound)
        play_sound("mixkit-cheering-crowd-loud-whistle-610.wav")  # Same sound or choose another

        # Announce the prize using TTS (Text to Speech)
        speak_prize(prize)
        
        # Display number of spins
        st.markdown(f"Total Spins Today: {st.session_state.spins}")
        st.markdown("---")

# Fun Footer
st.markdown('---')
st.caption('Made with ❤️ using Streamlit | Spin again for more fun!')







