# uORF_RiboCode_Pipeline

## Overview
This pipeline detects and analyzes **translated upstream open reading frames (uORFs)** from Ribo-seq data using **RiboCode**.  
It outputs tables of translated ORFs and generates basic visualizations.

## 
## Installation
```bash
conda env create -f environment.yml
conda activate ribocode_env

## Usage

Step 1: Run uORF detection
bash scripts/run_ribocode.sh

Step 2: Visualize uORFs
python scripts/visualize_uORFs.py

Output

results/*_translated_ORFs.txt → list of translated ORFs, including uORFs
results/plots/ → histogram plots of uORF lengths and Ribo-seq counts
