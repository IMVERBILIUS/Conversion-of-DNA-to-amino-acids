# Tabel kodon RNA ke asam amino
codon_table = {
    'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L',
    'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',
    'AUU': 'I', 'AUC': 'I', 'AUA': 'I', 'AUG': 'M',
    'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V',
    'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S',
    'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
    'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
    'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
    'UAU': 'Y', 'UAC': 'Y', 'UAA': 'STOP', 'UAG': 'STOP',
    'CAU': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
    'AAU': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K',
    'GAU': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',
    'UGU': 'C', 'UGC': 'C', 'UGA': 'STOP', 'UGG': 'W',
    'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
    'AGU': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',
    'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'
}

def dna_to_rna(dna_seq):
    # Mengubah DNA menjadi RNA
    return dna_seq.replace('T', 'U')

def rna_to_protein(rna_seq):
    # Menerjemahkan RNA menjadi asam amino
    protein_seq = []
    for i in range(0, len(rna_seq), 3):
        codon = rna_seq[i:i+3]
        amino_acid = codon_table.get(codon, '')
        if amino_acid == 'STOP':
            break
        protein_seq.append(amino_acid)
    return ''.join(protein_seq)

# Meminta input dari pengguna
dna_input = input("Masukkan urutan DNA: ").upper()

# Memeriksa apakah input valid
valid_nucleotides = {'A', 'T', 'C', 'G'}
if set(dna_input).issubset(valid_nucleotides) and len(dna_input) % 3 == 0:
    rna_sequence = dna_to_rna(dna_input)
    protein_sequence = rna_to_protein(rna_sequence)
    # Menampilkan hasil
    print(f"DNA: {dna_input}")
    print(f"Urutan RNA: {rna_sequence}")
    print(f"Urutan Asam Amino: {protein_sequence}")
else:
    print("Urutan DNA tidak valid. Pastikan hanya mengandung A, T, C, G dan panjangnya kelipatan 3.")
