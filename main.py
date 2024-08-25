from Bio.Seq import Seq
from Bio import BiopythonWarning
import warnings

warnings.simplefilter('ignore', BiopythonWarning)

def dna_to_rna(dna):
    complement = {'A': 'U', 'T': 'A', 'C': 'G', 'G': 'C',
                  'a': 'u', 't': 'a', 'c': 'g', 'g': 'c'}
    rna = ''.join([complement.get(base, base) for base in dna])
    return rna

def rna_to_protein(rna):
    if len(rna) % 3 != 0:
        rna += 'N' * (3 - len(rna) % 3)
    
    rna_seq = Seq(rna)
    protein_seq = rna_seq.translate(to_stop=False)  # Abaikan kodon stop
    return str(protein_seq)

def main():
    while True:
        dna_input = input("Masukkan urutan DNA: ").strip()
        rna_seq = dna_to_rna(dna_input)
        protein_seq = rna_to_protein(rna_seq)
        
        print(f"DNA: {dna_input}")
        print(f"RNA: {rna_seq}")
        print(f"Asam Amino: {protein_seq}")

        repeat = input("Apakah Anda ingin mengulang? (ya/tidak): ").strip().lower()
        if repeat != 'ya':
            print("Terima kasih telah menggunakan program ini!")
            break

if __name__ == "__main__":
    main()
