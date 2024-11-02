import google.generativeai as ai

# Minha chave API
API_KEY = 'AIzaSyA5hL24Fa37wIkFzvX5J5JlKWCgAq9YVyY'

# Configuração da API
ai.configure(api_key=API_KEY)

# Criação do modelo
model = ai.GenerativeModel("gemini-pro")
chat = model.start_chat()

# Início da conversa
print("Chatbot: Olá! Vamos trabalhar juntos para alcançar sua meta financeira.")
print("Chatbot: Qual é a sua meta? (Exemplo: comprar um celular, fazer uma viagem, etc.)")

# Pergunta sobre a meta e o valor
meta = input("Eu: ")
print("Chatbot: Qual o valor para essa meta?")
valor_meta = float(input("Eu: R$ "))

# Pergunta sobre o tempo para realizar a meta
print("Chatbot: Em quantos meses você quer alcançar essa meta?")
meses = int(input("Eu: "))

# Cálculo do valor mensal fixo
valor_mensal = valor_meta / meses

# Exibe o valor mensal a ser economizado
print(f"Chatbot: Para alcançar sua meta de R${valor_meta:.2f} em {meses} meses, você precisa economizar R${valor_mensal:.2f} por mês.")

# Geração do prompt para dicas financeiras
prompt = f"Assuma que você só responde sobre economia e finanças. O usuário quer {meta} e possui um orçamento de R${valor_mensal:.2f}. Ajude-o a alcançar essa meta com dicas financeiras apropriadas."

# Obter dicas do chatbot
response = chat.send_message(prompt)
print('Chatbot:', response.text)

# Encerrar a conversa
print("\nChatbot: Esse é seu plano! Se precisar de mais alguma ajuda, estou aqui!")
