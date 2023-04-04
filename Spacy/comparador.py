import spacy

# Importe o comparador - Matcher
from spacy.matcher import Matcher

nlp = spacy.load("pt_core_news_sm")
doc = nlp("Vazou a data de lançamento do novo iPhone X após a Apple revelar a existência de compras antecipadas.")

# Inicialize o comparador com o vocabulário compartilhado
matcher = Matcher(nlp.vocab)

# Crie uma expressão que faça a correspondência dos tokens: "iPhone" and "X"
pattern = [{"TEXT": "iPhone"}, {"TEXT": "X"}]

# Adicione uma expressão ao comparador
matcher.add("IPHONE_X_PATTERN", [pattern])

# Use o comparador no doc
matches = matcher(doc)
print("Correspondências:", [doc[start:end].text for match_id, start, end in matches])

doc = nlp(
    "Após fazer a atualização do iOS você não irá perceber uma mudança radical "
    "na sua interface: nada parecido com a reviravolta estética que foi feita com o iOS 7. A "
    "maioria da roupagem do iOS 11 permanece a mesma que o iOS 10. Mas você irá descobrir "
    "alguns ajustes se você procurar nos detalhes."
)
print(f'\n{doc}')
# Escreva uma expressão que corresponda às versões completas do IOS ("iOS 7", "iOS 11", "iOS 10")
pattern = [{"TEXT": "iOS"}, {"IS_DIGIT": True}]

# Adicione a expressão ao comparador matcher e aplique o matcher ao doc
matcher.add("IOS_VERSION_PATTERN", [pattern])
matches = matcher(doc)
print("Total de correspondências encontradas:", len(matches))

# Faça a iteração sobre as correspondencias e imprima a partição do texto
for match_id, start, end in matches:
    print("Correspondência encontrada:", doc[start:end].text)