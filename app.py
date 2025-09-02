import streamlit as st

st.set_page_config(page_title="Obersoft AI Chart Game", page_icon="🌸", layout="centered")

# Background (Golden Age feel)
page_bg = """
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://wallpapercave.com/wp/wp9112830.jpg"); 
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

st.title("🌸 Obersoft AI - Brahmakumaris Self-Chart Game 🌸")
st.write("Answer YES/NO for your daily chart and see your destiny!")

# Questions
amritvela = st.radio("1) Amritvela done?", ["YES", "NO"], horizontal=True)
murli = st.radio("2) Murli class done?", ["YES", "NO"], horizontal=True)
traffic = st.radio("3) Traffic control?", ["YES", "NO"], horizontal=True)
bhojan = st.radio("4) Bhojan mein Yaad?", ["YES", "NO"], horizontal=True)
numashyam = st.radio("5) Numashyam Yog?", ["YES", "NO"], horizontal=True)
ratri = st.radio("6) Ratri Potamel?", ["YES", "NO"], horizontal=True)
gratitude = st.radio("7) Gratitude practice?", ["YES", "NO"], horizontal=True)
civil = st.radio("8) Civil eyes?", ["YES", "NO"], horizontal=True)

# Button
if st.button("🚪 Submit My Chart"):
    answers = [amritvela, murli, traffic, bhojan, numashyam, ratri, gratitude, civil]

    if all(ans == "YES" for ans in answers):
        st.success("🎉 Congratulations! You are in Heaven 🌸✨")
        st.image(
            "https://media.giphy.com/media/26FLdmIp6wJr91JAI/giphy.gif",  # Heaven GIF
            caption="🌸 Angels welcome you to Heaven 🌸",
            use_container_width=True
        )
        st.balloons()
        st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")
    else:
        st.error("😈 Oops! You missed something… Welcome to Hell 🔥")
        st.image(
            "https://media.giphy.com/media/l0MYt5jPR6QX5pnqM/giphy.gif",  # Hell GIF
            caption="🔥 Evil welcomes you to Hell 🔥",
            use_container_width=True
        )
        st.audio("https://www2.cs.uic.edu/~i101/SoundFiles/CantinaBand60.wav")
