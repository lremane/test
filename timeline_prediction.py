import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

move = pd.read_csv('MOVE.csv')
wip = pd.read_csv('WIP.csv')
rqt = pd.read_csv('RQT.csv')
rqt = rqt.drop('LOT_ID', axis=1)
avail_lost = pd.read_csv('AVAIL+LOST.csv')
move_spec = pd.read_csv('move_spec.csv')

df = move.merge(wip, on=['DD', 'STAGE'])
df = df.merge(rqt, on=['DD', 'STAGE'])
df = df.merge(avail_lost, on='DD')
df = df.merge(move_spec, on='STAGE')

wip_sum = df.groupby('DD')['WIP'].sum().reset_index()
wip_sum = wip_sum.rename(columns={'WIP': 'WIP_SUM'})
df = df.merge(wip_sum, on='DD')

pd.options.display.max_columns = None
print(df.head())

numeric_df = df.select_dtypes(include='number')
correlation_matrix = numeric_df.corr()

# heatmap
# plt.figure(figsize=(10, 8))
# sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
# plt.title('Correlation Matrix Heatmap')
# plt.savefig('correlation_matrix_heatmap.png', dpi=300, bbox_inches='tight')
# plt.show()

# correlation
col1 = ''
col2 = ''

# Plot the scatter plot with a regression line
plt.figure(figsize=(10, 6))
sns.regplot(x=df[col1], y=df[col2], scatter_kws={"s": 10})
plt.title(f'Scatter Plot of {col1} vs {col2} with Regression Line')
plt.xlabel(col1)
plt.ylabel(col2)
plt.savefig(f'scatter_plot_{col1}_vs_{col2}_regression.png', dpi=300, bbox_inches='tight')
plt.show()

