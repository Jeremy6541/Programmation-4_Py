import mistletoe
from mistletoe.block_token import Heading

# Fonction de Jérémy Roy (Centrage de texte)
def CenterText(Document,New_file):
    found = False  # Variable globale pour suivre l'état de la recherche du motif
    # Ouverture du document Markdown en mode lecture pour inspection initiale
    Doc = open(Document, "r")
    lines = Doc.readlines()

    # Ouverture du document Markdown en mode écriture pour modification
    New_Doc = open(New_file, "w")
    for Symbol in lines:
        Shortcut = "()" + str("\n")  # Recherche du motif à remplacer
        if Symbol.find(Shortcut) != -1 and (found == False): # -1 signifie que le motif n'a pas été trouvé
            Symbol = Symbol.replace(Shortcut, '<div align="center">\n\n', 1) # Remplacement des balises Markdown par des balises HTML (Besoin de 2 \n car le premier n'est pas visible)    
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


# Fonction de Nicolas Migneault (Création de table des matières)
def creer_table_matiere(fichier):

    # Lire le fichier
    with open(fichier, "r", encoding="utf-8") as f:
        texte = f.read()

    # Vérifier si le marqueur existe
    if "**contenu:**" not in texte.lower():
        print("Aucun **contenu:** détecté.")
        return

    print("**contenu:** détecté.")

    table = "## Table des matières\n\n"

    # Parser le document
    document = mistletoe.Document(texte)

    for element in document.children:

        if isinstance(element, Heading):

            if element.level == 2 or element.level == 3 or element.level == 4 or element.level == 5 or element.level == 6:

                titre = ""

                for enfant in element.children:
                    if hasattr(enfant, "content"):
                        titre += enfant.content

                lien = titre.lower().replace(" ", "-")

                # Ajouter le titre dans la table
                if element.level == 1:
                    table += f"- [{titre}](#{lien})\n"

                elif element.level == 2:
                    table += f"  - [{titre}](#{lien})\n"

                elif element.level == 3:
                    table += f"    - [{titre}](#{lien})\n"

                elif element.level == 4:
                    table += f"      - [{titre}](#{lien})\n"

                elif element.level == 5:
                    table += f"        - [{titre}](#{lien})\n"

                elif element.level == 6:
                    table += f"          - [{titre}](#{lien})\n"

    # Insérer la table après le marqueur
    texte = texte.replace(
        "**contenu:**",
        "" + table,
        1
    )

    # Sauvegarder
    with open(fichier, "w", encoding="utf-8") as f:
        f.write(texte)

    print("Table des matières créée.")


creer_table_matiere("projet_1_markdown.md")
CenterText('projet_1_markdown.md', 'Centered_file.md')  # Appel de la fonction CenterText pour centrer le texte du document Markdown


# Envoie du document Markdown modifié à la fonction de rendu HTML
with open('Centered_file.md', 'r') as fin:
    rendered = mistletoe.markdown(fin)  
    print(rendered)
    fin.close()

# Écriture du rendu HTML dans un fichier de sortie
with open('projet_1_markdown.md.html', 'w', encoding='utf-8') as fout:
    fout.write(rendered)
    fout.close()