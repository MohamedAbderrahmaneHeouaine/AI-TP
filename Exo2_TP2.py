#EXERCICE 2

from aima3 import utils
from aima3.logic import *

#Définir une knowledge base
kb=FolKB()

#l'informer des données dont on dispose
kb.tell(expr('Color(Bleu)'))
kb.tell(expr('Color(Vert)'))
kb.tell(expr('Color(Blanc)'))
kb.tell(expr('Color(Noir)'))

#l'informer que les couleurs sont différentes
kb.tell(expr('Diff_color(Vert ,Bleu)'))
kb.tell(expr('Diff_color(Vert ,Blanc)'))
kb.tell(expr('Diff_color(Vert ,Noir)'))
kb.tell(expr('Diff_color(Blanc ,Bleu)'))
kb.tell(expr('Diff_color(Blanc ,Noir)'))
kb.tell(expr('Diff_color(Bleu ,Noir)'))

#l'informer des règles qu'on a , des contraintes d'adjacence

kb.tell(expr('Diff_color(x ,y)==>Diff_color(y ,x)'))
kb.tell(expr('Color(c1)&Color(c2)&Color(c3)&Color(c4)&Color(c5)&Color(c6)&Diff_color(c1 ,c2)&Diff_color(c1 ,c3)&Diff_color(c1 ,c6)&Diff_color(c1 ,c5)&Diff_color(c2 ,c4)&Diff_color(c2 ,c5)&Diff_color(c3,c4)&Diff_color(c3,c2)&Diff_color(c6,c5)&Diff_color(c2 ,c6)&Diff_color(c2 ,c3)& Diff_color(c6 ,c3)==> Carte(c1,c2,c3,c4,c5,c6)'))


#demande des combinaisons possibles pour colorier la carte 
result=fol_fc_ask(kb,expr('Carte(c1,c2,c3,c4,c5,c6)'))

print(list(result))