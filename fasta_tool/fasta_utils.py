import statistics
from collections import Counter

def read_fasta(filepath):
    records = []
    header = None
    seq_chunks = []

    with open(filepath, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            if line.startswith(">"):
                if header is not None:
                    records.append((header, "".join(seq_chunks)))
                header = line[1:]
                seq_chunks = []
            else:
                seq_chunks.append(line.upper())

        if header is not None:
            records.append((header, "".join(seq_chunks)))

    return records

def count_sequences(records):
    return len(records)

def check_unique_headers(records):
    headers = [h for h, _ in records]
    return len(headers) == len(set(headers))

def find_duplicate_headers(records):
    headers = [h for h, _ in records]
    return [h for h, c in Counter(headers).items() if c > 1]

def sequence_length_stats(records):
    lengths = [len(seq) for _, seq in records]
    return {
        "min": min(lengths),
        "max": max(lengths),
        "mean": statistics.mean(lengths),
        "median": statistics.median(lengths),
    }

def gc_content(sequence):
    sequence = sequence.upper()
    g = sequence.count("G")
    c = sequence.count("C")
    atgc = sum(sequence.count(b) for b in "ATGC")
    if atgc == 0:
        return 0.0
    return (g + c) / atgc * 100

def overall_gc_content(records):
    all_seq = "".join(seq for _, seq in records)
    return gc_content(all_seq)

def gc_per_sequence(records):
    return [(header, gc_content(seq)) for header, seq in records]

def nucleotide_composition(records):
    counts = {"A": 0, "C": 0, "T": 0, "G": 0, "N": 0}
    for _, seq in records:
        for base in counts:
            counts[base] += seq.count(base)
    total = sum(counts.values())
    proportions = {b: c / total for b, c in counts.items()}
    return counts, proportions
