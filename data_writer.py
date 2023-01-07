import pandas as pd

pd.options.display.max_rows = None

happiness_data_frame = pd.read_csv('2018.csv')

minimum_wage_data_frame = pd.read_csv('MINIMUM_WAGES.csv')

initial_combined_data_frame = pd.merge(happiness_data_frame, minimum_wage_data_frame, how='inner',
                                       left_on='Country or region', right_on='Country')
initial_combined_data_frame.drop(['GDP per capita', 'Social support', 'Healthy life expectancy',
                                  'Freedom to make life choices', 'Generosity', 'Perceptions of corruption', 'Country',
                                  '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010',
                                  '2011', '2012', '2013', '2014', '2015', '2016', '2017'], axis=1, inplace=True)

initial_combined_data_frame.drop([0, 1, 2, 3, 5, 6, 7, 8, 10, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,
                                  26, 27], axis=0, inplace=True)

initial_combined_data_frame.to_csv('happiness_via_min_wage.csv')

0, 1, 2, 3, 5, 6, 7, 8, 10, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27
food_security_data_frame = pd.read_csv('FAOSTAT_data_8-15-2021.csv')

final_combined_data_frame = pd.merge(initial_combined_data_frame, food_security_data_frame, how='inner',
                                     left_on='Country or region', right_on='Area')
final_combined_data_frame.drop(['Domain Code', 'Domain', 'Area Code (FAO)', 'Element Code', 'Element', 'Item Code',
                                'Year Code', 'Flag', 'Flag Description', 'Note'], axis=1, inplace=True)

final_combined_data_frame.to_csv('happiness_via_min_wage_and_food_security.csv')
