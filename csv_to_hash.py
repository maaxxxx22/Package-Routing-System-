import csv
from hashmap import HashMap

# Read PackagesForHash CSV data into HashMap
# Space-time complexity: O(n)
with open("PackagesData.csv") as csvfile:
    CSVPkgData = csv.DictReader(csvfile, ("Pkg ID","Deliv Address", "City", "State", "Zip", "Delivery Deadline", "Weight", "Note"))
    # Create new empty instance of the HashMap class and Add each row of csv file to it. Actual Delivery Time attribute is also added to the HashMap
    PkgData = HashMap()
    for row in CSVPkgData:
        row['Delivery Status'] = ''
        row['Actual Deliv Time'] = ''
        PkgData.insert(row['Pkg ID'], row)
    def get_map():
        return PkgData

 # Read DistancesForHash CSV data into a dictionary
 # Space-Time Complexity: O(n)
with open("DistancesData.csv") as csvfile:
    CSVDistData = csv.DictReader(csvfile)
    DistData = {}
    for row in CSVDistData:
        DistData[row["Address"]] = row
    def get_dist_data():
        return DistData