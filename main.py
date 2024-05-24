import blockchain
# Initilisation du blockchain pour difficulté 4
donnee = blockchain.Blockchain(4)
# Affichage du bloc Genesis
print(str(donnee.chain[0]) + 'n')

datas = [
    {'Expediteur':'abc@example.com', 'Recepteur':'xyz@example.com', 'code':4}, 
    {'Expediteur':'def@example.com', 'Recepteur':'ghi@example.com', 'code':10},  
    {'Expediteur':'jkl@example.com', 'Recepteur':'pqr@example.com', 'code':8}
    ]


for data in datas: # Affichage des autres blocs
    donnee.addBlock(data)
    print(donnee.chain[-1])
    print