# Este fragmento nos permite leer la totalidad de un archivo de texto
f = open('Discord bots codes.txt', 'r', encoding='utf-8')
text = f.read()
print(text)
f.close()