gene_metadata=("ATGCGCAT","insulin_gene",1322.0,"chromosome_11")
print("1.Core biological metadata unclocked:",gene_metadata)

print("2.Extracted DNA sequence base:" ,gene_metadata[0] )
print("3.Target Gene classification:" ,gene_metadata[1])
print("4.chromosome mapping location:" ,gene_metadata[-1]) 
total_attributes=len(gene_metadata)
print("Total sequence metrics tracked:" ,total_attributes)