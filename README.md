**WGUPS Package Tracker**

**Description:** The WGUPS Package Tracker is a Python-based application that facilitates the efficient management and tracking of package deliveries for the Western Governors University Parcel Service (WGUPS). The application uses Tkinter, a standard Python GUI library, to provide a user-friendly interface for querying package statuses, tracking truck routes, and calculating delivery mileage. The project was created and executed within a virtual environment to ensure a clean and isolated development environment.
****
**Features:**

1. **Package Status Query:** Users can query the status of a specific package by entering the package ID. The application retrieves the package's current status, delivery address, city, zip code, weight, delivery deadline, and other relevant information.
1. **Truck Route Tracking:** The application implements a Greedy algorithm to optimize truck routes and distribution of packages across three trucks (Truck 1, Truck 2, and Truck 3). Each truck is assigned a list of package IDs for delivery, ensuring efficient delivery routes.
1. **Mileage Calculation:** The application calculates the mileage for each truck's route based on the delivery start time and the current query time. It also provides the total mileage for all three deliveries combined.
1. **Virtual Environment:** The project was developed and executed in a virtual environment, ensuring a clean and isolated development environment with specific dependencies and package versions.
****
**Dependencies:** The application utilizes the following Python libraries and modules:

- **tkinter**: For building the GUI and user interface.
- **datetime**: For handling date and time-related operations.
- **csv**: For reading the DistanceData.csv and PackageData.csv files.
- **json**: For reading the truck\_data.json file.
- **tkinter.messagebox**: For displaying error messages in the GUI.
- **tkinter.ttk**: For creating the combobox in the GUI.




****

**File Structure:**

WGUPS\_Package\_Tracker/

├── main.py

├── app.py

├── all\_routes.py

├── rt\_mileage.py

├── pkg\_status.py

├── csv\_to\_hash.py

├── hashmap.py

├── DistanceData.csv

├── PackageData.csv

└── truck\_data.json



****

**Screenshot of the Graphical User Interface**

![alt text](https://github.com/maaxxxx22/Package-Routing-System-/blob/main/app%20images/gui%20print.PNG)



**Note:** Please ensure that all the required data files (**DistanceData.csv**, **PackageData.csv**, and **truck\_data.json**) are present in the project directory before running the application. These files contain essential information for package tracking, mileage calculation, and truck assignment.

