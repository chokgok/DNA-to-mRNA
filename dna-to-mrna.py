DNA_to_RNA = {
    "A": "U",
    "T": "A",
    "G": "C",
    "C": "G",
}

def transcribe(dna):
    mRNA = ""
    for nucleotide in dna:
        if nucleotide == " ":
            continue
        mRNA = mRNA + DNA_to_RNA[nucleotide]
    return mRNA

def codons(rna):
    mRNA_codons = ""
    for n in range(len(rna)):
        if n % 3 == 0 and n != 0:
            mRNA_codons = mRNA_codons + " "
        mRNA_codons = mRNA_codons + rna[n]
    return mRNA_codons

def main():
    print(f"mRNA sequence: {codons(transcribe(input("Enter DNA sequence: ")))}")

# GAGCTATTCCATGGA
# GAG CTA TTC CAT GGA

if __name__ == "__main__":
    main()