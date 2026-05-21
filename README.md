# A Short Expository Note on a Modular Sieve for Rational Points on Mordell Curves

This repository contains a short expository note and a small Python implementation of a modular sieve for finding integer points on Mordell curves of the form

y² = x³ + k.

The project is educational and experimental. The parametrization and local congruence ideas used here are standard in arithmetic geometry. The goal is to provide a clean, reproducible example of how congruence filters can reduce a finite search space for integer points on Mordell curves.

## What the code does

The program checks candidate integer values of `x` in a bounded interval. For each candidate, it tests whether `x³ + k` can be a square modulo several selected primes.

If `x³ + k` is not a quadratic residue modulo one of these primes, then it cannot be an integer square. Candidates that pass the modular filters are then checked directly over the integers.

This gives a simple computational demonstration of a modular sieve.

## What this project does not claim

This repository does not claim to prove the Birch and Swinnerton-Dyer conjecture.

It does not claim to provide a new rank algorithm.

It does not claim mathematical novelty.

It is a compact educational implementation intended for learning, testing, and reproducibility.

## Repository structure

```text
mordell-modular-sieve/
├── mordell_sieve/
│   ├── __init__.py
│   └── sieve.py
├── examples/
│   └── run_examples.py
├── benchmarks/
│   └── small_benchmark.py
├── README.md
├── SETUP_INSTRUCTIONS.md
├── requirements.txt
├── CITATION.cff
├── LICENSE
└── .gitignore
