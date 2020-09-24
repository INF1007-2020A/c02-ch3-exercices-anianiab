#!/usr/bin/env python


def dissipated_power(voltage, resistance):
	# TODO: Calculer la puissance dissipée par la résistance.
	power = pow(voltage,2) / resistance
	return power

def orthogonal(v1, v2):
	# TODO: Retourner vrai si les vecteurs sont orthogonaux, faux sinon.
	v1[0] # Pour accéder au X
	v1[1] # Pour accéder au Y
	produit_scalaire = v1[0]*v2[0] + v1[1]*v2[1]
	return produit_scalaire == 0
	pass

def average(values):
	# TODO: Calculer la moyenne des valeurs positives (on ignore les valeurs strictement négatives).
	somme = 0
	nombre_valeur = 0
	
	for v in values:
    		if v >= 0:
    				nombre_valeur += 1
					somme += v
	return somme / nombre_valeur
		pass # La variable v contient une valeur de la liste.

def bills(value):
	# TODO: Calculez le nombre de billets de 20$, 10$ et 5$ et pièces de 1$ à remettre pour représenter la valeur.
	while value != 0:
		if value >= 20:
    			twenties = value // 20
				value = value - twenties*20
			pass
		elif value >= 10:
    			tens = value // 10
				value = value % 10	
			pass
		elif value >= 5:
    			fives = value // 5
                value = value % 5
			pass
		elif value >= 1:
    			ones = value // 1
				value = 0
	      	pass

	return (twenties, tens, fives, twos, ones);

if __name__ == "__main__":
	print(dissipated_power(69, 420))
	print(orthogonal((1, 1), (-1, 1)))
	print(average([1, 4, -2, 10]))
	print(bills(137))
