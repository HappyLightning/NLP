import spacy


nlp = spacy.load("pt_core_news_sm")
print('\nPrevisão de entidades nomeadas:')
doc = nlp('A Apple está tentando comprar uma startup australiana por R$500.000.000.00')
print(f'{doc}')
# Iterar nas entidades previstas
print([(entity, entity.label_) for entity in doc.ents])
print(f'Explicações: {[spacy.explain(entity.label_ ) for entity in doc.ents]}')