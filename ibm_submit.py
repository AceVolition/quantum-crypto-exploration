import os
from qiskit import QuantumCircuit, transpile
from qiskit_ibm_runtime import QiskitRuntimeService, SamplerV2 as Sampler

# Read API key securely from the file
with open(os.path.expanduser("~/.config/ibm-quantum/apikey"), "r") as f:
    api_key = f.read().strip()

# Connect to IBM
print("Connecting to IBM Quantum...")
service = QiskitRuntimeService(
    channel="ibm_quantum_platform", 
    token=api_key, 
    instance="crn:v1:bluemix:public:quantum-computing:us-east:a/7a0830401cff427ebbfd98fb1a56132f:ff360888-2c20-4846-a345-7e910dd5f3c0::"
)

# Find the least busy real quantum computer
backend = service.least_busy(operational=True, simulator=False)
print(f"Using backend: {backend.name}")

# Create Bell Circuit
qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)
qc.measure_all()

# Transpile and Submit
qc_transpiled = transpile(qc, backend=backend, optimization_level=3)
sampler = Sampler(backend)
job = sampler.run([qc_transpiled], shots=1024)

print(f"\nSUCCESS! YOUR JOB ID IS: {job.job_id()}\n")
