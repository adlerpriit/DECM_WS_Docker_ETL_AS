import pandas as pd
import argparse

# Define command line arguments for input and output files
parser = argparse.ArgumentParser(description='Transform air quality data')
parser.add_argument('infile', type=str, help='The input file to transform')
parser.add_argument('outfile', type=str, help='The output file to write the transformed data to')
args = parser.parse_args()

# Read the input file, specifying the separator, decimal, and the column to parse as date
data = pd.read_csv(args.infile, sep=';', decimal=',', parse_dates=['Kuupäev']).sort_values(['Kuupäev']).rename(columns={'Kuupäev': 'DateTime', 'PM2.5': 'PM2p5'})

# Write the transformed data to the output file in Parquet format
data.to_parquet(args.outfile, index=False)