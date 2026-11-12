import os
from qiskit_ibm_runtime import QiskitRuntimeService

with open(os.path.expanduser("~/.config/ibm-quantum/apikey"), "r") as f:
    api_key = f.read().strip()

# We must include the CRN here too
service = QiskitRuntimeService(
    channel="ibm_quantum_platform", 
    token=api_key, 
    instance="crn:v1:bluemix:public:quantum-computing:us-east:a/7a0830401cff427ebbfd98fb1a56132f:ff360888-2c20-4846-a345-7e910dd5f3c0::"
)

job = service.job("dbqi8bok09pc73ataf30")

print(f"Status: {job.status()}")
if str(job.status()) == "DONE":
    result = job.result()
    print(result[0].data.meas.get_counts())
