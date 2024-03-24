from aima3 import utils
from aima3.logic import *

#Définir une knowledge base
dest_kb=FolKB()


#Ensemble de faits (Facts) pour le test
dest_kb.tell(expr('Saison(Printemps)'))
dest_kb.tell(expr('Interet(Tourisme)'))
dest_kb.tell(expr('Preference(Culture)'))
dest_kb.tell(expr('Compagnie(Groupe)'))
dest_kb.tell(expr('Climat(Désertique)'))
dest_kb.tell(expr('Continent(Afrique)'))
dest_kb.tell(expr('Budget(Moyen)'))

#Remplir la KB avec l'ensemble des destinations (Rules)
#dest_kb.tell(expr(''))

#Règles pour définir que chaque saison est incluse dans toutes les saisons
dest_kb.tell(expr('Saison(Hiver)==>Saison(Toutes)'))
dest_kb.tell(expr('Saison(Eté)==>Saison(Toutes)'))
dest_kb.tell(expr('Saison(Printemps)==>Saison(Toutes)'))
dest_kb.tell(expr('Saison(Automne)==>Saison(Toutes)'))

#Règle pour définir les deux saisons Printemps et Automne en un seul prédicat
dest_kb.tell(expr('Saison(Printemps)==>Saison(PA)'))
dest_kb.tell(expr('Saison(Automne)==>Saison(PA)'))

#Règle pour définir les deux saisons Printemps , Automne et hiver en un seul prédicat
dest_kb.tell(expr('Saison(PA)==>Saison(PAH)'))
dest_kb.tell(expr('Saison(Hiver)==>Saison(PAH)'))


#Règle pour définir que la préférence Traditions est incluse dans Culture et vise-versa
dest_kb.tell(expr('Preference(Traditions)==>Preference(Culture)'))
dest_kb.tell(expr('Preference(Culture)==>Preference(Traditions)'))

#Règle pour définir que la préférence Histoire est incluse dans Culture et vise-versa
dest_kb.tell(expr('Preference(Histoire)==>Preference(Culture)'))
dest_kb.tell(expr('Preference(Culture)==>Preference(Histoire)'))

#Règle pour définir que Découverte implique Tourisme
dest_kb.tell(expr('Interet(Découverte)==>Interet(Tourisme)'))



#Règles définissant les destinations

#-------------------------------------------------------------#
#Destination 1 : Singapour

dest_kb.tell(expr('Budget(Elévé) & Preference(Luxe) & Interet(Tourisme) & Compagnie(Seul) & Climat(Tropical) & Continent(Asie) & Saison(Toutes) ==> Destination(Singapour)'))
dest_kb.tell(expr('Budget(Elévé) & Preference(Luxe) & Interet(Affaires) & Compagnie(Seul) & Climat(Tropical) & Continent(Asie) & Saison(Toutes) ==> Destination(Singapour)'))


#-------------------------------------------------------------#
#Destination 2 : Bangkok

#Groupe
dest_kb.tell(expr('Budget(Moyen) & Preference(Traditions) & Interet(Tourisme) & Compagnie(Groupe) & Climat(Tropical) & Continent(Asie) & Saison(Toutes) ==> Destination(Bangkok)'))
dest_kb.tell(expr('Budget(Moyen) & Preference(Culture) & Interet(Tourisme) & Compagnie(Groupe) & Climat(Tropical) & Continent(Asie) & Saison(Toutes) ==> Destination(Bangkok)'))
dest_kb.tell(expr('Budget(Moyen)& Preference(K-pop) & Interet(Découverte) & Compagnie(Groupe) & Climat(Tropical) & Continent(Asie) & Saison(Toutes) ==> Destination(Bangkok)'))

#Seul
dest_kb.tell(expr('Budget(Moyen)& Preference(K-pop) & Interet(Découverte) & Compagnie(Seul) & Climat(Tropical) & Continent(Asie) & Saison(Toutes) ==> Destination(Bangkok)'))
dest_kb.tell(expr('Budget(Moyen) & Preference(Culture) & Interet(Tourisme) & Compagnie(Seul) & Climat(Tropical) & Continent(Asie) & Saison(Toutes) ==> Destination(Bangkok)'))

