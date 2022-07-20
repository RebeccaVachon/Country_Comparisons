import pandas as pd
import numpy as np

comparison_df = pd.read_csv('County_Comparison.csv')
print(comparison_df.dtypes)

excel_comparison_df = pd.read_excel('County_Comparison.xlsx', sheet_name='County_Comparison')
print(excel_comparison_df.dtypes)