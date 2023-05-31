from Bio import SeqIO

def filter_common_sequences(file1, file2, output_file):
    sequences1 = set()
    with open(file1, "r") as handle: #reads sequences from the FASTA file of the training set
        for record in SeqIO.parse(handle, "fasta"):
            sequences1.add(str(record.seq))

    common_sequences = []
    with open(file2, "r") as handle: #reads sequences from the FASTA file of the positive set
        for record in SeqIO.parse(handle, "fasta"):
            sequence = str(record.seq)
            if sequence not in sequences1:
                common_sequences.append(record)

    with open(output_file, "w") as handle: #writes the common sequences to the output file
        SeqIO.write(common_sequences, handle, "fasta")

file1 = "training_to_remove.fasta" #file with training seqs
file2 = "../kunitz_all.fasta" #unfiltered file with positive seqs
output_file = "kunitz_all_clean.fasta"

filter_common_sequences(file1, file2, output_file)
