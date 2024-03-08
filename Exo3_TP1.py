#EXERCICE N°3

from aima3 import utils
from aima3.logic import *

kb=FolKB()


#l'informer des emplacement existants qu'on va utiliser comme étant un id des maisons
kb.tell(expr('Emplacement(Debut)'))
kb.tell(expr('Emplacement(Milieu)'))
kb.tell(expr('Emplacement(Fin)'))

kb.tell(expr('Avant(Debut,Milieu)'))
kb.tell(expr('Avant(Milieu , Fin)'))



#prédicats de déduction des couleurs 
kb.tell(expr('Nationalite(x,Anglaise)==>Couleur(x,Blanc)'))
kb.tell(expr('Nationalite(x,Espagnole)&Avant(y,x)==>Couleur(y,Vert)'))
kb.tell(expr('Nationalite(x,Française)&Avant(x,y)==>Couleur(y,Bleu)'))

kb.tell(expr('Couleur(x,Vert)&Avant(x,y)==>Sport(y,Football)'))

#prédicats de déduction des sports
kb.tell(expr('Sport(Debut,Tennis)'))
kb.tell(expr('Sport(Fin,Football)'))
kb.tell(expr('Couleur(x,Vert)==>Sport(x,Natation)'))

#prédicats de déduction des nationalités
kb.tell(expr('Nationalite(Fin,Espagnole)'))
kb.tell(expr('Nationalite(Debut,Anglaise)'))
kb.tell(expr('Nationalite(Milieu,Française)'))


#définition de la maison
kb.tell(expr('Emplacement(x)&Couleur(x,c)&Sport(x,s)&Nationalite(x,n)==>Maison(x,c,s,n)'))



#requete
Maison=fol_fc_ask(kb,expr('Maison(x,c,s,n)'))

print(list(Maison))