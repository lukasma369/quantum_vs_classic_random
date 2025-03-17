import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import chisquare
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

# Number of numbers generated
num_samples = 10000 

# Classic randomness with NumPy
classic_random_numbers = np.random.randint(0, 2, num_samples)

# Quantum coincidence with Qiskit
def generate_quantum_random_numbers(n):
    qc = QuantumCircuit(1, 1)
    qc.h(0)
    qc.measure(0, 0)

    simulator = AerSimulator()
    job = simulator.run(qc, shots=n)
    result = job.result()
    counts = result.get_counts()

    # Convert the results to a binary list
    bitstring = ''.join([k * v for k, v in counts.items()])
    return np.array([int(bit) for bit in bitstring[:n]])

quantum_random_numbers = generate_quantum_random_numbers(num_samples)

# Histogram of both generators
plt.figure(figsize=(12, 5))
plt.hist(classic_random_numbers, bins=2, alpha=0.6, label="Klasická náhoda (NumPy)")
plt.hist(quantum_random_numbers, bins=2, alpha=0.6, label="Kvantová náhoda (Qiskit)")
plt.xticks([0, 1])
plt.xlabel("Vygenerovaná hodnota")
plt.ylabel("Počet výskytů")
plt.title("Porovnání náhodnosti: NumPy vs. Qiskit")
plt.legend()
plt.show()

# Statistical analysis (Chi-Square test for equality)
classic_chi, classic_p = chisquare(np.bincount(classic_random_numbers, minlength=2))
quantum_chi, quantum_p = chisquare(np.bincount(quantum_random_numbers, minlength=2))

print(f"Chi-Square Test (NumPy): χ² = {classic_chi:.2f}, p-hodnota = {classic_p:.5f}")
print(f"Chi-Square Test (Qiskit): χ² = {quantum_chi:.2f}, p-hodnota = {quantum_p:.5f}")

# Conclusion: If p-value > 0.05, the distribution is uniform