#-------------------------------------------------------------#
#Destination  3 : Tokyo

#Groupe
dest_kb.tell(expr('Budget(Moyen) & Preference(Culture) & Interet(Tourisme) & Compagnie(Groupe) & Climat(subtropical) & Continent(Asie) & Saison(Printemps)==> Destination(Tokyo)'))
dest_kb.tell(expr('Budget(Moyen) & Preference(Mangas) & Interet(Découverte) & Compagnie(Groupe) & Climat(subtropical) & Continent(Asie) & Saison(Printemps)==> Destination(Tokyo)'))
dest_kb.tell(expr('Budget(Moyen) & Preference(Modernité) & Interet(Professionel) & Compagnie(Groupe) & Climat(subtropical) & Continent(Asie) & Saison(Toutes)==> Destination(Tokyo)'))
dest_kb.tell(expr('Budget(Elevé) & Preference(Affaires) & Interet(Professionnel) & Compagnie(Groupe) & Climat(subtropical) & Continent(Asie) & Saison(Toutes)==> Destination(Tokyo)'))

#Seul
dest_kb.tell(expr('Budget(Moyen) & Preference(Modernité) & Interet(Découverte) & Compagnie(Seul) & Climat(subtropical) & Continent(Asie) & Saison(Printemps)==> Destination(Tokyo)'))
dest_kb.tell(expr('Budget(Moyen) & Preference(Mangas) & Interet(Découverte) & Compagnie(Seul) & Climat(subtropical) & Continent(Asie) & Saison(Printemps)==> Destination(Tokyo)'))



#-------------------------------------------------------------#
#Destination  4 : Istanbul

#Groupe
dest_kb.tell(expr('Budget(Moyen) & Preference(Architecture) & Interet(Tourisme) & Compagnie(Groupe) & Climat(Méditarranéen) & Continent(Asie) & Saison(Printemps)==> Destination(Istanbul)'))
dest_kb.tell(expr('Budget(Moyen) & Preference(Architecture) & Interet(Tourisme) & Compagnie(Groupe) & Climat(Méditarranéen) & Continent(Asie) & Saison(Automne)==> Destination(Istanbul)'))
dest_kb.tell(expr('Budget(Moyen) & Preference(Histoire) & Interet(Tourisme) & Compagnie(Groupe) & Climat(Méditarranéen) & Continent(Asie) & Saison(Printemps)==> Destination(Istanbul)'))
dest_kb.tell(expr('Budget(Moyen) & Preference(Histoire) & Interet(Tourisme) & Compagnie(Groupe) & Climat(Méditarranéen) & Continent(Asie) & Saison(Automne)==> Destination(Istanbul)'))
dest_kb.tell(expr('Budget(Moyen) & Preference(Gastronomie) & Interet(Tourisme) & Compagnie(Groupe) & Climat(Méditarranéen) & Continent(Asie) & Saison(Printemps)==> Destination(Istanbul)'))
dest_kb.tell(expr('Budget(Moyen) & Preference(Gastronomie) & Interet(Tourisme) & Compagnie(Groupe) & Climat(Méditarranéen) & Continent(Asie) & Saison(Automne)==> Destination(Istanbul)'))

#Seul
dest_kb.tell(expr('Budget(Moyen) & Preference(Architecture) & Interet(Tourisme) & Compagnie(Seul) & Climat(Méditarranéen) & Continent(Asie) & Saison(Printemps)==> Destination(Istanbul)'))
dest_kb.tell(expr('Budget(Moyen) & Preference(Architecture) & Interet(Tourisme) & Compagnie(Seul) & Climat(Méditarranéen) & Continent(Asie) & Saison(Automne)==> Destination(Istanbul)'))
dest_kb.tell(expr('Budget(Moyen) & Preference(Histoire) & Interet(Tourisme) & Compagnie(Seul) & Climat(Méditarranéen) & Continent(Asie) & Saison(Printemps)==> Destination(Istanbul)'))
dest_kb.tell(expr('Budget(Moyen) & Preference(Histoire) & Interet(Tourisme) & Compagnie(Seul) & Climat(Méditarranéen) & Continent(Asie) & Saison(Automne)==> Destination(Istanbul)'))
dest_kb.tell(expr('Budget(Moyen) & Preference(Gastronomie) & Interet(Tourisme) & Compagnie(Seul) & Climat(Méditarranéen) & Continent(Asie) & Saison(Printemps)==> Destination(Istanbul)'))
dest_kb.tell(expr('Budget(Moyen) & Preference(Gastronomie) & Interet(Tourisme) & Compagnie(Seul) & Climat(Méditarranéen) & Continent(Asie) & Saison(Automne)==> Destination(Istanbul)'))

