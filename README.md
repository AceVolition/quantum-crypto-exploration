# Quantum Computing & Blockchain Cryptography

A hands-on exploration of real quantum hardware and proof-of-work cryptography.

## Quantum (Qiskit)
* `bell.py`: Generates a basic Bell State circuit on a local simulator.
* `noisy.py`: Simulates the circuit with a depolarizing noise model.
* `ibm_submit.py`: Submits a transpiled Bell State circuit to a real IBM Quantum processor (`ibm_fez`).
* `ibm_fetch.py`: Polls the IBM Cloud for the job status and prints the measurement counts.

## Blockchain
* `chain.py`: Demonstrates a simple SHA-256 hash chain.
* `mine.py`: A custom proof-of-work algorithm that brute-forces a nonce to find a hash with six leading zeros.
