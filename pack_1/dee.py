import matplotlib.pyplot as plt

# Sample means and ranges
sample_means = [100.0, 100.025, 100.025, 100.05, 100.05]
sample_ranges = [0.4, 0.6, 0.4, 0.3, 0.3]

# Plot X̄ Chart
plt.figure(figsize=(12, 8))

# Plotting the X̄ chart
plt.subplot(2, 1, 1)
plt.plot(sample_means, marker='o', linestyle='-', color='blue')
plt.axhline(y=100.03, color='green', linestyle='--', label='CL (100.03)')
plt.axhline(y=100.322, color='red', linestyle='--', label='UCL (100.322)')
plt.axhline(y=99.738, color='red', linestyle='--', label='LCL (99.738)')
plt.title('X̄ Chart')
plt.xlabel('Sample')
plt.ylabel('Mean')
plt.legend()

# Plot R Chart
plt.subplot(2, 1, 2)
plt.plot(sample_ranges, marker='o', linestyle='-', color='blue')
plt.axhline(y=0.4, color='green', linestyle='--', label='CL (0.4)')
plt.axhline(y=0.913, color='red', linestyle='--', label='UCL (0.913)')
plt.axhline(y=0, color='red', linestyle='--', label='LCL (0)')
plt.title('R Chart')
plt.xlabel('Sample')
plt.ylabel('Range')
plt.legend()

plt.tight_layout()
plt.show()