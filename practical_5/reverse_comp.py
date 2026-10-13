import sys
print(sys.executable)
print(sys.path)
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
import os
filename='dna.fasta'
destination='reverse_comp.fasta'
records = list(SeqIO.parse(filename, "fasta"))       #SeqIO.parse underrstands FASTA files and grabs one sequence per iteration



rc_records= []          #list of the reverse complements. to be filled
for record in records:
    #loops through each entry in the fasta file and prints its name and the length of the sequence
    print(record.id)
    print("length:", len(record))

    #reverse complement creates a....reverse complement to the sequence. This creates 'record'_rc for each record

    rc= record.reverse_complement(id=record.id + "_rc", descriptions="reverse complement to", record)
    #adds each rc_record to the list
    rc_records.append(rc)
SeqIO.write(rc_records, "DNA_rc.fasta", "fasta") #SeqIO writes the list to a file. Syntax: Content, filename, format

    #seq.count() gives you the count in string.