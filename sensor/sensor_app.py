from datetime import datetime, date
from load_data import load_sensor_data
from house_info import HouseInfo
# Runner script for all modules


##############################
# Do not remove these two lines
# They are needed to validate your unittest
data = []
print("Sensor Data App")

time_fmt = '%m/%d/%y'

data = load_sensor_data()
print("Loaded records: {}".format(len(data)))


house_info = HouseInfo(data)
test_area = 1
recs = house_info.get_data_by_area('id', test_area)
print("\nHouse sensor records for area {} = {}".format(test_area, len(recs)))


test_date = datetime.strptime('5/9/20', time_fmt)
recs = house_info.get_data_by_date('id', rec_date=test_date)
print("\nHouse sensor records for date: {} = {}".format(test_date.strftime(time_fmt), len(recs)))

##############################

# Module 1 code here:

# Module 2 code here:

# Module 3 code here:

# Module 4 code here:

# Module 5 code here: