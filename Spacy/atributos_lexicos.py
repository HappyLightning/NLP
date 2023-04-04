import spacy


nlp = spacy.load("pt_core_news_sm")
doc = nlp('Um Playstation 5 é muito caro.')

print('Indíce: ', [token.i for token in doc])
print('Texto: ', [token.text for token in doc])
print('É alpha: ', [token.is_alpha for token in doc])
print('É uma pontuação: ', [token.is_punct for token in doc])
print('Como um Número: ', [token.like_num for token in doc])

# Contar as ocorrências de '%' num texto.
print('Contar as ocorrências de "%" num texto:')
nlp = spacy.blank("pt")  # Objeto spacy vazio da lingua pt.

# Processar o texto
doc = nlp(
    "Em 1990, mais de 60% da população da Ásia Oriental estava em situação de extrema pobreza."
    "Agora, menos de 4% está nessa situação."
)
print(f'\n{doc}')
# Iterar os tokens de um documento doc
for token in doc:
    # Checar se o token é composto por algarismos numéricos
    if token.like_num:
        # Selecionar o próximo token do documento
        next_token = doc[token.i + 1]
        # Checar se o texto do proximo token é igual a "%"
        if next_token.text == "%":
            print(f"Percentual encontrado: {token.text}%")