#-------------------------------------------------------------#
#Destination  5 : Séoul

#Groupe
dest_kb.tell(expr('Budget(Moyen) & Preference(Histoire) & Interet(Tourisme) & Compagnie(Groupe) & Climat(Continental) & Continent(Asie) & Saison(Toutes)==> Destination(Séoul)'))
dest_kb.tell(expr('Budget(Moyen) & Preference(Affaires) & Interet(Professionnel) & Compagnie(Groupe) & Climat(Continental) & Continent(Asie) & Saison(Toutes)==> Destination(Séoul)'))
dest_kb.tell(expr('Budget(Moyen) & Preference(Gastronomie) & Interet(Tourisme) & Compagnie(Groupe) & Climat(Continental) & Continent(Asie) & Saison(Toutes)==> Destination(Séoul)'))
dest_kb.tell(expr('Budget(Moyen) & Preference(K-pop) & Interet(Tourisme) & Compagnie(Groupe) & Climat(Continental) & Continent(Asie) & Saison(Toutes)==> Destination(Séoul)'))

#Seul
dest_kb.tell(expr('Budget(Moyen) & Preference(Histoire) & Interet(Tourisme) & Compagnie(Seul) & Climat(Continental) & Continent(Asie) & Saison(Toutes)==> Destination(Séoul)'))
dest_kb.tell(expr('Budget(Moyen) & Preference(Affaires) & Interet(Professionnel) & Compagnie(Seul) & Climat(Continental) & Continent(Asie) & Saison(Toutes)==> Destination(Séoul)'))
dest_kb.tell(expr('Budget(Moyen) & Preference(Gastronomie) & Interet(Tourisme) & Compagnie(Seul) & Climat(Continental) & Continent(Asie) & Saison(Toutes)==> Destination(Séoul)'))
dest_kb.tell(expr('Budget(Moyen) & Preference(K-pop) & Interet(Tourisme) & Compagnie(Seul) & Climat(Continental) & Continent(Asie) & Saison(Toutes)==> Destination(Séoul)'))

#Famille
dest_kb.tell(expr('Budget(Moyen) & Preference(Histoire) & Interet(Tourisme) & Compagnie(Famille) & Climat(Continental) & Continent(Asie) & Saison(Toutes)==> Destination(Séoul)'))
dest_kb.tell(expr('Budget(Moyen) & Preference(Gastronomie) & Interet(Tourisme) & Compagnie(Famille) & Climat(Continental) & Continent(Asie) & Saison(Toutes)==> Destination(Séoul)'))


#-------------------------------------------------------------#
#Destination  6 : Bali

#Groupe
dest_kb.tell(expr('Budget(Moyen) & Preference(Relaxation) & Interet(Tourisme) & Compagnie(Groupe) & Climat(Tropical) & Continent(Asie) & Saison(Eté)==> Destination(Bali)'))
dest_kb.tell(expr('Budget(Elevé) & Preference(Relaxation) & Interet(Tourisme) & Compagnie(Groupe) & Climat(Tropical) & Continent(Asie) & Saison(Eté)==> Destination(Bali)'))

#Seul
dest_kb.tell(expr('Budget(Moyen) & Preference(Histoire) & Interet(Tourisme) & Compagnie(Seul) & Climat(Tropical) & Continent(Asie) & Saison(Eté)==> Destination(Bali)'))
dest_kb.tell(expr('Budget(Elevé) & Preference(Histoire) & Interet(Tourisme) & Compagnie(Seul) & Climat(Tropical) & Continent(Asie) & Saison(Eté)==> Destination(Bali)'))

