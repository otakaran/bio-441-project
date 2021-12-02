import pandas as pd
import numpy as np
import io
import os
import sys

def read_vcf(path):
    with open(path, 'r') as f:
        lines = [l for l in f if not l.startswith('##')]
    return pd.read_csv(
        io.StringIO(''.join(lines)),
        dtype={'#CHROM': str, 'POS': int, 'ID': str, 'REF': str, 'ALT': str,
               'QUAL': str, 'FILTER': str, 'INFO': str},
        sep='\t',
        usecols=range(9)
    ).rename(columns={'#CHROM': 'CHROM'})

if __name__ == '__main__':
    pd.set_option('display.max_columns', None)

    sys.path.append('c:\\testStudy')
    vcf_fp = 'c:\\testStudy\\Dataset1_Complete_MS.vcf'

    GWAS_results_df = pd.read_csv('outputs/filteredGWASResults.csv')
    vcf_df = read_vcf(vcf_fp)

    snp_info = []
    # for every row in GWAS results dataframe, find the row with the chromosome and position in vcf df
    for index, row in GWAS_results_df.iterrows():
        chrom = row['Chromosome']
        pos = row['Position ']
        vcf_row = vcf_df[(vcf_df['CHROM'] == chrom) & (vcf_df['POS'] == pos)]
        if not vcf_row.empty:
            snp_info.append(vcf_row.iloc[0])
        else:
            snp_info.append('NA')

    snp_info = [row['INFO'] for row in snp_info]
    GWAS_results_df['SNP_INFO'] = snp_info

    # output GWAS_results_df to a csv file called outputs/geneAssociation.csv
    GWAS_results_df.to_csv('outputs/GWAS_with_SNP_info.csv', index=False)