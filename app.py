# Name: Okunta Braide  Student ID: 002450037

import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from all_routes import delivery
from rt_mileage import Mileage
from pkg_status import PackageStatus
import datetime


# Identify a named self-adjusting algorithm: Greedy algorithm
# We have used Tkinter library to create the application
# The space complexity of the Application is O(n^2) as all the calculated functions have complexity of O(n^2)

class MainGUI:
    def __init__(self, win):
        self.win = win
        self.win.title("WGUPS Package Tracker")

        self.numberOfPackages = 40
        self.queryTime = tk.StringVar()
        self.mainQuery = tk.StringVar()
        self.packageId = tk.StringVar()
        self.winWidth = 500
        self.winHeight = 350
        self.labels = []
        self.position_windows()

        self.create_controls()

    # Create a new window
    def display_package_status(self, package_status):
        status_window = tk.Toplevel(self.win)
        status_window.title("Package Status")

        # Create a label to display the package status
        status_label = tk.Label(status_window, text=package_status, font=("Arial", 10))
        status_label.pack()

    # Position the windows in center of screen
    def position_windows(self):
        screenWidth = self.win.winfo_screenwidth()
        screenHeight = self.win.winfo_screenheight()

        posX = (screenWidth // 2) - (self.winWidth // 2)
        posY = (screenHeight // 2) - (self.winHeight // 2)

        self.win.geometry(f"{self.winWidth}x{self.winHeight}+{posX}+{posY}")

    # Initialize and configure the GUI components
    def create_controls(self):
        time_label = tk.Label(self.win, text="Time(HH:MM:SS format):", font=("Arial", 12))
        time_label.grid(row=0, column=0, sticky="e")

        status_label = tk.Label(self.win, text="Type:", font=("Arial", 12))
        status_label.grid(row=1, column=0, sticky="e")

        pkg_label = tk.Label(
            self.win, text=f"Package ID(1-{self.numberOfPackages}):", font=("Arial", 12)
        )
        pkg_label.grid(row=2, column=0, sticky="e")

        time_entry = tk.Entry(self.win, textvariable=self.queryTime, font=("Arial", 12))
        time_entry.grid(row=0, column=1)

        options = ["all", "pkg", "done"]
        mainQuery = tk.StringVar()
        self.statusEntry = ttk.Combobox(
            self.win, textvariable=mainQuery, values=options, font=("Arial", 11)
        )
        self.statusEntry.set("Select an option")

        self.statusEntry.bind("<<ComboboxSelected>>", self.handle_selection)
        self.statusEntry.grid(row=1, column=1)

        pkg_entry = tk.Entry(self.win, textvariable=self.packageId, font=("Arial", 12))
        pkg_entry.grid(row=2, column=1)

        submit_button = tk.Button(
            self.win, text="Submit", command=self.submit_handler, font=("Arial", 12)
        )
        submit_button.grid(row=3, columnspan=2, pady=10)

        self.result_listbox = tk.Listbox(self.win, font=("Arial", 10))
        self.result_listbox.grid(row=4, column=0, columnspan=2, sticky="nsew", padx=10, pady=5)

        self.win.grid_rowconfigure(4, weight=1)
        self.win.grid_columnconfigure(0, weight=1)
        self.win.grid_columnconfigure(1, weight=1)

        self.win.grid_rowconfigure(0, weight=1)
        self.win.grid_rowconfigure(1, weight=1)
        self.win.grid_rowconfigure(2, weight=1)
        self.win.grid_rowconfigure(3, weight=1)
        self.win.grid_rowconfigure(4, weight=1)
        self.win.grid_rowconfigure(5, weight=1)

    # select handler for Type dropdown
    def handle_selection(self, event):
        selected_item = self.statusEntry.get()
        # print("Selected item:", selected_item)


    # submit handler for the form
    def submit_handler(self):
        queryTime = self.queryTime.get().strip()
        mainQuery = self.statusEntry.get()
        packageId = self.packageId.get().strip()

        if queryTime == "done":
            self.win.quit()
        elif mainQuery == "done":
            self.win.quit()
        elif queryTime and mainQuery == "all":
            # Retrieve delivery data
            d1, d2, d3, hashRecords = delivery()

            # Validations
            # Convert queryTime to datetime object
            mil_time_format = "%H:%M:%S"
            try:
                valid_time = datetime.datetime.strptime(queryTime, mil_time_format)
            except ValueError:
                messagebox.showerror(
                    "Error", "Invalid time format. Please enter time in HH:MM:SS format."
                )
                return

            # Get mileage data
            del1_miles, del2_miles, del3_miles, total_miles = Mileage.route_mileage(
                valid_time, d1, d2, d3
            )

            # Prepare the results
            arrResults = []
            arrResults.append(f"Delivery 1 (Truck 1 first trip) mileage: \033[31m{del1_miles} miles\033[0m")
            arrResults.append(f"Delivery 2 (Truck 2): \033[31m{del2_miles} miles\033[0m")
            arrResults.append(f"Delivery 3 (Truck 1 second trip): \033[31m{del3_miles} miles\033[0m")
            arrResults.append(
                f"Total Mileage (all 3 Deliveries) at Time {valid_time.time()}: \033[31m{total_miles} miles\033[0m"
            )

            # Clear the previous results
            self.print_heading("MILEAGE FOR ALL TRUCKS AND DELIVERY TRIPS")
            self.show_results(arrResults)

            # Prepare the package statuses
            package_statuses = []
            package_statuses.append(f"\nTOTAL MILEAGE FOR ALL TRIPS BY {valid_time.time()} IS {total_miles} MILES")
            package_statuses.append(f"\nALL PACKAGES ON DELIVERY 1 (TRUCK 1 FIRST TRIP):")
            for i in d1[2]:
                package_status = PackageStatus.getPackageStatus(i, valid_time, hashRecords, False)
                package_statuses.extend(package_status)

            package_statuses.append("\nALL PACKAGES ON DELIVERY 2 (TRUCK 2):")
            for i in d2[2]:
                package_status = PackageStatus.getPackageStatus(i, valid_time, hashRecords, False)
                package_statuses.extend(package_status)

            package_statuses.append("\nALL PACKAGES ON DELIVERY 3 (TRUCK 1 SECOND TRIP):")
            for i in d3[2]:
                package_status = PackageStatus.getPackageStatus(i, valid_time, hashRecords, False)
                package_statuses.extend(package_status)

            # Clear the previous results
            self.result_listbox.delete(0, tk.END)

            # Add the package statuses to the listbox
            for package_status in package_statuses:
                if "Delivery Status" in package_status:
                    # Set delivery lines to green color
                    self.result_listbox.insert(tk.END, package_status)
                    self.result_listbox.itemconfig(tk.END, fg="green")
                    self.print_colored_result(package_status)
                elif "ALL PACKAGES ON" in package_status:
                    # Set delivery 1 lines to bold black color
                    self.result_listbox.insert(tk.END, package_status)
                    self.result_listbox.itemconfig(tk.END, fg="blue")
                    self.print_heading(package_status)
                elif "STATUS OF PKG" in package_status:
                    # Set delivery 1 lines to bold black color
                    self.result_listbox.insert(tk.END, package_status)
                    self.result_listbox.itemconfig(tk.END, fg="blue")
                    self.print_colored_result(package_status)
                elif "TOTAL MILEAGE FOR" in package_status:
                    self.result_listbox.insert(tk.END, package_status)
                    self.result_listbox.itemconfig(tk.END, fg="red")
                    self.print_colored_result(package_status)

                else:
                    # Set other lines to default color (black)
                    self.result_listbox.insert(tk.END, package_status)
                    self.result_listbox.itemconfig(tk.END, fg="black")
                    print(package_status)

    # Prints the package status with colored text based on its type.
    def print_colored_result(self, package_status):
        if "Delivery Status" in package_status:
            print("\033[32m" + package_status + "\033[0m")  # Green color
        elif "ALL PACKAGES ON" or "STATUS OF PKG" in package_status:
            print("\033[34m" + package_status + "\033[0m")  # Blue color
        else:
            print(package_status)

    # Prints a heading line with stars and the provided heading text.
    def print_heading(self, heading):
        print("\033[33m" + "*" * 49)
        print(heading.strip())
        print("*" * 49 + "\033[0m")

    # Displays the results in the listbox and prints them on the console.
    def show_results(self, arrResults):
        self.result_listbox.delete(0, tk.END)
        for result in arrResults:
            self.result_listbox.insert(tk.END, result)
            print(result)


    # Removes the specified labels from the GUI.
    def remove_results(self, labels):
        for label in labels:
            label.grid_forget()

    # Updates the height of the GUI window based on the content height.
    def update_height(self, labels):
        content_height = self.calculate_content_height(labels) + self.winHeight
        screenWidth = self.win.winfo_screenwidth()
        screenHeight = self.win.winfo_screenheight()

        posX = (screenWidth // 2) - (self.winWidth // 2)
        posY = (screenHeight // 2) - (content_height // 2)

        self.win.geometry(f"{self.winWidth}x{content_height}+{posX}+{posY}")


    # Calculates the total height of the specified labels.
    def calculate_content_height(self, labels):
        total_height = sum(widget.winfo_height() for widget in labels)
        return total_height



if __name__ == "__main__":
    win = tk.Tk()

    app = MainGUI(win)

    win.mainloop()

