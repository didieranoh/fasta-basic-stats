#!/usr/bin/env python3
import argparse
import os
from .fasta_fxns import (
    read_fasta,
    count_sequences,
    check_unique_headers,
    find_duplicate_headers,
    sequence_length_stats,
    gc_content,
    overall_gc_content,
    gc_per_sequence,
    nucleotide_composition,
)

def save_report_txt(filename, report_text):
    with open(filename, "w") as f:
        f.write(report_text)
    print(f"\nFull report saved as TXT: {filename}")

def main():
    parser = argparse.ArgumentParser(description="FASTA File Report")
    parser.add_argument("-i", "--input", required=True, help="Input FASTA file")
    parser.add_argument("-o", "--output", default=None, help="Custom base name for report files (optional)")
    args = parser.parse_args()

    records = read_fasta(args.input)
    
    input_path = os.path.abspath(args.input)
    input_dir = os.path.dirname(input_path)
    base_name_only = args.output or os.path.basename(input_path).rsplit(".", 1)[0]
    base_name = os.path.join(input_dir, base_name_only)

    report_lines = []

    report_lines.append(f"=== FASTA Report for {args.input} ===\n")

    total_sequences = count_sequences(records)
    report_lines.append(f"Total sequences: {total_sequences}")

    unique = check_unique_headers(records)
    report_lines.append(f"Headers unique: {unique}")
    duplicates = []
    if not unique:
        duplicates = find_duplicate_headers(records)
        report_lines.append(f"Duplicate headers ({len(duplicates)}): {duplicates}")

    stats = sequence_length_stats(records)
    report_lines.append("\nSequence Length Statistics:")
    for k, v in stats.items():
        report_lines.append(f"  {k}: {v}")

    gc_overall = overall_gc_content(records)
    report_lines.append(f"\nOverall GC content: {gc_overall:.2f}%")

    report_lines.append("\nGC content per sequence:")
    for h, gc in gc_per_sequence(records):
        report_lines.append(f"  {h}: {gc:.2f}%")

    counts, proportions = nucleotide_composition(records)
    report_lines.append("\nNucleotide Composition:")
    report_lines.append("Counts:")
    for b, c in counts.items():
        report_lines.append(f"  {b}: {c}")
    report_lines.append("Proportions:")
    for b, p in proportions.items():
        report_lines.append(f"  {b}: {p:.2f}")

    report_lines.append("\n=== End of Report ===\n")

    report_text = "\n".join(report_lines)

    print(report_text)

    save_report_txt(f"{base_name}_full_report.txt", report_text)

if __name__ == "__main__":
    main()
