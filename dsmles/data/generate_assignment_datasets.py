"""
Generate all pre-generated datasets for assignment notebooks.
Run this script once to create all CSV files that assignments will load.
All datasets use seed=42 for reproducibility.
"""

import numpy as np
import pandas as pd
from sklearn.datasets import make_classification
import os

DATA_DIR = os.path.dirname(os.path.abspath(__file__))

def save_csv(df, filename):
    """Save DataFrame to CSV in the data directory."""
    path = os.path.join(DATA_DIR, filename)
    df.to_csv(path, index=False)
    print(f"Created: {filename} ({len(df)} rows)")

# ==============================================================================
# hw03-intermediate-pandas: batch reactor data
# ==============================================================================
print("\n=== hw03-intermediate-pandas ===")

np.random.seed(42)
n = 200
batch_data = pd.DataFrame({
    'batch_id': [f'B{i:04d}' for i in range(1, n+1)],
    'reactor': np.random.choice(['R1', 'R2', 'R3'], n),
    'shift': np.random.choice(['day', 'night'], n),
    'temperature': np.round(np.random.uniform(350, 450, n), 1),
    'pressure': np.round(np.random.uniform(1, 5, n), 2),
    'feed_rate': np.round(np.random.uniform(50, 150, n), 1),
    'conversion': np.round(np.random.uniform(0.6, 0.95, n), 3),
    'yield': np.round(np.random.uniform(0.5, 0.9, n), 3)
})
save_csv(batch_data, 'hw03_batch_data.csv')

reactor_specs = pd.DataFrame({
    'reactor': ['R1', 'R2', 'R3'],
    'volume_L': [1000, 1500, 800],
    'max_temp': [500, 480, 520],
    'commissioned': ['2018-03-15', '2019-07-22', '2020-01-10']
})
save_csv(reactor_specs, 'hw03_reactor_specs.csv')

# ==============================================================================
# hw04-feature-engineering
# ==============================================================================
print("\n=== hw04-feature-engineering ===")

# Problem 1: Process data
np.random.seed(42)
n = 100
temp = np.random.uniform(300, 500, n)
pressure = np.random.uniform(1, 10, n)
flow = np.random.uniform(10, 100, n)
catalyst = np.random.uniform(0.1, 2, n)
conversion = 0.1 * (temp - 300) / 200 + 0.05 * pressure + 0.01 * flow + 0.2 * catalyst + np.random.normal(0, 0.05, n)
conversion = np.clip(conversion, 0, 1)

hw04_process = pd.DataFrame({
    'temperature': temp,
    'pressure': pressure,
    'flow_rate': flow,
    'catalyst_loading': catalyst,
    'conversion': conversion
})
save_csv(hw04_process, 'hw04_process_data.csv')

# Problem 2: Arrhenius kinetics data
np.random.seed(42)
n = 80
T = np.random.uniform(300, 500, n)
A, Ea, R = 1e10, 60000, 8.314
k_true = A * np.exp(-Ea / (R * T))
k_obs = k_true * np.exp(np.random.normal(0, 0.15, n))

hw04_kinetics = pd.DataFrame({
    'temperature': T,
    'rate_constant': k_obs
})
save_csv(hw04_kinetics, 'hw04_kinetics_data.csv')

# Problem 3: Catalyst categorical data
np.random.seed(42)
n = 120
hw04_catalyst = pd.DataFrame({
    'catalyst_type': np.random.choice(['Pt', 'Pd', 'Ni', 'Cu'], n),
    'support': np.random.choice(['Al2O3', 'SiO2', 'TiO2'], n),
    'preparation': np.random.choice(['impregnation', 'coprecipitation', 'sol-gel'], n),
    'loading_wt_pct': np.round(np.random.uniform(0.5, 5, n), 2),
    'activity': np.round(np.random.uniform(10, 100, n), 1)
})
save_csv(hw04_catalyst, 'hw04_catalyst_data.csv')

# ==============================================================================
# hw05-dimensionality-reduction
# ==============================================================================
print("\n=== hw05-dimensionality-reduction ===")

# Problem 1: Spectroscopic data
np.random.seed(42)
n_samples = 100
n_wavelengths = 50
wavelengths = np.linspace(400, 700, n_wavelengths)

concentration = np.random.uniform(0.1, 1.0, n_samples)
temperature = np.random.uniform(25, 75, n_samples)

