# Codon table (for translation from mRNA to amino acids)
codon_table = {
    'UUU': 'Phe', 'UUC': 'Phe', 'UUA': 'Leu', 'UUG': 'Leu',
    'UCU': 'Ser', 'UCC': 'Ser', 'UCA': 'Ser', 'UCG': 'Ser',
    'UAU': 'Tyr', 'UAC': 'Tyr', 'UGU': 'Cys', 'UGC': 'Cys',
    'UGG': 'Trp', 'CUU': 'Leu', 'CUC': 'Leu', 'CUA': 'Leu',
    'CUG': 'Leu', 'AUU': 'Ile', 'AUC': 'Ile', 'AUA': 'Ile',
    'AUG': 'Met', 'GUU': 'Val', 'GUC': 'Val', 'GUA': 'Val',
    'GUG': 'Val', 'GCU': 'Ala', 'GCC': 'Ala', 'GCA': 'Ala',
    'GCG': 'Ala', 'GAU': 'Asp', 'GAC': 'Asp', 'GAA': 'Glu',
    'GAG': 'Glu', 'GGU': 'Gly', 'GGC': 'Gly', 'GGA': 'Gly',
    'GGG': 'Gly', 'AAU': 'Asn', 'AAC': 'Asn', 'AAA': 'Lys',
    'AAG': 'Lys', 'CAU': 'His', 'CAC': 'His', 'CAA': 'Gln',
    'CAG': 'Gln', 'CGU': 'Arg', 'CGC': 'Arg', 'CGA': 'Arg',
    'CGG': 'Arg'
}

# Function to get complement strand and mRNA sequence
def complement_dna(seq):
    complement = {"A":"T", "T":"A", "C":"G", "G":"C"}
    comp_dna = ''.join([complement[base] for base in seq])
    
    # Transcribe to mRNA (replace 'T' with 'U')
    mrna = comp_dna.replace("T", "U")
    
    return comp_dna, mrna

# Function to translate mRNA to amino acids
def AminoAcid(seq):
    aminoacid = []
    for i in range(0, len(seq), 3):
        codon = mrna[i:i+3]
        aminoacid.append(codon_table.get(codon))
        
    return aminoacid
    
input_dna = "TTACGA"
comp_dna, mrna = complement_dna(input_dna)
aminoacid = AminoAcid(mrna)

print("Input DNA = " + input_dna + "\n")
print("Complement = " + comp_dna)
print("mRNA = " + mrna)
print("Aminoacid = " + (' - '.join(aminoacid)))