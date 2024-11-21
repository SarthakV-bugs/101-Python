from Bio.Seq import Seq
from Bio import SeqIO
import re

def count_pattern_in_fasta(file_path, pattern):
    for record in SeqIO.parse(file_path, "fasta"):
        sequence = str(record.seq)
        count = len(re.findall(pattern, sequence))
        print(f"Sequence ID: {record.id}, Pattern Count: {count}")

def main():
    fasta_file = "example.fasta"
    pattern = r"CGA"
    count_pattern_in_fasta(fasta_file, pattern)

if __name__ == "__main__":
    main()