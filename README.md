Quantum mechanics allows for truly random numbers thanks to the principle of superposition and measurement of quantum bits (qubits).
Are quantum generators better than classical ones? We will find out experimentally!

Key code snippet:
import numpy as np
from qiskit import Aer, QuantumCircuit, execute

def quantum_rng():
    circuit = QuantumCircuit(1, 1)
    circuit.h(0)  
    circuit.measure(0, 0)
    result = execute(circuit, Aer.get_backend('qasm_simulator'), shots=1).result()
    return int(list(result.get_counts().keys())[0])

classic_random = np.random.randint(0, 10, 1000)
quantum_random = [quantum_rng() for _ in range(1000)]

📖 IBM Quantum Computing
📝 Qiskit Documentation
🔬 Principles of Quantum Randomness
