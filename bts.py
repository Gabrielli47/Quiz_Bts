import random
from PIL import Image

print("💜 Bem-vindo ao Quiz do BTS! 💜\n")

pontos = 0

perguntas = [
    {"pergunta": "Quem é o líder do BTS? ", "resposta": "rm"},
    {"pergunta": "Quem é o maknae (mais novo)? ", "resposta": "jungkook"},
    {"pergunta": "Qual membro se chama Kim Taehyung? ", "resposta": "v"},
    {"pergunta": "Qual membro é conhecido como sunshine? ", "resposta": "jhope"},
    {"pergunta": "Quantos membros tem o BTS? ", "resposta": "7"}
]

# embaralhar perguntas
random.shuffle(perguntas)

# loop do quiz
for p in perguntas:
    resposta = input(p["pergunta"]).lower()

    if resposta == p["resposta"]:
        print("✅ Correto!\n")
        pontos += 1
    else:
        print(f"❌ Errado! Resposta certa: {p['resposta']}\n")

# resultado final
print(f"🎯 Você fez {pontos} de {len(perguntas)} pontos!\n")

# classificação

if pontos == 5:
    imagem = "bts_top.jpg"
elif pontos >= 3:
    imagem = "bts_medio.jpg"
else:
    imagem = "bts_basico.jpg"

print("\n💜 Obrigado por jogar! 💜")

# abrir imagem escolhida por você
try:
    img = Image.open(imagem)
    img.show()
except:
    print(f"⚠️ Coloque a imagem '{imagem}' na pasta do código!")