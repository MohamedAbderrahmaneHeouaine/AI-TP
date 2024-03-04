from aima3.logic import *

kb = FolKB()

regions = ['1', '2', '3', '4', '5', '6']
colors = ['Blue', 'Green', 'White', 'Black']
adjacents = [('3','4'), ('3','2'), ('3','1'), ('3','6'), ('1','2'), ('1','6'), ('1','5'), ('5','6'), ('2','5'), ('2','4')]




for color in colors:
    for color in colors:
        if color != color:
           kb.tell(expr(f'Different({color}, {color})'))


#for region in regions:
    #for color in colors:
       # kb.tell(expr(f'Color({region}, {color})'))


for region1 in regions:
    for region2 in regions:
      if (region1, region2) in adjacents and (region2, region1) in adjacents:
          kb.tell(expr(f'{color}({region1}) & {color}({region2}) ==> AdjacentSameColor({region1}, {region2})'))
          kb.tell(expr(f'AdjacentSameColor({region1}, {region2}) ==> AdjacentSameColor({region2}, {region1})'))


for region1 in regions:
    for region2 in regions:
        if (region1, region2) not in adjacents and (region2, region1) not in adjacents:
            kb.tell(expr(f'NonAdjacent({region1}, {region2})'))

for region1 in regions:
    for region2 in regions:
        if region1 != region2:
            for color in colors:
                kb.tell(expr(f'NonAdjacent({region1}, {region2}) & Color({region1}, {color}) ==> Color({region2}, {color})'))
                kb.tell(expr(f'NonAdjacent({region1}, {region2}) & Color({region2}, {color}) ==> Color({region1}, {color})'))
        

result = kb.ask(expr('Color(1, Green) & Color(2, Green)'))

if result is not None and result is not False:
    print(True)
else:
    print(False)