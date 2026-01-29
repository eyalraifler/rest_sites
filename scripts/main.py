import re
from find_sequences import *


file = open("data/orf_coding_all.fa.txt", "r")

genes ={} # dictionary to hold: key - gene name, value - sequence
name = ""
seq = ""
for line in file:
    line = line.strip("\n")
    if line[0] == ">":
        if seq != "" and name != "":
            genes[name] = seq
        name = line
        seq = "" 
    elif line != "\n" or None:
        seq += line
        
if seq != "" and name != "": # to add the last gene in the file
    genes[name] = seq

file.close()

# Now we have a dictionary with all the genes and their seq. 
# We can go over it and print all the genes that have at least one of the restriction sites.
with open("results/restriction_sites_results.txt", "w") as results_file:
    dsal_overall_count = 0
    secl_overall_count = 0
    cjul_overall_count = 0
    genes_containing_sites = 0
    
    for gene_name in genes:
        gene_seq = genes[gene_name]
        dsal_count = find_dsal(gene_seq)[1]
        dsal_overall_count += dsal_count
        
        secl_count = find_secl(gene_seq)[1]
        secl_overall_count += secl_count
        
        cjul_count = find_cjul(gene_seq)[1]
        cjul_overall_count += cjul_count
        
        secl_occurences = find_secl(gene_seq)[0]
        cjul_occurences = find_cjul(gene_seq)[0]
        dsal_occurences = find_dsal(gene_seq)[0]
        
        if dsal_count > 0 or secl_count > 0 or cjul_count > 0:
            genes_containing_sites += 1
            results_file.write(f"{gene_name}:\n")
            results_file.write(f"There are {dsal_count} Dsal sites:\n")
            for site in dsal_occurences:
                results_file.write(f"Dsal site: {site}\n")
                
            results_file.write(f"There are {secl_occurences} Secl sites:\n")
            for site in secl_occurences:
                results_file.write(f"Secl site: {site}\n")
            
            results_file.write(f"There are {cjul_occurences} Cjul sites:\n")
            for site in cjul_occurences:
                results_file.write(f"Cjul site: {site}\n")

    results_file.write(f"\nNumber of Protein with any kind of site: {genes_containing_sites}\n")
        
            



    