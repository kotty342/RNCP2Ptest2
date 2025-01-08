class Blockchain:
    def __init__(self):
        self.chain = []

    def add_record(self, hash_value):
        self.chain.append(hash_value)

    def get_chain(self):
        return self.chain

    def __len__(self):
        return len(self.chain)