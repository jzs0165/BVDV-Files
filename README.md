# Insights into the secondary and tertiary structure of the Bovine Viral Diarrhea Virus Internal Ribosome Entry Site -- Supplementary data

Devadatta Gosavi1<sup>1</sup>, Iwona Wower<sup>2</sup>, Irene K. Beckmann<sup>3</sup>, Ivo L. Hofacker<sup>3,4</sup>, Jacek Wower<sup>2</sup>, Michael T. Wolfinger<sup>3,4</sup>, Joanna Sztuba-Solinska<sup>1</sup>

<sub><sup>1</sup>Department of Biological Sciences, Auburn University, 120 W. Samford Ave, Rouse Life Sciences Building, Auburn, AL 36849, United States</sub><br/>
<sub><sup>2</sup>Department of Animal and Dairy Sciences, Auburn University, 209 Upchurch Hall, Auburn, AL 36849, United States</sub><br/>
<sub><sup>3</sup>Department of Theoretical Chemistry, University of Vienna, Vienna, Austria</sub><br/>
<sub><sup>4</sup>Research Group Bioinformatics and Computational Biology, Faculty of Computer Science, University of Vienna, Vienna, Austria</sub><br/>

This repository contains additional resources that were used during preparation of the manuscript. These include custom software and data files.

## Software: SHAPE_Trimmer
A Python script for trimming sequences bound by primers and concatenation of truncated files. Specifically, this script performs
- truncation of sequences in .fastq files for target RNA zones 1-3 as required for SHAPE-MaP
- concatenation of truncatated files into a common file for complete sequence coverage

- define input/infiles files (EDIT AS NEEDED for number of zones)
- name output filename (EDIT AS NEEDED)
- hybridization site lengths for respective primers for 3 RNA zones; these correspond to the length of primers; indices match infiles
- for Zone 3 R1 delete 31 nts due to lack of PCR primer being ahead of RT plus RT read wrong for 5 nts
- trimming and merging

## Data files
The *stk* directory contains Stockholm files of structural multiples sequence nucleotide alignments that were used to
- compare published BVDV IRES RNA structures
- compute consensus structures

## Citation 
If you use data provided in this repository in your own work please link back to this site and cite the following publications - Thank you!

- **Insights into the secondary and tertiary structure of the Bovine Viral Diarrhea Virus Internal Ribosome Entry Site**  
 _Devadatta Gosavi, Iwona Wower, Irene K. Beckmann, Ivo L. Hofacker, Jacek Wower, Michael T. Wolfinger, Joanna Sztuba-Solinska_  
 bioRxiv 2021.05.13.444024 (2021) [PDF](https://www.biorxiv.org/content/10.1101/2021.05.13.444024v1.full.pdf) | [doi:10.1101/2021.05.13.444024](https://doi.org/10.1101/2021.05.13.444024)