spectra = np.zeros((n_samples, n_wavelengths))
for i in range(n_samples):
    peak1 = np.exp(-((wavelengths - (500 + 20*concentration[i])) ** 2) / 200) * concentration[i]
    peak2 = np.exp(-((wavelengths - (600 - 10*temperature[i]/50)) ** 2) / 300) * (temperature[i]/50)
    spectra[i] = peak1 + peak2 + np.random.normal(0, 0.02, n_wavelengths)

hw05_spectra = pd.DataFrame(spectra, columns=[f'wl_{int(w)}' for w in wavelengths])
hw05_spectra['concentration'] = concentration
hw05_spectra['temperature'] = temperature
save_csv(hw05_spectra, 'hw05_spectroscopic_data.csv')

# Problem 2: Catalyst properties
np.random.seed(42)
n = 150
type_a = np.random.multivariate_normal([100, 50, 0.8, 300, 25, 1.2, 0.05, 2.5, 80, 15], np.eye(10)*[100, 25, 0.01, 400, 10, 0.1, 0.001, 0.25, 50, 5], 50)
type_b = np.random.multivariate_normal([150, 30, 0.5, 250, 35, 0.8, 0.08, 3.0, 60, 20], np.eye(10)*[100, 25, 0.01, 400, 10, 0.1, 0.001, 0.25, 50, 5], 50)
type_c = np.random.multivariate_normal([80, 70, 0.9, 350, 20, 1.5, 0.03, 2.0, 90, 10], np.eye(10)*[100, 25, 0.01, 400, 10, 0.1, 0.001, 0.25, 50, 5], 50)

hw05_catalyst = pd.DataFrame(
    np.vstack([type_a, type_b, type_c]),
    columns=['surface_area', 'pore_volume', 'acidity', 'crystallite_size',
             'metal_dispersion', 'reduction_temp', 'impurity_level', 'particle_size',
             'activity', 'selectivity']
)
hw05_catalyst['catalyst_type'] = ['Type_A']*50 + ['Type_B']*50 + ['Type_C']*50
save_csv(hw05_catalyst, 'hw05_catalyst_properties.csv')

# ==============================================================================
# hw06-linear-regression
# ==============================================================================
print("\n=== hw06-linear-regression ===")

# Problem 1: Simple regression
np.random.seed(42)
temp_simple = np.array([300, 320, 340, 360, 380, 400, 420, 440, 460, 480])
purity = 85 + 0.03 * (temp_simple - 300) + np.random.normal(0, 0.5, 10)

hw06_simple = pd.DataFrame({
    'temperature': temp_simple,
    'purity': purity
})
save_csv(hw06_simple, 'hw06_simple_regression.csv')

# Problem 2: Multiple regression
np.random.seed(42)
n = 100
temp = np.random.uniform(300, 500, n)
pressure = np.random.uniform(1, 10, n)
catalyst = np.random.uniform(0.5, 5, n)
time = np.random.uniform(10, 60, n)
yield_val = 20 + 0.1*(temp-300) + 2*pressure + 5*catalyst + 0.3*time + np.random.normal(0, 3, n)

hw06_multiple = pd.DataFrame({
    'temperature': temp,
    'pressure': pressure,
    'catalyst_loading': catalyst,
    'residence_time': time,
    'yield': yield_val
})
save_csv(hw06_multiple, 'hw06_multiple_regression.csv')

# ==============================================================================
# hw07-classification
# ==============================================================================
print("\n=== hw07-classification ===")

# Problem 1: QC binary classification
np.random.seed(42)
n = 200
temp_dev = np.random.normal(0, 2, n)
press_dev = np.random.normal(0, 1.5, n)
viscosity = np.random.uniform(50, 150, n)
quality_score = -0.3*np.abs(temp_dev) - 0.4*np.abs(press_dev) + 0.01*(viscosity-100) + np.random.normal(0, 0.5, n)
quality = (quality_score > 0).astype(int)

hw07_qc = pd.DataFrame({
    'temp_deviation': temp_dev,
    'pressure_deviation': press_dev,
    'viscosity': viscosity,
    'quality': quality
})
save_csv(hw07_qc, 'hw07_qc_classification.csv')

# Problem 2: Multi-class catalyst classification
np.random.seed(42)
X_cat, y_cat = make_classification(n_samples=150, n_features=4, n_informative=3,
                                    n_redundant=1, n_classes=3, n_clusters_per_class=1,
                                    random_state=42)