#Famille
dest_kb.tell(expr('Budget(Moyen) & Preference(Histoire) & Interet(Tourisme) & Compagnie(Famille) & Climat(Tropical) & Continent(Asie) & Saison(Eté)==> Destination(Bali)'))
dest_kb.tell(expr('Budget(Elevé) & Preference(Histoire) & Interet(Tourisme) & Compagnie(Famille) & Climat(Tropical) & Continent(Asie) & Saison(Eté)==> Destination(Bali)'))



#-------------------------------------------------------------#
#Destination  7 : Marrakech
#Groupe
dest_kb.tell(expr('Budget(Moyen) & Preference(Culture) & Interet(Tourisme) & Compagnie(Groupe) & Climat(Subtropical) & Continent(Afrique) & Saison(PAH)==> Destination(Marrakech)'))
dest_kb.tell(expr('Budget(Moyen) & Preference(Gastronomie) & Interet(Tourisme) & Compagnie(Groupe) & Climat(Subtropical) & Continent(Afrique) & Saison(PAH)==> Destination(Marrakech)'))

#Seul
dest_kb.tell(expr('Budget(Moyen) & Preference(Culture) & Interet(Tourisme) & Compagnie(Seul) & Climat(Subtropical) & Continent(Afrique) & Saison(PAH)==> Destination(Marrakech)'))
dest_kb.tell(expr('Budget(Moyen) & Preference(Gastronomie) & Interet(Tourisme) & Compagnie(Seul) & Climat(Subtropical) & Continent(Afrique) & Saison(PAH)==> Destination(Marrakech)'))

#Famille
dest_kb.tell(expr('Budget(Moyen) & Preference(Culture) & Interet(Tourisme) & Compagnie(Famille) & Climat(Subtropical) & Continent(Afrique) & Saison(PAH)==> Destination(Marrakech)'))
dest_kb.tell(expr('Budget(Moyen) & Preference(Gastronomie) & Interet(Tourisme) & Compagnie(Famille) & Climat(Subtropical) & Continent(Afrique) & Saison(PAH)==> Destination(Marrakech)'))

#-------------------------------------------------------------#
#Destination  8 : Caire

#Groupe
dest_kb.tell(expr('Budget(Moyen) & Preference(Histoire) & Interet(Tourisme) & Compagnie(Groupe) & Climat(Désertique) & Continent(Afrique) & Saison(PA)==> Destination(Caire)'))
dest_kb.tell(expr('Budget(Moyen) & Preference(Archéologie) & Interet(Tourisme) & Compagnie(Groupe) & Climat(Désertique) & Continent(Afrique) & Saison(PA)==> Destination(Caire)'))
dest_kb.tell(expr('Budget(Moyen) & Preference(Gastronomie) & Interet(Tourisme) & Compagnie(Groupe) & Climat(Désertique) & Continent(Afrique) & Saison(PA)==> Destination(Caire)'))

#Seul
dest_kb.tell(expr('Budget(Moyen) & Preference(Histoire) & Interet(Tourisme) & Compagnie(Seul) & Climat(Désertique) & Continent(Afrique) & Saison(PA)==> Destination(Caire)'))
dest_kb.tell(expr('Budget(Moyen) & Preference(Archéologie) & Interet(Tourisme) & Compagnie(Seul) & Climat(Désertique) & Continent(Afrique) & Saison(PA)==> Destination(Caire)'))
dest_kb.tell(expr('Budget(Moyen) & Preference(Gastronomie) & Interet(Tourisme) & Compagnie(Seul) & Climat(Désertique) & Continent(Afrique) & Saison(PA)==> Destination(Caire)'))

#Famille
dest_kb.tell(expr('Budget(Moyen) & Preference(Histoire) & Interet(Tourisme) & Compagnie(Famille) & Climat(Désertique) & Continent(Afrique) & Saison(PA)==> Destination(Caire)'))
dest_kb.tell(expr('Budget(Moyen) & Preference(Archéologie) & Interet(Tourisme) & Compagnie(Famille) & Climat(Désertique) & Continent(Afrique) & Saison(PA)==> Destination(Caire)'))
dest_kb.tell(expr('Budget(Moyen) & Preference(Gastronomie) & Interet(Tourisme) & Compagnie(Famille) & Climat(Désertique) & Continent(Afrique) & Saison(PA)==> Destination(Caire)'))


