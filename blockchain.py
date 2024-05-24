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