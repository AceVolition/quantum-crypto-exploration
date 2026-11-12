import hashlib
import time

netid = "bgonz0123"
data = "Transaction Data"
target = "000000" # Six zeros
nonce = 0

print("--- mine.py Output ---")
print(f"Mining block with target: {target}...")
start_time = time.time()

while True:
    block_text = f"{netid}{data}{nonce}"
    block_hash = hashlib.sha256(block_text.encode()).hexdigest()

    if block_hash.startswith(target):
        end_time = time.time()
        print(f"Success! Found hash: {block_hash}")
        print(f"Winning Nonce: {nonce}")
        print(f"Attempts (Tries): {nonce + 1}")
        print(f"Time taken: {end_time - start_time:.2f} seconds")
        break
    nonce += 1
