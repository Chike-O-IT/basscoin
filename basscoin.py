import hashlib
import time

# Define what a Basscoin block is
class Block:
    def __init__(self, index: int, timestamp: int, data: str, previous_hash):
        """
        :param index: block index
        :param timestamp: millisecond
        :param data: block real data
        :param previous_hash: previous block hash
        """
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()

    def hash_block(self):
        sha = hashlib.sha256()
        seq = [
            str(x) for x in [self.index, self.timestamp, self.data, self.previous_hash]
        ]
        sha.update("".join(seq).encode("utf8"))
        return sha.hexdigest()

    def __str__(self):
        return f"Block:index={self.index}&timestamp={self.timestamp}&data={self.data}&hash={self.hash}"


def get_cur_millisecond():
    return int(round(time.time() * 1000))

# Generate genesis block
def create_genesis_block():
    # Manually construct a block with
    # index zero and arbitrary previous hash
    return Block(0, get_cur_millisecond(), "snake coin genesis block", "0")

# Generate all later blocks in the blockchain
def next_block(previous_block: Block):
    index = previous_block.index + 1
    return Block(
        index=index,
        timestamp=get_cur_millisecond(),
        data=f"this is block #{index}",
        previous_hash=previous_block.hash,
    )

# Create the blockchain and add the genesis block
def make_test_block_chain():
    block_chain = [create_genesis_block()]
    previous_block = block_chain[0]
# How many blocks should we add to the chain after the genesis block??
    for _ in range(50):
        block = next_block(previous_block)
        block_chain.append(block)
        previous_block = block
        # broadcast: tell everyone about it!
        print(f"Block #{block.index} has been added to the blockchain! detail: {block}")
        time.sleep(1)


if __name__ == "__main__":
    make_test_block_chain()
    
print("WELCOME TO BASSCOIN")
