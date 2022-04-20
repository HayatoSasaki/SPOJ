import matplotlib.pyplot as plt

# Human
input_ = open("Data Science\Visualization\Case Study 02 - Bioinformatics 'Comparative Genomics'\Bioinformatics - Human_18S_rRNA_gene-complete.fasta").read()
output_ = open('Comparative_Human.html', 'w')
# Bacteria
# input_ = open("Data Science\Visualization\Case Study 02 - Bioinformatics 'Comparative Genomics'\Bioinformatics - Escherichia_coli strain_U_5.41_16S_ribosomal_RNA_gene-partial sequence.fasta").read()
# output_ = open('Comparative_Bacteria.html', 'w')

count_ = {}

for i in ['A', 'T', 'C', 'G']:
    for j in ['A', 'T', 'C', 'G']:
        count_[i+j] = 0

input_ = input_.replace('\n', '')

for k in range(len(input_)-1):
    count_[input_[k]+input_[k+1]] += 1

i = 1
for k in count_:
    transp = count_[k]/max(count_.values())
    output_.write("<div style='width:100px; border:1px solid #111; color:#fff; height: 100px; float:left; background-color:rgba(0,0,0, "+str(transp)+"')>"+k+"</div>")

    if i % 4 == 0:
        output_.write("<div style='clear:both'></div>")
    i += 1

output_.close()
