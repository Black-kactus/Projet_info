Pour faire fonctionner le programme, vous devez avoir avoir un dossier contenant :
- les images nécessaires : cavalier_blanc, roi_blanc, reine_blanche, fou_blanc, tour_blanche, pion_blanc, cavalier_noir, roi_noir, reine_noire, fou_noir, tour_noire, pion_noir   /   defaite_des_blancs, defaite_des_noirs  /   dep_roi, dep_tour, dep_dame, dep_fou, dep_cavalier, dep_pion
- les fichiers python board.py, piece.py, main.py, new_interface.py 
- le fichier Scripts.txt pour avoir les scripts de certains coups spéciaux 

Une fois le programme new_interface.py lancé, il affiche une fenêtre d’interface sur laquelle vous pouvez jouer. Cliquez sur "Nouvelle Partie", puis rentrez le nom des joueur.e.s et cliquez sur "Lancer la Partie". Pour jouer, entrez la pièce à jouer dans "Pièce à bouger" (ou effectuez un clic gauche sur la case correspondante) puis sa case d’arrivée dans "Coup à jouer" (ou effectuez un clic droit sur la case correspondante) et appuyer sur valider. Si le coup est possible, il s'effectue et c'est au tour de l'autre joueur.e, sinon, un message d'erreur s'afficher et c'est toujours à votre tour de jouer. 

Pour plus de détails, cliquez sur "Options": 

Ce bouton vous permet de :
- compiler un script (le programme effectue les coups et l'échiquier s'affiche au dernier coup réalisé)
- lire les règles du jeu
- connaître les commandes spéciales du jeu dans "Comment jouer ?"
- changer le style d'affichage si vous avez un système OS par exemple, sur lequel le thème aqua tkinter ne permet pas d'utiliser certaines fonctionnalités
- activer/désactiver le son
