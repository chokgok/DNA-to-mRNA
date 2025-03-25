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
    return ' '.join(rna[i:i+3] for i in range(0, len(rna), 3))

def main():
    print(f"mRNA sequence: {codons(transcribe(input("Enter DNA sequence: ")))}")

if __name__ == "__main__":
    main()