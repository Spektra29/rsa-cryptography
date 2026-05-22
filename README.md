# RSA Cryptography Project

A complete implementation and analysis of RSA cryptography from scratch using Python.

This project explores the mathematics, implementation, performance, and security of RSA public-key cryptography without using built-in cryptographic libraries.

---

# Features

- RSA key generation
- RSA encryption and decryption
- Miller-Rabin probabilistic primality testing
- Extended Euclidean Algorithm
- Fast modular exponentiation (square-and-multiply)
- Pollard Rho integer factorization
- Performance benchmarking
- Graph visualization
- Command-line interface (CLI)

---

# Technologies Used

- Python
- Matplotlib
- Random
- Time
- Math

---

# Project Structure

```text
rsa-cryptography/
│
├── graphs/
│   ├── benchmark_results.png
│   └── factorization_results.png
│
├── presentation/
│
├── report/
│
├── src/
│   ├── benchmarking.py
│   ├── cli.py
│   ├── factorization.py
│   ├── math_utils.py
│   ├── primality.py
│   └── rsa_core.py
│
├── README.md
├── requirements.txt
└── LICENSE
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/rsa-cryptography.git
```

## Navigate Into Project

```bash
cd rsa-cryptography
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Running the Project

## Start CLI

```bash
python src/cli.py
```

---

# CLI Features

```text
1. Generate RSA Keys
2. Encrypt Message
3. Decrypt Message
4. Run Benchmark Tests
5. Run Factorization Benchmark
6. Exit
```

---

# Benchmarking

The project benchmarks:

- Prime generation time
- RSA key generation time
- Pollard Rho factorization performance

Generated graphs are stored in:

```text
graphs/
```

---

# Mathematical Concepts Used

- Modular Arithmetic
- Euler Totient Function
- Greatest Common Divisor (GCD)
- Extended Euclidean Algorithm
- Fermat’s Little Theorem
- Euler’s Theorem

---

# Security Concepts

The project also explores:

- RSA computational asymmetry
- Integer factorization difficulty
- Textbook RSA vulnerabilities
- RSA-OAEP padding
- Hybrid encryption systems
- Quantum computing threats

---

# Example Output

## Encryption

```text
Original Message:
Hello RSA

Encrypted Message:
483920482394823948239482394
```

## Decryption

```text
Decrypted Message:
Hello RSA
```

---

# Future Improvements

- RSA-OAEP implementation
- Digital signatures
- GUI version
- AES hybrid encryption
- Post-quantum cryptography research

---

# Author

Boston Karymshakov

Penn State University
Computer Science