import time 
from Crypto.PublicKey import RSA
pub_keys=set()  
start_time=time.time()
for i in range(10000):
	f = open("time/"+str(i)+".pem", "wb")
	key = RSA.generate(1024) # Generation des clés RSA 1024 bits
	public = key.publickey().exportKey("PEM") # Extraction de la clé publique de l'entité key
	assert public not in pub_keys # Gestion des erreurs
	pub_keys.add(public) # Ecriture de la clé publique dans la liste public
	f.write(public) # Ecriture des clés publiques dans le fichier public
	f.close() # Fermeture du fichier public.pem
	# Calcul du temps nécessaire pour la génération des clés 
	if (i==1999):
		end_time=time.time()
		print("Temps d'execution pour 2000 clés = " + str(end_time-start_time) + "secs")
	if (i==3999):
		end_time=time.time()
		print("Temps d'execution pour 4000 clés = " + str(end_time-start_time) + "secs")
	if (i==7999):
		end_time=time.time()
		print("Temps d'execution pour 8000 clés = " + str(end_time-start_time) + "secs")
