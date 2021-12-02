import pandas as pd
import numpy as np

if __name__ == '__main__':
    GWAS_df = pd.read_csv('outputs/GWAS_with_SNP_info.csv')

    info_SNPs = GWAS_df['SNP_INFO']
    info_SNPs = [info.split('|') for info in info_SNPs]
    genes_SNPs = [info[3] for info in info_SNPs]
    type_SNPs = [info[1] for info in info_SNPs]
    impact_SNPs = [info[2] for info in info_SNPs]

    GWAS_df['Gene'] = genes_SNPs
    GWAS_df['Type'] = type_SNPs
    GWAS_df['Impact'] = impact_SNPs

    # drop the SNP_INFO column
    GWAS_df.drop(columns=['SNP_INFO'], inplace=True)

    GWAS_df.to_csv('outputs/final_GWAS.csv', index=False)