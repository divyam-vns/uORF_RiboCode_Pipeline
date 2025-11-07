#!/usr/bin/env python3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import glob
import os

RESULTS_DIR = "results"
OUTPUT_PLOTS = os.path.join(RESULTS_DIR, "plots")
os.makedirs(OUTPUT_PLOTS, exist_ok=True)

# Collect all translated ORFs from RiboCode outputs
orf_files = glob.glob(os.path.join(RESULTS_DIR, "*_translated_ORFs.txt"))

for f in orf_files:
    df = pd.read_csv(f, sep="\t")
    sample_name = os.path.basename(f).replace("_translated_ORFs.txt","")
    
    # Filter uORFs: start < CDS start (assume 'uORF' column exists or use Start coordinate)
    uorfs = df[df['uORF'] == True] if 'uORF' in df.columns else df[df['Start'] < df['CDS_Start']]
    
    # Plot histogram of uORF lengths
    plt.figure(figsize=(8,5))
    sns.histplot(uorfs['Length'], bins=30, kde=False, color='skyblue')
    plt.title(f"uORF length distribution: {sample_name}")
    plt.xlabel("Length (nt)")
    plt.ylabel("Count")
    plt.savefig(os.path.join(OUTPUT_PLOTS, f"{sample_name}_uORF_length.png"))
    plt.close()
    
    # Plot histogram of Ribo-seq counts (translation)
    plt.figure(figsize=(8,5))
    sns.histplot(uorfs['Ribo_Counts'], bins=30, log_scale=(False,True), color='salmon')
    plt.title(f"uORF ribosome counts: {sample_name}")
    plt.xlabel("Ribo-seq counts")
    plt.ylabel("Frequency (log scale)")
    plt.savefig(os.path.join(OUTPUT_PLOTS, f"{sample_name}_uORF_counts.png"))
    plt.close()

print("uORF plots saved in:", OUTPUT_PLOTS)
