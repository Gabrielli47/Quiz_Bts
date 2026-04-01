import streamlit as st
from PIL import Image
import random

st.title("💜 Quiz do BTS 💜")

# Pontos
pontos = 0

# Perguntas
perguntas = [
    {"pergunta": "Quem é o líder do BTS?", "resposta": "rm"},
    {"pergunta": "Quem é o maknae (mais novo)?", "resposta": "jungkook"},
    {"pergunta": "Qual membro se chama Kim Taehyung?", "resposta": "v"},
    {"pergunta": "Qual membro é conhecido como sunshine?", "resposta": "jhope"},
    {"pergunta": "Quantos membros tem o BTS?", "resposta": "7"}
]

# Embaralhar perguntas
random.shuffle(perguntas)

# Loop do quiz
for p in perguntas:
    resposta = st.text_input(p["pergunta"], key=p["pergunta"]).lower()
    if resposta:
        if resposta == p["resposta"]:
            st.success("✅ Correto!")
            pontos += 1
        else:
            st.error(f"❌ Errado! Resposta certa: {p['resposta']}")

st.write(f"🎯 Você fez {pontos} de {len(perguntas)} pontos!")

# Classificação
if pontos == 5:
    imagem = "bts_top.jpg"
elif pontos >= 3:
    imagem = "bts_medio.jpg"
else:
    imagem = "bts_basico.jpg"

# Mostrar imagem
try:
    img = Image.open(imagem)
    st.image(img, caption="Sua classificação", use_column_width=True)
except FileNotFoundError:
    st.warning(f"⚠️ Imagem '{imagem}' não encontrada na pasta do código!")