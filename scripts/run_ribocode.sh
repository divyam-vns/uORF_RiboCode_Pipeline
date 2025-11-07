#!/bin/bash
# =============================
# Run RiboCode uORF analysis
# =============================

# Input files
GTF="data/annotation.gtf"
FASTA="data/transcripts.fa"
BAM_DIR="data/bam"
OUTPUT_DIR="results"

mkdir -p $OUTPUT_DIR

# Step 1: Prepare transcriptome database
RiboCode prepare_transcriptome \
  --gtf $GTF \
  --genome $FASTA \
  --prefix $OUTPUT_DIR/transcript_db

# Step 2: Detect ORFs including uORFs
# RiboCode will output all translated ORFs
for bam in $BAM_DIR/*.bam; do
    SAMPLE=$(basename $bam .bam)
    RiboCode run \
      --bam $bam \
      --gtf $GTF \
      --genome $FASTA \
      --output $OUTPUT_DIR/${SAMPLE}_translated_ORFs.txt \
      --min-length 9 \
      --start-codons AUG,CUG,GUG,UUG
done

echo "RiboCode uORF detection complete. Results in $OUTPUT_DIR"
