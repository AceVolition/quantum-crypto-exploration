import hashlib

def hash_block(block):
    return hashlib.sha256(str(block).encode()).hexdigest()


block1 = {"sender": "bgonz0123", "receiver": "Bob", "amount": 10}
block2 = {"sender": "Bob", "receiver": "Charlie", "amount": 5}

block1_hash = hash_block(block1)
block2["previous_hash"] = block1_hash
block2_hash = hash_block(block2)

print("--- chain.py Output ---")
print(f"Block 1: {block1}")
print(f"Block 1 Hash: {block1_hash}\n")
print(f"Block 2: {block2}")
print(f"Block 2 Hash: {block2_hash}")
