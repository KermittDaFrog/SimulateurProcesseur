import sys
 
hexadecimal =  ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
 
for ligne in sys.stdin:
    groupes = ligne.split()
	#Si la ligne a moins 2 groupes de mots alors il n'y a pas d'instruction sur cette ligne
    if len(groupes) < 2:
        continue
	#Si la taille du groupe de mot censé correspondre à l'instruction machine n'est pas égale à 8 alors ce n'est pas une instruction
    if len(groupes[1]) != 8:
        continue
	#Si le premier caractere du groupe de mot censé correspondre à l'instruction machine n'est pas un hexadecimal alors ce n'est pas une instruction
    if groupes[1][0] not in hexadecimal:
        continue
	#On affiche l'instruction
    print groupes[1]