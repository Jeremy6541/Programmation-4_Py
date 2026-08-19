import mistletoe

with open('Exemple.md', 'r') as fin:
    rendered = mistletoe.markdown(fin)  
    print(rendered)
