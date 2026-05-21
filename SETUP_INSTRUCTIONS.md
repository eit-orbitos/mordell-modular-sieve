# SETUP_INSTRUCTIONS.md

Ова се практични чекори за да го ставиш проектот на GitHub без претерано тврдење.

## 1. Направи GitHub repository

На GitHub избери **New repository**.

Recommended settings:

```text
Repository name: mordell-modular-sieve
Visibility: Public
Add README: Off
Add .gitignore: Off
Add license: Off
```

Не додавај README/license преку GitHub формата, затоа што тие веќе се во ZIP пакетот.

## 2. GitHub description

Краток и чист опис:

```text
Expository Python implementation of a modular sieve for rational points on Mordell curves y² = x³ + k.
```

Topics што можеш да ги додадеш:

```text
number-theory
arithmetic-geometry
elliptic-curves
mordell-curves
python
educational
modular-arithmetic
```

## 3. Отпакувај ZIP локално

```bash
unzip mordell-modular-sieve.zip
cd mordell-modular-sieve
```

## 4. Замени YOUR_USERNAME

Во овие два фајла замени `YOUR_USERNAME` со твојот GitHub username:

```text
README.md
CITATION.cff
```

Пример:

```text
https://github.com/eit-orbitos/mordell-modular-sieve
```

## 5. Провери дека кодот работи

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python examples/run_examples.py
python benchmarks/small_benchmark.py
```

Windows PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python examples\run_examples.py
python benchmarks\small_benchmark.py
```

## 6. Push на GitHub

```bash
git init
git add .
git commit -m "Initial educational modular sieve note"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/mordell-modular-sieve.git
git push -u origin main
```

## 7. Release notes за v0.1.0

Title:

```text
v0.1.0 — Educational modular sieve note
```

Release description:

```text
Initial public educational release.

Includes:
- Short README explaining the scope and limitations
- Simple Python implementation of a modular sieve for bounded searches on Mordell curves y² = x³ + k
- Example runs and a small benchmark script
- CITATION.cff metadata
- MIT License

Claim level:
- Expository / pedagogical implementation
- No novelty claim
- No BSD claim
- No rank algorithm claim
```

## 8. Email tone

Email-от треба да биде краток, скромен и јасен. Не тврди дека имаш доказ. Кажи дека е мала експозиторна белешка и дека бараш насока/совет.

Suggested subject:

```text
Short expository note on a modular sieve for Mordell curves
```

Suggested email:

```text
Dear Professor [Last Name],

My name is Toni Mladenovski. I am sharing a small educational GitHub repository containing a short expository Python implementation of a modular sieve for bounded searches for integer points on Mordell curves of the form y² = x³ + k.

I am not claiming novelty or a result on BSD. The project is meant as a clean pedagogical note showing how local congruence filters can reduce a finite search space before direct integer-square checking.

Repository:
https://github.com/YOUR_USERNAME/mordell-modular-sieve

I would be grateful for any brief advice on whether the exposition is mathematically clear, and whether there are standard references or improvements I should add.

Thank you for your time.

Sincerely,
Toni Mladenovski
```

## 9. arXiv / Zenodo advice

For now, GitHub is enough. Do not upload to arXiv unless a qualified mathematician or mentor reviews the note first. Zenodo can be used later if you want a DOI for the GitHub release, but it is optional.

## 10. Final status

```text
PROJECT: mordell-modular-sieve
STATUS: GitHub-ready educational repository
CLAIM LEVEL: Expository / pedagogical implementation
RESEARCH CLAIM: No
BSD CLAIM: No
RANK ALGORITHM CLAIM: No
VALUE: Clean reproducible note + code + benchmark
```
