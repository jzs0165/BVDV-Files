# SHAPE_Trimmer
Script trimming off sequences bound by primers and concatenating truncated files
# Functions of this script include:
# 1) truncation of sequences in .fastq files for target RNA zones 1-3 as required for SHAPE-MaP
# 2) concatenated truncatated files into a common file for complete sequence coverage

# define input/infiles files (EDIT AS NEEDED for number of zones)
# name output filename (EDIT AS NEEDED)
# hybridization site lengths for respective primers for 3 RNA zones; these correspond to the length of primers; indices match infiles
# for Zone 3 R1 delete 31 nts due to lack of PCR primer being ahead of RT plus RT read wrong for 5 nts
# trimming and merging