hw07_catalyst = pd.DataFrame(X_cat, columns=['surface_area', 'pore_volume', 'acidity', 'activity'])
hw07_catalyst['catalyst_type'] = y_cat
save_csv(hw07_catalyst, 'hw07_catalyst_classification.csv')

# ==============================================================================
# hw08-regularization
# ==============================================================================
print("\n=== hw08-regularization ===")

# Problem 1: Polynomial overfitting
np.random.seed(42)
x = np.linspace(0, 10, 30)
y = 3 + 2*x - 0.1*x**2 + np.random.normal(0, 2, 30)

hw08_poly = pd.DataFrame({'x': x, 'y': y})
save_csv(hw08_poly, 'hw08_polynomial.csv')

# Problem 2: High-dimensional sparse
np.random.seed(42)
n_samples, n_features = 100, 50
X = np.random.randn(n_samples, n_features)
true_coef = np.zeros(n_features)
true_coef[[0, 5, 10, 20, 35]] = [3, -2, 1.5, -1, 0.8]  # Only 5 relevant features
y = X @ true_coef + np.random.normal(0, 1, n_samples)

hw08_sparse = pd.DataFrame(X, columns=[f'feature_{i}' for i in range(n_features)])
hw08_sparse['target'] = y
save_csv(hw08_sparse, 'hw08_sparse_features.csv')

# ==============================================================================
# hw09-nonlinear-methods
# ==============================================================================
print("\n=== hw09-nonlinear-methods ===")

# Problem 1: Reaction rate data
np.random.seed(42)
n = 150
T = np.random.uniform(300, 500, n)
C = np.random.uniform(0.1, 2, n)
rate = 1e8 * np.exp(-50000/(8.314*T)) * C**1.5 * np.exp(np.random.normal(0, 0.1, n))

hw09_kinetics = pd.DataFrame({
    'temperature': T,
    'concentration': C,
    'rate': rate
})
save_csv(hw09_kinetics, 'hw09_reaction_kinetics.csv')

# Problem 2: Complex process data
np.random.seed(42)
n = 200
temp = np.random.uniform(300, 500, n)
pressure = np.random.uniform(1, 20, n)
catalyst = np.random.uniform(0.5, 5, n)
conversion = (
    0.3 * np.tanh(0.01 * (temp - 350)) +
    0.2 * (1 - np.exp(-0.1 * pressure)) +
    0.15 * np.log(catalyst + 1) +
    0.1 * temp * pressure / 5000 +
    np.random.normal(0, 0.03, n)
)
conversion = np.clip(conversion, 0, 1)

hw09_process = pd.DataFrame({
    'temperature': temp,
    'pressure': pressure,
    'catalyst_loading': catalyst,
    'conversion': conversion
})
save_csv(hw09_process, 'hw09_process_data.csv')

# ==============================================================================
# hw10-ensemble-methods
# ==============================================================================
print("\n=== hw10-ensemble-methods ===")

np.random.seed(42)
n = 300
temp = np.random.uniform(300, 500, n)
pressure = np.random.uniform(1, 20, n)
mol_weight = np.random.uniform(100, 500, n)
crystallinity = np.random.uniform(0, 1, n)
additive = np.random.uniform(0, 5, n)
cooling_rate = np.random.uniform(1, 20, n)

strength = (
    50 * np.log(mol_weight / 100) +
    30 * crystallinity +
    10 * np.tanh(0.5 * additive) +
    -5 * np.log(cooling_rate) +
    0.02 * (temp - 300) * crystallinity +
    np.random.normal(0, 5, n)
)

hw10_polymer = pd.DataFrame({
    'temperature': temp,
    'pressure': pressure,
    'molecular_weight': mol_weight,
    'crystallinity': crystallinity,
    'additive_concentration': additive,
    'cooling_rate': cooling_rate,
    'tensile_strength': strength
})
save_csv(hw10_polymer, 'hw10_polymer_properties.csv')

# ==============================================================================
# hw11-clustering
# ==============================================================================
print("\n=== hw11-clustering ===")

# Problem 1: Operating regimes
np.random.seed(42)
regime1 = np.random.multivariate_normal([350, 2, 80], [[100, 0, 0], [0, 0.1, 0], [0, 0, 25]], 40)
regime2 = np.random.multivariate_normal([400, 5, 120], [[100, 0, 0], [0, 0.5, 0], [0, 0, 50]], 45)
regime3 = np.random.multivariate_normal([450, 8, 90], [[150, 0, 0], [0, 0.3, 0], [0, 0, 30]], 40)

