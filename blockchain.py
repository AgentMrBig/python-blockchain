from block import Block


class Blockchain:
    """
    Blackchain: a public ledger of transactions.
    Implemented as a list of blocks - data sets of transations
    """

    def __init__(self):
        self.chain = []

    def add_block(self, data):
        self.chain.append(Block(data))

    def __repr__(self):
        return f'Blockchain: {self.chain}'


blockchain = Blockchain()
blockchain.add_block('one')
blockchain.add_block('two')


print(blockchain)
