# Cameron M. Merrick
# 2/10/2017
# Python - Custom Blockchain
# An implementation of the blockchain in Python.
# For educational purposes and for development of my GitHub portfolio.


import hashlib as hasher
import datetime as date


class Block:

    def __init__(self, index, timestamp, data, p_hash):
        # Initialize the members of a Block object
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.p_hash = p_hash
        self.hash = self.hash_block()

    def hash_block(self):
        sha = hasher.sha256()
        sha.update(str(self.index).encode(encoding='utf_8', errors='strict') + str(self.timestamp).encode(encoding='utf_8', errors='strict') + str(self.data).encode(encoding='utf_8', errors='strict') + str(self.p_hash).encode(encoding='utf_8'))
        return sha.hexdigest()


# Create a new block at the margin (end) of the chain as it grows
def next_block(last_block):
    this_index = last_block.index + 1
    this_timestamp = date.datetime.now()
    this_data = "001010001011010111010100" + str(this_index)
    this_hash = last_block.hash
    return Block(this_index, this_timestamp, this_data, this_hash)


# Create 'Genesis' Block (to be called first in main)
def make_genesis():
    # Manually create the first block with user defined params
    return Block(0, date.datetime.now(), "GENESIS [...]", "0")


# Testing the blockchain architecture
def main():
    # Start with the genesis block as a standalone code chunk
    blockchain = [make_genesis()]
    previous_block = blockchain[0]

    # Define the number of blocks to simulate
    blockchain_length = 20

    # Add blocks to the chain via a for loop
    for i in range(0, blockchain_length):
        staged_block = next_block(previous_block)
        blockchain.append(staged_block)
        previous_block = staged_block
        print("Block # {} added to the blockchain".format(staged_block.index))
        print("Hash: {}\n".format(staged_block.hash))


if __name__ == "__main__":
    main()




# Minor thing: For Python 3.6, you need to encode hash_block like
#
# def hash_block(self):
#  sha = hasher.sha256()
#  sha.update((str(self.index) +
#  str(self.timestamp) +
#  str(self.data) +
#  str(self.previous_hash)).encode()) #change here
# return sha.hexdigest()
