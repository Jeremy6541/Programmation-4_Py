import mistletoe

# Ouverture du document Markdown en mode lecture pour inspection initiale
with open("Exemple.md", "r") as Draft_file:
    lines = Draft_file.readlines()
    Draft_file.close()

    # Ouverture du document Markdown en mode écriture pour modification
    Draft_file = open("Exemple.md", "w") 
    for Symbol in lines:
        Shortcut = '()'  # Recherche du motif à remplacer
        if Symbol.find(Shortcut) != -1: # -1 signifie que le motif n'a pas été trouvé
            Symbol = Symbol.replace(Shortcut, '<div align="center">', 1) # Remplacement des balises Markdown par des balises HTML    
        Draft_file.write(Symbol)
    Draft_file.close()

    # Ouverture du document Markdown suite à la première modification
    Draft_file = open("Exemple.md", "r")
    lines = Draft_file.readlines()
    Draft_file.close()

    # Ouverture du document Markdown en mode écriture pour modification
    Draft_file = open("Exemple.md", "w") 
    for Symbol in lines:
        Shortcut = '()'  # Recherche du motif à remplacer
        if Symbol.find(Shortcut) != -1: # -1 signifie que le motif n'a pas été trouvé
            Symbol = Symbol.replace(Shortcut, '</div>', 1) # Remplacement des balises Markdown par des balises HTML
        Draft_file.write(Symbol)
    Draft_file.close()

# Envoie du document Markdown modifié à la fonction de rendu HTML
with open('Exemple.md', 'r') as fin:
    rendered = mistletoe.markdown(fin)  
    print(rendered)
    fin.close()

# Écriture du rendu HTML dans un fichier de sortie
with open('Exemple.html', 'w') as fout:
  fout.write(rendered)
  fout.close()
