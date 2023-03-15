# 70gff.py

# Write a program that converts genes in gff into JSON
# Use the E. coli genome gff
# Your code should mimic the output below

import json
import argparse
import gzip
import re

parser = argparse.ArgumentParser(description='Convert genes from gff to JSON')
parser.add_argument('file', type=str, metavar='<path>, help='gff file')
arg = parser.parse_args()

genes = []

with gzip.open(arg.file, 'rt') as fp:
	for line in fp.readlines():
		if re.search('RefSeq\s+gene', line):
			gene = re.search('(gene=)(\w+)', line).group(2) # this and the lines below are extracting important information
			span = re.search('(gene\s+)(\d+)(\s+)(\d+)', line)
			strand = re.search('[+-]', line).group()
			gene_dict = {}
# assign values to the dictionary called gene_dict
			gene_dict["gene"] = f"{gene}"
			gene_dict["beginning"] = f"{span.group(2)}"
			gene_dict["end"] = f"{span.group(4)}"
			gene_dict["strand"] = f"{strand}"
			
			genes.append(gene_dict)
#prints results		
print(json.dumps(genes, indent = 4))
"""
python3 70gff.py ~/DATA/E.coli/GCF_000005845.2_ASM584v2_genomic.gff.gz
[
    {
        "gene": "thrL",
        "beg": 190,
        "end": 255,
        "strand": "+"
    },
    {
        "gene": "thrA",
        "beg": 337,
        "end": 2799,
        "strand": "+"
    },
...
"""
