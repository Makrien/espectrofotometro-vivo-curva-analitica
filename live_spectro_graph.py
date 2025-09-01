import matplotlib.pyplot as plt
import numpy as np

# Sample data (concentration is x in mg/L and inversed_path is y in cm⁻¹)
concentration = np.array([25, 20, 15, 10, 5])
heights = np.array([1.3, 1.8, 2.3, 3.3, 7.7])
inversed_path = 1 / heights

# Considering y = mx + b, m being the slope and b the intercept
# This function returns m and b
slope, intercept = np.polyfit(concentration, inversed_path, deg=1)

# Estimate y-values and their error
y_est = slope * concentration + intercept
y_err = concentration.std() * np.sqrt(1/len(concentration) + (concentration - concentration.mean())**2 / np.sum((concentration - concentration.mean())**2))

# Calcutate the correlation coefficient r
# numpy.corrcoef return a matrix, therefore the index after the function
corr = np.corrcoef(inversed_path, y_est)[0,1]

# Calculate the coefficient of determination r²
r_squared = corr**2

# Strings for adding linear equation and coefficients of determination r² and correlation r
equation_txt = f"Equação da reta: 1/b = {slope:.4f}c"
corr_txt = f"Coeficiente de correlação r = {corr}"
r_squared_txt = f"Coeficiente de determinação r² = {r_squared}"

# Comparative graphic
plt.figure(figsize=(12, 8))

plt.plot(concentration, y_est, linestyle='-', marker='')
plt.plot(concentration, inversed_path, label=f"Tubo 1 = 25,00 mg/L\nTubo 2 = 20,00 mg/L\nTubo 3 = 15,00 mg/L\nTubo 4 = 10,00 mg/L\nTubo 5 = 5,000 mg/L", linestyle='', marker='o')

plt.title('Concentração das amostras em função do inverso do caminho óptico', fontsize=14)
plt.xlabel('c (em mol/L)', fontsize=12)
plt.ylabel('1/b (em cm⁻¹)', fontsize=12)
plt.legend(title="Concentrações", fontsize=10)
plt.text(5, 0.57, equation_txt, size=10)
plt.text(5, 0.54, corr_txt, size=10)
plt.text(5, 0.51, r_squared_txt, size=10)
plt.grid(alpha=0.5)
plt.tight_layout()

# Save graphic
plt.savefig("live_spectro_graph.png")

# Show graphic
plt.show()