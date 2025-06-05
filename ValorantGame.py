print("Seja bem-vindo ao Quiz do Valorant!")
answer_user = input("Quer jogar? (S/N): ").strip().lower()

if answer_user != "s":
    print("Tudo bem! Até a próxima 👋")
    quit()

pontuacao = 0

print("\nComeçando...\n")

# Pergunta 1
resposta_1 = input("Qual o nome do personagem? 🟢🦈🔵\n(A) Viper\n(B) Neon\n(C) Gekko\nAlternativa: ").strip().lower()
if resposta_1 == "c":
    print("Correto!")
    pontuacao += 1
else:
    print("Incorreto...")

# Pergunta 2
resposta_2 = input("\nQual agente usa uma cortina de veneno verde?\n(A) Phoenix\n(B) Viper\n(C) Sage\nAlternativa: ").strip().lower()
if resposta_2 == "b":
    print("Correto!")
    pontuacao += 1
else:
    print("Incorreto...")

# Pergunta 3
resposta_3 = input("\nQual é a função da Sage?\n(A) Iniciadora\n(B) Sentinela\n(C) Controladora\nAlternativa: ").strip().lower()
if resposta_3 == "b":
    print("Correto!")
    pontuacao += 1
else:
    print("Incorreto...")

# Pergunta 4
resposta_4 = input("\nQual time brasileiro venceu o VCT Américas em 2023?\n(A) FURIA\n(B) LOUD\n(C) Aspas\nAlternativa: ").strip().lower()
if resposta_4 == "b":
    print("Correto!")
    pontuacao += 1
else:
    print("Incorreto...")

# Pergunta 5
resposta_5 = input("\nO jogador 'Aspas' ficou famoso por jogar com qual agente?\n(A) Jett\n(B) Killjoy\n(C) Brimstone\nAlternativa: ").strip().lower()
if resposta_5 == "a":
    print("Correto!")
    pontuacao += 1
else:
    print("Incorreto...")

# Resultado final
print(f"\nFim do quiz! Sua pontuação foi: {pontuacao}/5")
