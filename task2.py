# Dictionary for amino acids to codon mappings
amino_acid_to_codon = {
    'W': ['UGG'],           # Tryptophan (W) has only one codon
    'Y': ['UAC', 'UAU'],    # Tyrosine (Y) has two codons
}

# Generate all possible mRNA sequences for the amino acid sequence
def generate_mRNA(amino_acid_seq):
    possible_mrna = []
    
    # Recursive function to generate all mRNA combinations
    def combine(codon_seq, amino_seq):
        if len(amino_seq) == 0:
            possible_mrna.append(codon_seq)
            return
        current_amino_acid = amino_seq[0]
        remaining_amino_acids = amino_seq[1:]
        for codon in amino_acid_to_codon[current_amino_acid]:
            combine(codon_seq + codon, remaining_amino_acids)
    
    combine("", list(amino_acid_seq))
    
    return possible_mrna
    
# Count occurrences of each codon in a given mRNA sequence
def count_codons(mrna_sequence):
    codon_count = {}
    codon_list = [mrna_sequence[i:i+3] for i in range(0, len(mrna_sequence), 3)]
    for codon in codon_list:
        codon_count[codon] = codon_count.get(codon, 0) + 1
    return codon_count

input_aminoacid = "WYW"

# Call the function and get all possible mRNA sequences
mRNA_sequences = generate_mRNA(input_aminoacid)

# Display the output as required
print("Input Aminoacid = " + input_aminoacid + "\n")

for mRNA in mRNA_sequences:
    print("mRNA = " + mRNA)
    codon_count = count_codons(mRNA)
    for codon, count in codon_count.items():
        print(f"{codon} = {count}")
    print()
