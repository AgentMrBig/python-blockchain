class Block:
    """
    Block: a unit of storage.
    Store transactions in a blockchain that supports a cryptocurrency.
    """
    def __init__(self, data):
        self.data = data

class Blockchain:
    """ 
    Blackchain: a public ledger of transactions.
    Implemented as a list of blocks - data sets of transations
    """
    def __init__(self):
        self.chain = []

    def add_block(self, data):
        self.chain.append(Block(data))

blockchain = Blockchain()
blockchain.add_block('one')
blockchain.add_block('two')
blockchain.add_block('three')

print(blockchain)
