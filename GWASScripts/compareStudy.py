import pandas as pd
import sys

if __name__ == '__main__':
    sys.path.append('c:\\testStudy')

    our_results = pd.read_csv('outputs/final_GWAS.csv')
    study_results = pd.read_csv('c:\\testStudy\\study_results.txt', sep='\t', header=None)
    study_results.columns = ['Phenotype', 'Chrom:Pos', 'Type', 'Gene', 'Action', 'P-value']

    # remove * / and space from the gene names
    study_results['Gene'] = study_results['Gene'].str.replace('*', '')
    study_results['Gene'] = study_results['Gene'].str.replace('/', '')
    study_results['Gene'] = study_results['Gene'].str.replace(' ', '')

    our_results_genes = our_results['Gene'].unique()
    study_results_genes = study_results['Gene'].unique()

    # get the intersection of the two sets
    common_genes = set(our_results_genes).intersection(set(study_results_genes))

    print(common_genes)
    print(f'Overlap Perc. with Respect to our Study: {len(common_genes) / len(our_results_genes) * 100}%')
    print(f'Overlap Perc. with Respect to their Study: {len(common_genes) / len(study_results_genes) * 100}%')
    print(f'Our Gene Discoveries: {our_results_genes}')

    gene_snps = []
    phenotype_snps = []
    for gene in our_results_genes:
        new_df = our_results[our_results['Gene'] == gene]
        snps = new_df['SNP'].values
        phen_types = new_df['Phenotype'].values
        phenotype_snps.append(phen_types)
        gene_snps.append(snps)


    genes_df = pd.DataFrame(our_results_genes, columns=['Gene'])
    genes_df['SNPs'] = gene_snps
    genes_df['Phenotypes'] = phenotype_snps
    print(genes_df)

    # output genes_df to csv file titled 'output/out_genes.csv'
    genes_df.to_csv('outputs/our_genes.csv', index=False)
    
