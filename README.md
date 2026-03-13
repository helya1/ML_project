# Chromosome Classification using Machine Learning

This repository contains the implementation of a machine learning project developed for the **M1 Statistics – Machine Learning course**.

The objective of the project is to automatically recognize the **chromosome class (1–22)** from a **1D intensity profile extracted from chromosome images**.

The project studies several approaches:

- Random Forest classification using raw signal data
- Dimension reduction using PCA
- Functional representation using:
  - Fourier decomposition
  - B-spline decomposition

The performance of the models is analyzed as a function of the **deformation intensity (`strength`)** applied to the chromosome profiles.

---

# Dataset

The dataset contains **110,000 simulated chromosome profiles**.

Each observation contains:

- `result` → 1D signal discretized on 100 points
- `target_class` → chromosome class (1–22)
- `strength` → deformation intensity
- `sigma` → second deformation parameter (constant in this dataset)

The goal is to predict **target_class** using **result only**.

---

# Methods implemented

The following methods are implemented:

### 1. Random Forest (baseline)

Classification directly from the 100-dimensional signal.

### 2. Dimension Reduction

Principal Component Analysis (PCA) is used to evaluate whether reducing the dimensionality improves classification performance.

### 3. Functional Representation

Instead of treating the signal as a vector, it is interpreted as a function and decomposed into:

- Fourier basis coefficients
- B-spline basis coefficients

These coefficients are then used as input for the classifier.

---

# Repository Structure
