# Functions of this script include:
# 1) truncation of sequences in .fastq files for PAN RNA zones 1-3 as required for SHAPE-MaP
# 2) merging truncatated files into a common file for complete sequence coverage

# input files (EDIT AS NEEDED)

infiles = [\
'Z1minusR1.fastq',\
'Z1minusR2.fastq',\
'Z2minusR1.fastq',\
'Z2minusR2.fastq',\
'Z3minusR1.fastq',\
'Z3minusR2.fastq']

# output filename (EDIT AS NEEDED)
outfile = 'PANallminus.fastq'


# hybridization site lengths for respective primers for 3 PAN zones; these correspond to the length of primers; indices match infiles
PHSLen = [\
20,\
20,\
18,\
19,\
31,\
18]

# for Z3R1 delete 31 nts due to lack of PCR primer being ahead of RT plus RT read wrong for 5 nts


# trimming and merging
for i in range (0,6):
	output = open(outfile, 'a')
	infile = open(infiles[i], 'r')

	cntr = 0
	seq_trunk = ''
	q_trunk = ''

	# read input file (.fastq) line by line
	for line in infile:
		cntr += 1
		# first line in .fastq data quartet contains sequence header
		if cntr == 1:
			seq_header = line
		elif cntr == 2:
			start_index = 5 + PHSLen[i]
			seq_len = len(line)
			if start_index < len(line):
				seq_trunk = line[start_index:len(line)]
			else:
				seq_trunk = ''
		elif cntr == 3:
			continue
		elif cntr == 4:
			if seq_trunk != '':
				q_trunk = line[start_index:len(line)]
				output.write(seq_header)
				output.write(seq_trunk)
				output.write("+\n")
				output.write(q_trunk)
			seq_trunk = ''
			q_trunk = ''
			cntr = 0
	
	infile.close()	
	output.close()
