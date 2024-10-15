vogais_txt = 'C:\\Users\\Julia\\Downloads\\exagerado_letra.txt'

with open(vogais_txt, 'r', encoding='utf-8') as file:
    extraido = file.read()

def contagem(texto):

    contagem_vogais = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    
    descarta_acento = {
        'á': 'a', 'â': 'a', 'ã': 'a', 'ä': 'a',
        'é': 'e', 'ê': 'e', 'ë': 'e',
        'í': 'i', 'î': 'i', 'ï': 'i',
        'ó': 'o', 'ô': 'o', 'õ': 'o', 'ö': 'o',
        'ú': 'u', 'û': 'u', 'ü': 'u'
    }
    
    for char in texto.lower():
        if char in contagem_vogais:
            contagem_vogais[char] += 1
        elif char in descarta_acento:
            contagem_vogais[descarta_acento[char]] += 1
    
    return contagem_vogais

contagem_final = contagem(extraido)

for letra, valor in contagem_final.items():
    print(f"Vogal '{letra}': {valor} vezes")
