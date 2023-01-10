from Crypto.PublicKey import RSA
from batch_gcd import batch_gcd
 
gcd_list = set()
for i in range (1000000):
	f = open("rsa_keys/"+str(i)+".pem", "r").read() # Ouverture des fichiers contenant les clés publiques RSA
	key = RSA.importKey(f) # Extraction des clés des fichiers 
	gcd_list.add(key.n) # Ajout des modulus n dans la liste

g = batch_gcd(*gcd_list) # Application de l'algorithme Batch GCD sur les modulus des clés
print(g)