#-------------------------------------------------------------#
#Destination  9 : Kilimandjaro

#Groupe
dest_kb.tell(expr('Budget(Elevé) & Preference(Aventure) & Interet(Alpinisme) & Compagnie(Groupe) & Climat(Océanique) & Continent(Afrique) & Saison(Eté)==> Destination(Kilimandjaro)'))
dest_kb.tell(expr('Budget(Elevé) & Preference(Aventure) & Interet(Alpinisme) & Compagnie(Groupe) & Climat(Océanique) & Continent(Afrique) & Saison(Hiver)==> Destination(Kilimandjaro)'))

#Seul
dest_kb.tell(expr('Budget(Elevé) & Preference(Aventure) & Interet(Alpinisme) & Compagnie(Seul) & Climat(Océanique) & Continent(Afrique) & Saison(Eté)==> Destination(Kilimandjaro)'))
dest_kb.tell(expr('Budget(Elevé) & Preference(Aventure) & Interet(Alpinisme) & Compagnie(Seul) & Climat(Océanique) & Continent(Afrique) & Saison(Hiver)==> Destination(Kilimandjaro)'))


#-------------------------------------------------------------#
#Destination  10 : Arabie-Saoudite

#Groupe
dest_kb.tell(expr('Budget(Elevé) & Preference(Religion) & Interet(Pélerinage) & Compagnie(Groupe) & Climat(Désértique) & Continent(Ais) & Saison(Pélerinage)==> Destination(Arabie-Saoudite)'))
dest_kb.tell(expr('Budget(Elevé) & Preference(Religion) & Interet(Tourisme) & Compagnie(Groupe) & Climat(Désértique) & Continent(Ais) & Saison(Toutes)==> Destination(Arabie-Saoudite)'))

#Seul
dest_kb.tell(expr('Budget(Elevé) & Preference(Religion) & Interet(Pélerinage) & Compagnie(Seul) & Climat(Désértique) & Continent(Ais) & Saison(Pélerinage)==> Destination(Arabie-Saoudite)'))
dest_kb.tell(expr('Budget(Elevé) & Preference(Religion) & Interet(Tourisme) & Compagnie(Seul) & Climat(Désértique) & Continent(Ais) & Saison(Toutes)==> Destination(Arabie-Saoudite)'))

#Famille
dest_kb.tell(expr('Budget(Elevé) & Preference(Religion) & Interet(Pélerinage) & Compagnie(Famille) & Climat(Désértique) & Continent(Ais) & Saison(Pélerinage)==> Destination(Arabie-Saoudite)'))
dest_kb.tell(expr('Budget(Elevé) & Preference(Religion) & Interet(Tourisme) & Compagnie(Famille) & Climat(Désértique) & Continent(Ais) & Saison(Toutes)==> Destination(Arabie-Saoudite)'))



#-------------------------------------------------------------#
#Destination  11 : Luminaria
#Groupe
dest_kb.tell(expr('Budget(Elevé) & Preference(Relaxation) & Interet(Tourisme) & Compagnie(Groupe) & Climat(Modéré) & Continent(Europe) & Saison(Toutes)==> Destination(Luminaria)'))
dest_kb.tell(expr('Budget(Elevé) & Preference(Festival ) & Interet(Tourisme) & Compagnie(Groupe) & Climat(Modéré) & Continent(Europe) & Saison(Toutes)==> Destination(Luminaria)'))

#Seul
dest_kb.tell(expr('Budget(Elevé) & Preference(Relaxation) & Interet(Tourisme) & Compagnie(Seul) & Climat(Modéré) & Continent(Europe) & Saison(Toutes)==> Destination(Luminaria)'))
dest_kb.tell(expr('Budget(Elevé) & Preference(Festival) & Interet(Tourisme) & Compagnie(Seul) & Climat(Modéré) & Continent(Europe) & Saison(Toutes)==> Destination(Luminaria)'))

