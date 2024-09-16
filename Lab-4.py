# Function to calculate degrees of freedom using Grubler's formula
def calculate_dof(m, N, J, joints_with_1_dof, joints_with_2_dof, joints_with_3_dof):
    # Grubler's formula for degrees of freedom
    total_dof = m * (N - J - 1) + (1 * joints_with_1_dof + 2 * joints_with_2_dof + 3 * joints_with_3_dof)
    return total_dof

# Get inputs from the user
m = int(input("Enter the number of degrees of freedom of a single body (m): "))
N = int(input("Enter the number of bodies (N): "))
J = int(input("Enter the number of joints (J): "))
joints_with_1_dof = int(input("Enter the number of joints with 1 DOF: "))
joints_with_2_dof = int(input("Enter the number of joints with 2 DOFs: "))
joints_with_3_dof = int(input("Enter the number of joints with 3 DOFs: "))

# Calculate the degrees of freedom
dof = calculate_dof(m, N, J, joints_with_1_dof, joints_with_2_dof, joints_with_3_dof)

# Output the result
print(f"The degrees of freedom of the mechanism is: {dof}")

# Verification using an example similar to the one in the problem:
# Example values:
# m = 6 (degrees of freedom in 3D space)
# N = 10 (number of bodies/links)
# J = 9 (number of joints)
# 3 revolute joints, 0 joints with 2 DOFs, and 6 spherical joints with 3 DOFs

verification_dof = calculate_dof(6, 10, 9, 3, 0, 6)
print(f"Verification with example inputs: {verification_dof} DOFs")
