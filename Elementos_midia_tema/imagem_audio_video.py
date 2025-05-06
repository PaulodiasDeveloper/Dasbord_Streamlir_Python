import streamlit as st
from PIL import Image


myDog = Image.open('../Mídia/dog.jpg')
st.subheader("1- Imagem do dog")
st.image(myDog, caption='Um cachorro desconfiado')   


myAudio = open('../Mídia/Scratching The Surface.mp3', 'rb')
abrirAudio = myAudio.read()
st.subheader("2- Minha música")
st.audio(abrirAudio, format='audio/mp3')

arquivoVideo = open('../Mídia/Buildings.mp4', 'rb')
abrirVideo = arquivoVideo.read()
st.subheader("3- Vídeo dos prédios")
st.video(abrirVideo)