#Famille
dest_kb.tell(expr('Budget(Elevé) & Preference(Relaxation) & Interet(Tourisme) & Compagnie(Famille) & Climat(Modéré) & Continent(Europe) & Saison(Toutes)==> Destination(Luminaria)'))
dest_kb.tell(expr('Budget(Elevé) & Preference(Festival) & Interet(Tourisme) & Compagnie(Famille) & Climat(Modéré) & Continent(Europe) & Saison(Toutes)==> Destination(Luminaria)'))

#-------------------------------------------------------------#
#Destination  12 : Paris

#Groupe
dest_kb.tell(expr('Budget(Elevé) & Preference(Histoire) & Interet(Tourisme) & Compagnie(Groupe) & Climat(Océanique) & Continent(Europe) & Saison(Toutes)==> Destination(Paris)'))
dest_kb.tell(expr('Budget(Elevé) & Preference(Gastronomie) & Interet(Tourisme) & Compagnie(Groupe) & Climat(Océanique) & Continent(Europe) & Saison(Toutes)==> Destination(Paris)'))
dest_kb.tell(expr('Budget(Elevé) & Preference(Luxe) & Interet(Tourisme) & Compagnie(Groupe) & Climat(Océanique) & Continent(Europe) & Saison(Toutes)==> Destination(Paris)'))
dest_kb.tell(expr('Budget(Elevé) & Preference(Affaires) & Interet(Professionnel) & Compagnie(Groupe) & Climat(Océanique) & Continent(Europe) & Saison(Toutes)==> Destination(Paris)'))

#Seul
dest_kb.tell(expr('Budget(Elevé) & Preference(Histoire) & Interet(Tourisme) & Compagnie(Seul) & Climat(Océanique) & Continent(Europe) & Saison(Toutes)==> Destination(Paris)'))
dest_kb.tell(expr('Budget(Elevé) & Preference(Gastronomie) & Interet(Tourisme) & Compagnie(Groupe) & Climat(Océanique) & Continent(Europe) & Saison(Toutes)==> Destination(Paris)'))
dest_kb.tell(expr('Budget(Elevé) & Preference(Luxe) & Interet(Tourisme) & Compagnie(Groupe) & Climat(Océanique) & Continent(Europe) & Saison(Toutes)==> Destination(Paris)'))


#Famille
dest_kb.tell(expr('Budget(Elevé) & Preference(Histoire) & Interet(Tourisme) & Compagnie(Famille) & Climat(Océanique) & Continent(Europe) & Saison(Toutes)==> Destination(Paris)'))
dest_kb.tell(expr('Budget(Elevé) & Preference(Gastronomie) & Interet(Tourisme) & Compagnie(Famille) & Climat(Océanique) & Continent(Europe) & Saison(Toutes)==> Destination(Paris)'))
dest_kb.tell(expr('Budget(Elevé) & Preference(Luxe) & Interet(Tourisme) & Compagnie(Famille) & Climat(Océanique) & Continent(Europe) & Saison(Toutes)==> Destination(Paris)'))


#-------------------------------------------------------------#
#Destination  13 : Varna

#Groupe
dest_kb.tell(expr('Budget(Moyen) & Preference(Relaxation) & Interet(Tourisme) & Compagnie(Groupe) & Climat(Océanique) & Continent(Europe) & Saison(Toutes)==> Destination(Varna)'))

#Seul
dest_kb.tell(expr('Budget(Moyen) & Preference(Relaxation) & Interet(Tourisme) & Compagnie(Seul) & Climat(Océanique) & Continent(Europe) & Saison(Toutes)==> Destination(Varna)'))



#-------------------------------------------------------------#
#Destination  14 : Rome
#Groupe
dest_kb.tell(expr('Budget(Moyen) & Preference(Culture) & Interet(Tourisme) & Compagnie(Groupe) & Climat(Méditerranéen) & Continent(Europe) & Saison(Toutes)==> Destination(Rome)'))
dest_kb.tell(expr('Budget(Moyen) & Preference(Gastronomie) & Interet(Tourisme) & Compagnie(Groupe) & Climat(Méditerranéen) & Continent(Europe) & Saison(Toutes)==> Destination(Rome)'))

