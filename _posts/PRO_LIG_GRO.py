# Read the two provided .gro files and process them as described
tar_e3l_path = "./TAR_E3L_processed.gro"
poc_gmx_path = "./POC_GMX.gro"
output_path = "./complex.gro"

# Read TAR_E3L_processed.gro
with open(tar_e3l_path, 'r') as file:
    tar_e3l_lines = file.readlines()

# Read POC_GMX.gro
with open(poc_gmx_path, 'r') as file:
    poc_gmx_lines = file.readlines()

# Extract the atom counts from the second lines
tar_e3l_atom_count = int(tar_e3l_lines[1].strip())
poc_gmx_atom_count = int(poc_gmx_lines[1].strip())

# Calculate the new total atom count
new_total_atom_count = tar_e3l_atom_count + poc_gmx_atom_count

# Create the merged content
merged_lines = []
merged_lines.append(tar_e3l_lines[0])  # First line of TAR_E3L_processed.gro (title)
merged_lines.append(f"{new_total_atom_count}\n")  # New total atom count

# Add the body of TAR_E3L_processed.gro (excluding the first 2 lines and the last line)
merged_lines.extend(tar_e3l_lines[2:-1])

# Add the body of POC_GMX.gro (excluding the first, second, and last lines)
merged_lines.extend(poc_gmx_lines[2:-1])

# Add the last line of TAR_E3L_processed.gro (box dimensions)
merged_lines.append(tar_e3l_lines[-1])

# Write the merged content to the output file
with open(output_path, 'w') as file:
    file.writelines(merged_lines)

output_path

