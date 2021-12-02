import numpy as np
import pandas as pd
import sys


if __name__ == '__main__':
    sys.path.append('c:\\testStudy')

    GWAS_file_paths = ['c:\\testStudy\\GWASResults\\GAPIT.MLM.HT.Tolerance.based.on.glucose.consumption.GWAS.Results.csv',
                  'c:\\testStudy\\GWASResults\\GAPIT.MLM.SynH.Final.OD600.GWAS.Results.csv',
                  'c:\\testStudy\\GWASResults\\GAPIT.MLM.SynH.Percent.glucose.consumed.GWAS.Results.csv',
                  'c:\\testStudy\\GWASResults\\GAPIT.MLM.HT.Tolerance.based.on.OD600.GWAS.Results.csv']

    p_thres = 0.0001


    HT_glucose_df = pd.read_csv(GWAS_file_paths[0])
    SynH_OD600_df = pd.read_csv(GWAS_file_paths[1])
    SynH_glucose_df = pd.read_csv(GWAS_file_paths[2])
    HT_OD600_df = pd.read_csv(GWAS_file_paths[3])

    # filter all dataframes by P.value, p_thres
    HT_glucose_df = HT_glucose_df[HT_glucose_df['P.value'] <= p_thres]
    SynH_OD600_df = SynH_OD600_df[SynH_OD600_df['P.value'] <= p_thres]
    SynH_glucose_df = SynH_glucose_df[SynH_glucose_df['P.value'] <= p_thres]
    HT_OD600_df = HT_OD600_df[HT_OD600_df['P.value'] <= p_thres]

    HT_glucose_df['Phenotype'] = 'HT_glucose'
    SynH_OD600_df['Phenotype'] = 'SynH_OD600'
    SynH_glucose_df['Phenotype'] = 'SynH_glucose'
    HT_OD600_df['Phenotype'] = 'HT_OD600'

    # concatenate all dataframes
    combined_df = pd.concat([HT_glucose_df, SynH_OD600_df, SynH_glucose_df, HT_OD600_df])

    combined_df = combined_df.groupby(['SNP', 'Chromosome', 'Position ']).agg(lambda x: x.tolist()).reset_index()
    print(combined_df)

    # export combined df to csv at path 'outputs/filteredGWASResults.csv'
    combined_df.to_csv('outputs/filteredGWASResults.csv', index=False)

    