#Seul
dest_kb.tell(expr('Budget(Moyen) & Preference(Culture) & Interet(Tourisme) & Compagnie(Seul) & Climat(Méditerranéen) & Continent(Europe) & Saison(Toutes)==> Destination(Rome)'))
dest_kb.tell(expr('Budget(Moyen) & Preference(Gastronomie) & Interet(Tourisme) & Compagnie(Seul) & Climat(Méditerranéen) & Continent(Europe) & Saison(Toutes)==> Destination(Rome)'))

#Famille
dest_kb.tell(expr('Budget(Moyen) & Preference(Culture) & Interet(Tourisme) & Compagnie(Famille) & Climat(Méditerranéen) & Continent(Europe) & Saison(Toutes)==> Destination(Rome)'))
dest_kb.tell(expr('Budget(Moyen) & Preference(Gastronomie) & Interet(Tourisme) & Compagnie(Famille) & Climat(Méditerranéen) & Continent(Europe) & Saison(Toutes)==> Destination(Rome)'))


#-------------------------------------------------------------#
#Destination  15 : Monaco

#Groupe
dest_kb.tell(expr('Budget(Elevé) & Preference(Relaxation) & Interet(Tourisme) & Compagnie(Groupe) & Climat(Méditerranéen) & Continent(Europe) & Saison(Toutes)==> Destination(Monaco)'))

#Seul
dest_kb.tell(expr('Budget(Elevé) & Preference(Relaxation) & Interet(Tourisme) & Compagnie(Seul) & Climat(Méditerranéen) & Continent(Europe) & Saison(Toutes)==> Destination(Monaco)'))

#Famille
dest_kb.tell(expr('Budget(Elevé) & Preference(Relaxation) & Interet(Tourisme) & Compagnie(Famille) & Climat(Méditerranéen) & Continent(Europe) & Saison(Toutes)==> Destination(Monaco)'))

#-------------------------------------------------------------#
#Destination  16 : NewYork
#Groupe
dest_kb.tell(expr('Budget(Elevé) & Preference(Relaxation) & Interet(Tourisme) & Compagnie(Groupe) & Climat(Subtropical) & Continent(Amérique) & Saison(Toutes)==> Destination(NewYork)'))

#Seul
dest_kb.tell(expr('Budget(Elevé) & Preference(Relaxation) & Interet(Tourisme) & Compagnie(Seul) & Climat(Méditerranéen) & Continent(Amérique) & Saison(Toutes)==> Destination(NewYork)'))

#Famille
dest_kb.tell(expr('Budget(Elevé) & Preference(Relaxation) & Interet(Tourisme) & Compagnie(Famille) & Climat(Méditerranéen) & Continent(Amérique) & Saison(Toutes)==> Destination(NewYork)'))

#-------------------------------------------------------------#
#Destination  17 : Mexico

#Groupe
dest_kb.tell(expr('Budget(Moyen) & Preference(Culture) & Interet(Tourisme) & Compagnie(Groupe) & Climat(Modéré) & Continent(Amérique) & Saison(Toutes)==> Destination(Mexico)'))
dest_kb.tell(expr('Budget(Moyen) & Preference(Gastronomie) & Interet(Tourisme) & Compagnie(Groupe) & Climat(Modéré) & Continent(Amérique) & Saison(Toutes)==> Destination(Mexico)'))

#Seul
dest_kb.tell(expr('Budget(Moyen) & Preference(Culture) & Interet(Tourisme) & Compagnie(Seul) & Climat(Modéré) & Continent(Amérique) & Saison(Toutes)==> Destination(Mexico)'))
dest_kb.tell(expr('Budget(Moyen) & Preference(Gastronomie) & Interet(Tourisme) & Compagnie(Seul) & Climat(Modéré) & Continent(Amérique) & Saison(Toutes)==> Destination(Mexico)'))

#Famille
dest_kb.tell(expr('Budget(Moyen) & Preference(Culture) & Interet(Tourisme) & Compagnie(Famille) & Climat(Modéré) & Continent(Amérique) & Saison(Toutes)==> Destination(Mexico)'))
dest_kb.tell(expr('Budget(Moyen) & Preference(Gastronomie) & Interet(Tourisme) & Compagnie(Famille) & Climat(Modéré) & Continent(Amérique) & Saison(Toutes)==> Destination(Mexico)'))


