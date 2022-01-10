
https://fr.jeffprod.com/blog/2014/comment-programmer-un-jeu-dechecs/

https://fr.wikipedia.org/wiki/R%C3%A8gles_du_jeu_d%27%C3%A9checs

https://docs.python.org/3/library/tk.html

Meilleure documentation tkinter https://tkdocs.com/tutorial/grid.html#morefeatures

créer executable : https://www.mathweb.fr/euclide/2019/02/01/creer-un-executable-sous-windows-a-partir-dun-programme-python/

Pour l'interpreteur :
#T,C,F,Q,K,P = tour, cavalier, fou, reine(queen), roi(king), pion
#N,B = noir, blanc
position=[[TB1,PB1,0,0,0,0,PN1,TN1],[CB1,PB2,0,0,0,0,PN2,CN1],[FB1,PB3,0,0,0,0,PN3,FN1],[QB1,PB4,0,0,0,0,PN4,QN1],[KB1,PB5,0,0,0,0,PN5,KN1],[FB2,PB6,0,0,0,0,PN6,FN2],[CB2,PB7,0,0,0,0,PN7,CN2],[TB2,PB8,0,0,0,0,PN8,TN2]]

Pour faire fonctionner le programme, vous devoir avoir un dossier contenant :
-avec les images nécessaires :
   cavalier_blanc, roi_blanc, reine_blanche, fou_blanc, tour_blanche, pion_blanc, cavalier_noir, roi_noir, reine_noire, fou_noir, tour_noire, pion_noir
   defaite_des_blancs, defaite_des_noirs
   dep_roi, dep_tour, dep_dame, dep_fou, dep_cavalier, dep_pion
-les fichiers python board, piece, main, new_interface 
-le fichier son ——, le fichier Scipts.txt. 

Une fois le programme lancé, il affiche une fenêtre d’interface sur laquelle vous pouvez jouer. Cliquez sur "Nouvelle Partie", puis rentrez le nom des joueurs et cliquez sur "Lancer la Partie". Pour jouer, entrez la pièce à jouer dans "Pièce à bouger" (ou effectuer un clic gauche sur la case correspondante) puis sa case d’arrivée dans "Coup à jouer" (ou effectuer un clic droit sur la case correspondante) et appuyer sur valider. Si le coup est possible, il s'effectue et c'est au tour de l'autre joueur, sinon, un message d'erreur s'afficher et c'est toujours à votre tour de jouer. 
Pour plus de détails, cliquez sur "Options". Ce bouton vous permet de :
- compiler un script (le programme effectue les coups et l'échiquier s'affiche au dernier coup réalisé)
- lire les règles du jeu
- connaître les commandes spéciales du jeu dans "Comment jouer ?"
- changer le style d'affichage si vous avez un système OS par exemple, sur lequel le thème aqua tkinter ne permet pas d'utiliser certaines fonctionnalités
- activer/désactiver le son
