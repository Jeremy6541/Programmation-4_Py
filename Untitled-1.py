import mistletoe

with open("Exemple.md", "r") as Draft_file:
    lines = Draft_file.readlines()
    Draft_file.close()
    Draft_file = open("Exemple.md", "w") 
    for Symbol in lines:
        Shortcut = '()'  # String to search for
        if Symbol.find(Shortcut) != -1:
            Symbol = Symbol.replace(Shortcut, '<div align="center">', 1)
        Draft_file.write(Symbol)
    Draft_file.close()

    Draft_file = open("Exemple.md", "r")
    lines = Draft_file.readlines()
    Draft_file.close()
    Draft_file = open("Exemple.md", "w") 
    for Symbol in lines:
        Shortcut = '()'  # String to search for
        if Symbol.find(Shortcut) != -1:
            Symbol = Symbol.replace(Shortcut, '</div>', 1)
        Draft_file.write(Symbol)
    Draft_file.close()


with open('Exemple.md', 'r') as fin:
    rendered = mistletoe.markdown(fin)  
    print(rendered)
    fin.close()
with open('Exemple.html', 'w') as fout:
  fout.write(rendered)
  fout.close()