hw11_regimes = pd.DataFrame(
    np.vstack([regime1, regime2, regime3]),
    columns=['temperature', 'pressure', 'flow_rate']
)
hw11_regimes['true_regime'] = [0]*40 + [1]*45 + [2]*40
save_csv(hw11_regimes, 'hw11_operating_regimes.csv')

# Problem 2: Catalyst samples (small hand-designed)
np.random.seed(42)
hw11_catalyst_small = pd.DataFrame({
    'surface_area': [250, 255, 245, 260, 248, 150, 155, 148, 152, 145,
                     300, 305, 298, 310, 295, 180, 175, 185, 178, 182],
    'pore_volume': [0.8, 0.82, 0.78, 0.85, 0.79, 0.5, 0.52, 0.48, 0.51, 0.49,
                    0.9, 0.92, 0.88, 0.95, 0.89, 0.6, 0.58, 0.62, 0.59, 0.61],
    'acidity': [1.2, 1.25, 1.18, 1.3, 1.22, 0.8, 0.82, 0.78, 0.81, 0.79,
                1.5, 1.52, 1.48, 1.55, 1.49, 1.0, 0.98, 1.02, 0.99, 1.01]
})
save_csv(hw11_catalyst_small, 'hw11_catalyst_samples.csv')

# Problem 3: Data with outliers
np.random.seed(42)
mode1 = np.random.multivariate_normal([50, 100], [[25, 0], [0, 100]], 50)
mode2 = np.random.multivariate_normal([80, 150], [[25, 0], [0, 100]], 50)
outliers = np.array([[20, 200], [90, 50], [60, 250], [100, 80]])

hw11_outliers = pd.DataFrame(
    np.vstack([mode1, mode2, outliers]),
    columns=['conversion', 'selectivity']
)
save_csv(hw11_outliers, 'hw11_outlier_data.csv')

# ==============================================================================
# hw12-uncertainty-quantification
# ==============================================================================
print("\n=== hw12-uncertainty-quantification ===")

# Problem 1: Rate vs temperature
np.random.seed(42)
T = np.array([300, 320, 340, 360, 380, 400, 420, 440, 460, 480])
A, Ea, R = 1e10, 50000, 8.314
k = A * np.exp(-Ea/(R*T)) * np.exp(np.random.normal(0, 0.2, 10))

hw12_arrhenius = pd.DataFrame({'temperature': T, 'rate_constant': k})
save_csv(hw12_arrhenius, 'hw12_arrhenius.csv')

# Problem 2: 2D regression
np.random.seed(42)
n = 50
x1 = np.random.uniform(0, 10, n)
x2 = np.random.uniform(0, 5, n)
y = 2 + 3*x1 - 0.5*x2 + 0.1*x1*x2 + np.random.normal(0, 2, n)

hw12_2d = pd.DataFrame({'x1': x1, 'x2': x2, 'y': y})
save_csv(hw12_2d, 'hw12_2d_regression.csv')

# ==============================================================================
# hw13-model-interpretability
# ==============================================================================
print("\n=== hw13-model-interpretability ===")

np.random.seed(42)
n = 300
temp = np.random.uniform(300, 500, n)
pressure = np.random.uniform(1, 20, n)
catalyst = np.random.uniform(0.5, 5, n)
time = np.random.uniform(5, 60, n)
purity = np.random.uniform(0.9, 1.0, n)

conversion = (
    0.3 * (1 - np.exp(-0.01 * (temp - 300))) +
    0.2 * (1 - np.exp(-0.1 * pressure)) +
    0.15 * np.tanh(0.5 * catalyst) +
    0.1 * (1 - np.exp(-0.05 * time)) +
    0.1 * purity +
    0.05 * (temp - 350) * catalyst / 500 +
    np.random.normal(0, 0.02, n)
)
conversion = np.clip(conversion, 0, 1)

hw13_reactor = pd.DataFrame({
    'temperature': temp,
    'pressure': pressure,
    'catalyst_loading': catalyst,
    'residence_time': time,
    'feed_purity': purity,
    'conversion': conversion
})
save_csv(hw13_reactor, 'hw13_reactor_data.csv')

print("\n=== All assignment datasets generated! ===")
