import mistletoe


def CenterText(Document,New_file):
    found = False  # Variable globale pour suivre l'état de la recherche du motif
    # Ouverture du document Markdown en mode lecture pour inspection initiale
    Doc = open(Document, "r")
    lines = Doc.readlines()

    # Ouverture du document Markdown en mode écriture pour modification
    New_Doc = open(New_file, "w")
    for Symbol in lines:
        Shortcut = '()'  # Recherche du motif à remplacer
        if Symbol.find(Shortcut) != -1 and (found == False): # -1 signifie que le motif n'a pas été trouvé
            Symbol = Symbol.replace(Shortcut, '<div align="center">\n', 1) # Remplacement des balises Markdown par des balises HTML    
            # add an empty line
            found = True  # Indique que le motif a été trouvé et remplacé

        elif Symbol.find(Shortcut) != -1 and (found == True): # -1 signifie que le motif n'a pas été trouvé
            Symbol = Symbol.replace(Shortcut, '</div>\n', 1) # Remplacement des balises Markdown par des balises HTML
            found = False
        New_Doc.write(Symbol)
    New_Doc.close()
    # Envoie du document Markdown modifié à la fonction de rendu HTML
    with open(New_file, 'r') as fin:
        rendered = mistletoe.markdown(fin)  
        print(rendered)
        fin.close()

    # Écriture du rendu HTML dans un fichier de sortie
    with open('Exemple.html', 'w') as fout:
        fout.write(rendered)
        fout.close()
CenterText('Exemple.md', 'Centered_file.md')  # Appel de la fonction CenterText pour centrer le texte du document Markdown