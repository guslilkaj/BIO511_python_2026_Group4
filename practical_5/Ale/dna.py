from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq

''' LOAD AND REPORT '''

# 1 Read all records from dna.fasta
records = list(SeqIO.parse("dna.fasta", "fasta"))

# 2 For each record, print the record ID and the sequence length
for rec in records:
    print(rec.id, len(rec))
    # 3 Also print the first 10 bases of the sequence.
    bases = str(rec.seq)
    print(bases[:10])

'''REVERSE COMPLEMENTS'''

# 1 For each original record, create the reverse complement of its sequence.
# 2 Make a new SeqRecord for the reverse complement. (reverse_complement makes a new record automatically)
# 3 Set the new ID to <oldid>_rc and the description to reverse complement of <oldid>.
reverse_records = []
for rec in records:
    reverse_rec = rec.reverse_complement(
        id=rec.id + "_rc",
        description="reverse complement of " + rec.id
    )
    print(f"Reverse complement of {rec.id}: {reverse_rec.seq}")
    reverse_records.append(reverse_rec)
# 4 Write all reverse-complement records to a file named dna_rc.fasta.
SeqIO.write(reverse_records, "dna_rc.fasta", "fasta")

'''GC% ANNOTATION'''
# 1 For each original record, calculate the GC% as 100 * (count of 'G' + count of 'C') / length.
# 2 Round to 1 decimal place.

gc_records = []
for rec in records:
    sequence = str(rec.seq)
    g_count = sequence.count("G")
    c_count = sequence.count("C")

    gc_percent = round(100 * (g_count + c_count) / len(sequence), 1)

    # 3 Create a copy of the record with GC% in the description
    new_rec = SeqRecord(
        rec.seq,
        id=rec.id,
        description=rec.description + f" GC={gc_percent}%"
    )
    gc_records.append(new_rec)

# 4 Write these annotated records to dna_with_gc.fasta.
SeqIO.write(gc_records, "dna_with_gc.fasta", "fasta")

''' TRANSLATION '''

# 1 Translate each DNA sequence and print the first 10 amino acids.
# 2 Read dna_rc.fasta back in and confirm that the IDs and descriptions look correct.
for rec in records:
    translated = rec.translate()
    print(translated.seq[:10])