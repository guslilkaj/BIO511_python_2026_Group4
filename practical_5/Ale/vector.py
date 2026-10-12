import numpy as np

genes = ["geneA", "geneB", "geneC", "geneD", "geneE"]
control = [120, 340, 15, 800, 60]
treated = [240, 340, 60, 200, 30]

print(f"Genes: {genes}")
# 1 Calculate control + treated and print the result. Is it what you expected?
total = control + treated # they're considered two lists
print(f"Lists sum = {total}")

# 2 Import NumPy with import numpy as np and turn both lists into NumPy arrays with np.array().
# Add the two arrays together and compare the result with step 1.
total = np.array(control) + np.array(treated)
print(f"Arrays sum = {total}")

# 3 The fold change of a gene is its value in the treated sample divided by its value in the control sample.
# Calculate the fold change of all five genes in one line of code.
fold_change =  np.array(treated) / np.array(control)
print(f"Fold change: {fold_change}")

# 4 Use np.log2() to calculate the log2 fold change of all genes.
# Which genes went up in the treated sample, which went down, and which stayed the same?
log2 = np.log2(fold_change)
print(f"Log2 fold change: {log2}")
# if log2 > 0 the gene went up in the treated sample
# if log2 < 0 the gene went down
# if log2 = 0 stayed the same

''' 5 The two samples did not get the same total number of reads.
Use np.sum() to divide each array by its own total, so that the values in each array add up to 1.
Calculate the log2 fold change again from the normalised arrays.
Do you come to the same conclusions as in step 4?'''

# Normalise each array so its values add up to 1
control_norm = np.array(control) / np.sum(control)
treated_norm = np.array(treated) / np.sum(treated)

print(f"Normalised control: {control_norm}")
print(f"Normalised treated: {treated_norm}")

# Calculate fold change using the normalised arrays
fold_change_norm = treated_norm / control_norm
# Calculate log2 fold change
log2_norm = np.log2(fold_change_norm)
print(f"Normalised log2 fold change: {log2_norm}")
