import spacy


# Carregando o core small pt.
nlp = spacy.load("pt_core_news_sm")

# Criado após processar um texto com o objeto nlp.
doc = nlp('Kenshiro, finalmente nos encontramos.')

# Iteração dos Tokens.
for token in doc:
    print(token.text)

# Indexar o doc para obter um token
unico_token = doc[0]  # Kenshiro.

# Um pedaço/fatia do doc é um objeto partição (span).
span = doc[2:4]  # "finalmente", "nos".
print(span.text)  # Obter o texto da partição com o atributo '.text'