#-------------------------------------------------------------#
#Destination  18 : BuenosAires
#Groupe
dest_kb.tell(expr('Budget(Moyen) & Preference(Culture) & Interet(Tourisme) & Compagnie(Groupe) & Climat(Tropical) & Continent(Amérique) & Saison(Toutes)==> Destination(BuenosAires)'))
dest_kb.tell(expr('Budget(Moyen) & Preference(Histoire) & Interet(Tourisme) & Compagnie(Groupe) & Climat(Tropical) & Continent(Amérique) & Saison(Toutes)==> Destination(BuenosAires)'))

#Seul
dest_kb.tell(expr('Budget(Moyen) & Preference(Culture) & Interet(Tourisme) & Compagnie(Seul) & Climat(Tropical) & Continent(Amérique) & Saison(Toutes)==> Destination(BuenosAires)'))
dest_kb.tell(expr('Budget(Moyen) & Preference(Histoire) & Interet(Tourisme) & Compagnie(Seul) & Climat(Tropical) & Continent(Amérique) & Saison(Toutes)==> Destination(BuenosAires)'))

#Famille
dest_kb.tell(expr('Budget(Moyen) & Preference(Culture) & Interet(Tourisme) & Compagnie(Famille) & Climat(Tropical) & Continent(Amérique) & Saison(Toutes)==> Destination(BuenosAires)'))

#-------------------------------------------------------------#
#Destination  19 : Vancouver

#Groupe
dest_kb.tell(expr('Budget(Moyen) & Preference(Hiking) & Interet(Tourisme) & Compagnie(Groupe) & Climat(Océanique) & Continent(Amérique) & Saison(Toutes)==> Destination(Vancouver)'))
dest_kb.tell(expr('Budget(Moyen) & Preference(Aventure) & Interet(Alpinisme) & Compagnie(Groupe) & Climat(Océanique) & Continent(Amérique) & Saison(Toutes)==> Destination(Vancouver)'))

#Seul
dest_kb.tell(expr('Budget(Moyen) & Preference(Hiking) & Interet(Tourisme) & Compagnie(Seul) & Climat(Océanique) & Continent(Amérique) & Saison(Toutes)==> Destination(Vancouver)'))
dest_kb.tell(expr('Budget(Moyen) & Preference(Aventure) & Interet(Alpinisme) & Compagnie(Seul) & Climat(Océanique) & Continent(Amérique) & Saison(Toutes)==> Destination(Vancouver)'))

#Famille
dest_kb.tell(expr('Budget(Moyen) & Preference(Hiking) & Interet(Tourisme) & Compagnie(Famille) & Climat(Océanique) & Continent(Amérique) & Saison(Toutes)==> Destination(Vancouver)'))


#-------------------------------------------------------------#
#Destination  20 : Rio-De-Janeiro

#Groupe
dest_kb.tell(expr('Budget(Moyen) & Preference(Plage) & Interet(Tourisme) & Compagnie(Groupe) & Climat(Tropical) & Continent(Amérique) & Saison(Toutes)==> Destination(RioDeJaneiro)'))
dest_kb.tell(expr('Budget(Moyen) & Preference(Culture) & Interet(Tourisme) & Compagnie(Groupe) & Climat(Tropical) & Continent(Amérique) & Saison(Toutes)==> Destination(RioDeJaneiro)'))

#Seul
dest_kb.tell(expr('Budget(Moyen) & Preference(Plage) & Interet(Tourisme) & Compagnie(Seul) & Climat(Tropical) & Continent(Amérique) & Saison(Toutes)==> Destination(RioDeJaneiro)'))
dest_kb.tell(expr('Budget(Moyen) & Preference(Culture) & Interet(Tourisme) & Compagnie(Seul) & Climat(Tropical) & Continent(Amérique) & Saison(Toutes)==> Destination(RioDeJaneiro)'))

#Famille
dest_kb.tell(expr('Budget(Moyen) & Preference(Plage) & Interet(Tourisme) & Compagnie(Famille) & Climat(Tropical) & Continent(Amérique) & Saison(Toutes)==> Destination(RioDeJaneiro)'))








result=fol_fc_ask(dest_kb,expr('Destination(x)'))

print(list(result))