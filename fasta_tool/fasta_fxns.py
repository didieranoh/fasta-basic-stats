#!/usr/bin/env python3
import statistics
from collections import Counter

def read_fasta_stream(filepath):
    """Generator to read sequences one by one from a FASTA file."""
    header, seq = None, []
    with open(filepath, "r") as f:
        for line in f:
            line = line.rstrip()
            if line.startswith(">"):
                if header:
                    yield header, "".join(seq)
                header = line[1:]
                seq = []
            else:
                seq.append(line)
        if header:
            yield header, "".join(seq)

def count_sequences(filepath):
    count = 0
    for _ in read_fasta_stream(filepath):
        count += 1
    return count

def check_unique_headers(filepath):
    seen = set()
    for header, _ in read_fasta_stream(filepath):
        if header in seen:
            return False
        seen.add(header)
    return True

def find_duplicate_headers(filepath):
    seen = set()
    duplicates = []
    for header, _ in read_fasta_stream(filepath):
        if header in seen:
            duplicates.append(header)
        else:
            seen.add(header)
    return duplicates

def sequence_length_stats(filepath):
    min_len = float("inf")
    max_len = 0
    total_len = 0
    count = 0
    for _, seq in read_fasta_stream(filepath):
        l = len(seq)
        min_len = min(min_len, l)
        max_len = max(max_len, l)
        total_len += l
        count += 1
    mean_len = total_len / count if count else 0
    return {"min": min_len, "max": max_len, "mean": mean_len, "count": count}

def overall_gc_content(filepath):
    total_gc = 0
    total_len = 0
    for _, seq in read_fasta_stream(filepath):
        total_gc += seq.count("G") + seq.count("C")
        total_len += len(seq)
    return (total_gc / total_len * 100) if total_len else 0

def gc_per_sequence(filepath):
    for header, seq in read_fasta_stream(filepath):
        gc = (seq.count("G") + seq.count("C")) / len(seq) * 100 if seq else 0
        yield header, gc

def nucleotide_composition(filepath):
    counts = Counter()
    total_len = 0
    for _, seq in read_fasta_stream(filepath):
        counts.update(seq)
        total_len += len(seq)
    proportions = {base: counts[base] / total_len if total_len else 0 for base in "ACGT"}
    return dict(counts), proportions