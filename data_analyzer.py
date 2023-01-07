import pandas as pd

pd.options.display.max_rows = None

happiness_data_frame = pd.read_csv('2018.csv')

minimum_wage_data_frame = pd.read_csv('MINIMUM_WAGES.csv')

combined_data_frame = pd.merge(happiness_data_frame, minimum_wage_data_frame, how='inner', left_on='Country or region',
                               right_on='Country')
combined_data_frame.drop(['GDP per capita', 'Social support', 'Healthy life expectancy',
                          'Freedom to make life choices', 'Generosity', 'Perceptions of corruption', 'Country', '2001',
                          '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012',
                          '2013', '2014', '2015', '2016', '2017'], axis=1, inplace=True)

print(combined_data_frame)
