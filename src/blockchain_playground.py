from scipy.optimize import fsolve

def original_function(xi, gam):
    return ((gam * xi * (1 - xi)) % 1) / ((gam / 4) % 1)

def inverse_function(y, gam):
    equation = lambda xi: original_function(xi, gam) - y
    xi_guess = 0.5  # Initial guess for root-finding algorithm
    xi_solution = fsolve(equation, xi_guess)
    return xi_solution[0]  # Return the first solution

# Test the functions
gam_value = 2  # You can choose any value for 'gam'
xi_values = [0.1, 0.2, 0.3, 0.4, 0.5]  # Example values for xi
y_values = [original_function(xi, gam_value) for xi in xi_values]
xi_inverse_values = [inverse_function(y, gam_value) for y in y_values]

# Print results
print("Original xi values:", xi_values)
print("Original y values:", y_values)
print("Inverse xi values:", xi_inverse_values)
