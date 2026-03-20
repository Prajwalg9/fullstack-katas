import pandas as pd

path =r'C:\Users\prajw\.cache\kagglehub\datasets\muhammadahmaddaar\delivery-logistics-dataset-india-multi-partner\versions\1\Delivery_Logistics.csv'


df=pd.read_csv(path)

#Head give 5 lines of any file by default -df.head()
#Head can give n number of lines of file -df.head(n)
print("First 5 lines",df.head())
print("First 3 lines",df.head(3))

#Tail give 5 lines of any file by default -df.tail()
#Tail can give n number of lines of file -df.tail(n)
print("last 5 lines",df.tail())
print("last 3 lines",df.tail(3))


#df.info() returns everything about an dataset
print(df.info())

# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 25000 entries, 0 to 24999
# Data columns (total 15 columns):
#  #   Column               Non-Null Count  Dtype
# ---  ------               --------------  -----
#  0   delivery_id          25000 non-null  float64
#  1   delivery_partner     25000 non-null  object
#  2   package_type         25000 non-null  object
#  3   vehicle_type         25000 non-null  object
#  4   delivery_mode        25000 non-null  object
#  5   region               25000 non-null  object
#  6   weather_condition    25000 non-null  object
#  7   distance_km          25000 non-null  float64
#  8   package_weight_kg    25000 non-null  float64
#  9   delivery_time_hours  25000 non-null  object
#  10  expected_time_hours  25000 non-null  object
#  11  delayed              25000 non-null  object
#  12  delivery_status      25000 non-null  object
#  13  delivery_rating      25000 non-null  int64
#  14  delivery_cost        25000 non-null  float64
# dtypes: float64(4), int64(1), object(10)
# memory usage: 2.9+ MB
# None



#describes following of dataset
print(df.describe())

#         delivery_id   distance_km  ...  delivery_rating  delivery_cost
# count  25000.000000  25000.000000  ...     25000.000000   25000.000000
# mean   12500.500000    150.390436  ...         3.666000     864.944579
# std     7212.732314     86.409745  ...         1.149964     435.712593
# min      250.990000      3.600000  ...         1.000000      95.667400
# 25%     6250.750000     75.900000  ...         3.000000     490.800000
# 50%    12500.500000    151.000000  ...         4.000000     867.535000
# 75%    18750.250000    224.900000  ...         5.000000    1237.910000
# max    24750.010000    297.100000  ...         5.000000    1632.720600