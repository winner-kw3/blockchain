#debut du projet
from hashlib import sha256
from datetime import datetime

class Block(object): # Methode pour class bloc
     
    def __init__ (self, index, Data, previousHash, difficulty): 
        """Constructor for Block object"""
        self.index = index
        self.Data = Data
        self.previousHash = previousHash
        self.difficulty = difficulty
        self.HD = datetime.now()
        self.nonce = 0
        self.hash = self.mineBlock()
        
    def __str__(self): # Représentation des contenues de blocs
        block_string = ''.join([
            "index: " + str(self.index) + '\n',
            "previousHash: " + self.previousHash + '\n',
            "HD: " + str(self.HD) + '\n',
            "hash:" + self.hash + '\n',
            "Data: " + str(self.Data) + 'n'
            
            
            ])
        return block_string 
    
    def calculateHash(self): # Calcule du hash 
        """Calculate a hash based on the Block contents and nonce value"""
        hash_string = ''.join([
            str(self.index), 
            str(self.HD), 
            str(self.nonce), 
            str(self.Data), 
            self.previousHash
            ])
        return sha256(hash_string.encode('ascii')).hexdigest()
    def mineBlock(self): # Trouver le hash valide pour le bloc à base de la difficulté
        """Find a valid hash for the Block contents, based on difficulty"""
        while self.calculateHash()[:self.difficulty] != ('0' * self.difficulty):
            self.nonce += 1
        return self.calculateHash()

class Blockchain(object): # Methode et attribut pour la classe blockchain

    def init(self, difficulty=4): # Construcuteur pour l#objet blockchain
        self.index = 0
        self.difficulty = difficulty
        # create Genesis Block on the chain of Blocks
        self.chain = [Block(self.index, 'Genesis Block', '0'*64, self.difficulty)]

    def addBlock(self, Data): # ajoute de nouveau bloc à la blockchain
        self.index += 1
        newBlock = Block(self.index, Data, self.getLastBlock().hash, self.difficulty)
        self.chain.append(newBlock)