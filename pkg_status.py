import datetime


class PackageStatus :
    def getPackageStatus(pkg_id, time, hash, print=True):
        # Handle the address update for Package #9 at 10:20 a.m.
        # Update the package object and GUI accordingly
        if time.hour + time.minute / 60 + time.second / 3600 < 10.33:
            changeAddress = hash.get(('9'))
            changeAddress["Deliv Address"] = "300 State St"
            changeAddress["Zip"] = "84103"
        else:
            changeAddress = hash.get(('9'))
            changeAddress["Deliv Address"] = "410 S State St"
            changeAddress["Zip"] = "84111"
        currentPkg = hash.get(str(pkg_id))
        routeStart = datetime.timedelta(hours=float(currentPkg["Route Start"]))
        routeStart = datetime.datetime.strptime(str(routeStart), "%H:%M:%S")
        delivtime = datetime.timedelta(hours=float(currentPkg["Actual Deliv Time"]))
        delivtime = datetime.datetime.strptime(str(delivtime), "%H:%M:%S")
        if routeStart.time() > time.time():
            currentPkg["Delivery Status"] = f"At The Hub as of {time.time()}"
        elif delivtime.time() < time.time():
            currentPkg["Delivery Status"] = f"Delivered at {delivtime.time()}"
        else:
            currentPkg["Delivery Status"] = f"En Route as of {time.time()}" 
        # Lookup, return, and print the key-value attributes of the current package
        # Space-Time Complexity: O(1)
        PkgID = hash.lookup(str(pkg_id), "Pkg ID")
        address = hash.lookup(str(pkg_id), "Deliv Address")
        city = hash.lookup(str(pkg_id), "City")
        zip = hash.lookup(str(pkg_id), "Zip")
        weight = hash.lookup(str(pkg_id), "Weight")
        deadline = hash.lookup(str(pkg_id), "Delivery Deadline")
        status = hash.lookup(str(pkg_id), "Delivery Status")
        res_array = []
        # Push items into the array
        res_array.append(f"STATUS OF PKG ID {PkgID} AT TIME {time.time()}")
        res_array.append(f"Route Start Time: { routeStart.time()}")
        res_array.append(f"Delivery Address: { address}")
        res_array.append(f"Delivery City: { city}")
        res_array.append(f"Delivery Zip Code: { zip}")
        res_array.append(f"Delivery Weight: { weight} KILO")
        res_array.append(f"Delivery Deadline: { deadline}")
        res_array.append(f"Delivery Status: { status}")
        res_array.append(f"Truck: { currentPkg['Truck']}")

        if print:
            for index, text in enumerate(res_array):
                print(text)

        return res_array
        


