from Crypto.PublicKey import RSA
pub_keys=set() 
priv_keys=set()

for i in range(1000000):
	f = open("rsa_keys/"+str(i)+".pem", "wb")
	fd = open("rsa_keys/"+str(i)+"_p.pem", "wb")
	key = RSA.generate(1024) # Generation des clés RSA 1024 bits
	public = key.publickey().exportKey("PEM") # Extraction de la clé publique de l'entité key
	private = key.exportKey("PEM") # Extraction de la clé privé de l'entité key
	assert public not in pub_keys # Gestion des erreurs
	assert private not in priv_keys
	pub_keys.add(public) # Ecriture de la clé publique dans la liste public
	priv_keys.add(private) # Ecriture de la clé privé dans la liste private
	f.write(public) # Ecriture des clés publiques dans le fichier public
	fd.write(private) # Ecriture des clés privés dans le fichier public
	f.close() # Fermeture du fichier public.pem
	fd.close() # Fermeture du fichier private.pem
