# vehicle_report_gui.py
# France Cheong
# 11/12/2018

# ########
# Packages
# ########
import tkinter as tk
from tkinter import messagebox
import tkinter.ttk as ttk # for combobox

# Import database.py to get a session to a particular db
import database as db

# Fix for Mac issues - matplolib v3.0.3
# https://github.com/MTG/sms-tools/issues/36
import matplotlib
matplotlib.use("TkAgg") 

# Must import this package when using matplotlib to plot charts in its own GUI
import matplotlib.pyplot as plt

# #################################################
# Import any of your classes defined in other files
# #################################################

# Each GUI class will import the corresponding data access class to communicate with the database

# From file xxx.py import class Xxxx
from vehicle_dao import VehicleDAO

# ######################
# VehicleReportGui Class
# ######################

class VehicleReportGUI():
    """
    GUI class to display report of vehicles
    """

    def __init__(self):   
        """
        The initialiser is used to "instantiate" attributes of the class.

        We cannot create the GUI here as we need to return a reference to the frame created.
        Hence, we need to implement a 'normal' function to do this e.g. create_gui()

        Parameters (apart from self): None

        Return: None

        """
        # Instantiate a data access object 
        # Contains methods to access the database
        self.vhc_dao = VehicleDAO()

        # Form fields
        # Instantiate stringvars/intvars to hold the data entered on the form
        self.reorder_level = tk.IntVar() # Checkbox
        self.lead_time_days = tk.IntVar() # Checkbox
        self.unit_price = tk.IntVar() # Checkbox

        # Set the default value to reorder_level
        # i.e. the reorder_level check box is checked
        # With checkboxes, any number of them can be checked
        # Thus all 3 boxes can be checked
        self.reorder_level.set(1) 

        # Messagebox title
        self.mb_title_bar = "Vehicle Report"

        pass

    def create_gui(self, root):
        """
        Create a high level frame which contains the entire GUI (of this part of the application) and adds it to the root window.

        Widgets like labels, entries, etc  (including inner frames) are added to the high level frame 
        At the end, the function return a reference to the frame that was created for the calling program to be able to access it.

        Parameters (apart from self):
            root: main window of application

        Return: 
            vhc_report_frame: the frame containing all the widgets for the vehicle report frame

        """
        print("Creating vehicle report GUI ...")

        # Create the high level frame
        vhc_report_frame = tk.Frame(root)
        vhc_report_frame.pack()

        # Row 0: Title - span 5 column
        tk.Label(vhc_report_frame, font=('arial', 10), 
                text = "Vehicle Report").grid(row=0, column=0, columnspan=5)

        # Row 1: 3 check boxes and 2 buttons
        tk.Checkbutton(vhc_report_frame, variable=self.reorder_level, 
                       text="Reorder Level").grid(row=1, column=0)
        tk.Checkbutton(vhc_report_frame, variable=self.lead_time_days, 
                       text="Lead Time").grid(row=1, column=1)
        tk.Checkbutton(vhc_report_frame, variable=self.unit_price, 
                       text="Unit Price").grid(row=1, column=2)
        tk.Button(vhc_report_frame, width=10, text="Load", 
                  command=self.get_data_and_display).grid(row=1, column=3)
        tk.Button(vhc_report_frame, width=10, text="Visualise", 
                  command=self.visualise).grid(row=1, column=4)

        # Row 2: text field - span 5 columns
        # Note: txt_result is an attribute (not a local variable) 
        # as it has to be accessed from other places
        self.txt_result = tk.Text(vhc_report_frame, font=('arial', 10), 
                                  height=20, relief="flat")
        self.txt_result.grid(row=2, column=0, columnspan=5)
 
        # Return a reference to the high level frame created
        # Will need the reference to be able to destroy it in the calling function
        return vhc_report_frame

    def get_data_and_display(self):
        """
        Get the data from the database and display the result in the text field
        What is displayed, depends on which checkboxes were ticked on the form

        Parameters (apart from self):

        Return: 
        """
        print("Getting the data for display ...")
        
        # get the data from the database
        # Refer to method find_all() from vehicle_dao.py 
        # to find out about the format of the data returned
        session = db.get_db_session() # Get a session (database.py)
        result = self.vhc_dao.find_all(session)
        session.close() # Close the session
        # print this if you need to get an idea of the data structure
        #print("result", result) 
        
        # Display any error message encountered when fetching data from the database
        if 'message'in result.data():
            # If a "message" entry is present in the result dictionary object
            # Display everything that is returned in the result
            messagebox.showwarning(self.mb_title_bar, result, icon="warning") 

        # Create a header to display in the text area
        # all checkboxes selected - "Vehicle Id, Reorder Level, Lead Time, Unit Price"
        # only unit_price selected - "Vehicle Id, Unit Price"
        # etc
        list_str = []
        list_str.append("Vehicle Id")
        if self.reorder_level.get():
            list_str.append("Reorder Level")
        if self.lead_time_days.get():
            list_str.append("Lead Time")
        if self.unit_price.get() :
            list_str.append("Unit Price")   
        # Add new line
        list_str.append('\n')
        # Join the strings and insert in the text field
        row = ', '.join(list_str)

        # Clear the text box
        self.txt_result.delete('1.0', tk.END)

        # Then insert the header 
        self.txt_result.insert(tk.INSERT, row) 
        
        # Add data rows
        # Need a for loop to process the list of vehicle details 
        # in the result returned from the database
        # Since the values of vehicle_id, reorder_level, lead_time_days are numbers
        # We need to cast them to strings in order to be able 
        # to concatenate/join them into a single string
        for x in result['vehicles']:
            list_str = []
            list_str.append(str(x['vehicle_id']))
            if self.reorder_level.get():
                list_str.append(str(x['reorder_level']))
            if self.lead_time_days.get():
                list_str.append(str(x['lead_time_days']))
            if self.unit_price.get():
                list_str.append(str(x['unit_price']))           
            # Add new line character so that the next row is displayed on another line
            list_str.append('\n')
            # Join the strings as a single string using a comma and a space
            # and insert in the text area
            row = ', '.join(list_str)
            # Then insert the row in the text field
            self.txt_result.insert(tk.INSERT, row) 

            pass

    
    def visualise(self):
        """
        Get the data from the database and display it as a matplotlib bar chart
        Parameters (apart from self):

        Return: 
        """

        print("Getting the data and visualising it ...")
        
        # get the data from the database
        # Refer to method find_all() from vehicle_dao.py 
        # to find out about the format of the data returned
        session = db.get_db_session() # Get a session (database.py)
        result = self.vhc_dao.find_all(session)
        session.close()
        # print this if you need to get an idea of the data structure
        #print("result", result) 

        # Display any error message encountered when fetching data from the database
        if 'message'in result.data():
            # If a "message" entry is present in the result dictionary object
            # Display everything that is returned in the result
            messagebox.showwarning(self.mb_title_bar, result, icon="warning") 

        # Process the data according to which boxes were checked
        list_x = []
        list_reorder_level = []
        list_lead_time_days = []
        list_unit_price = []
        for x in result['vehicles']:          
            list_x.append(x['vehicle_id'])
            if self.reorder_level.get():
                list_reorder_level.append(x['reorder_level'])
            if self.lead_time_days.get():
                list_lead_time_days.append(x['lead_time_days'])
            if self.unit_price.get():
                list_unit_price.append(x['unit_price'])
            pass

        # Plot the bar graph   
        # There are a number of ways to use matplotlib to plot a bar chart
        # I used the simplest possible one with mostly default options
        # Feel free to experiment with other ways of doing so
        # And try the various options to customise your graph to your liking

        # plt is an alias for pyplot from matplotlib
        # imported at the beginning of the file with "import matplotlib.pyplot as plt"
        plt.title('Vehicle characteristics') # set the title of the graph
        plt.xlabel('Vehicle ID') # set the label of the x axis
        #plt.ylabel('Reorder level (units)') # set the label of the y axis

        # Build the y axis label according to what data will be plotted
        # i.e. reorder level and/or lead time and/or unit price
        # At the same time prepare a bar chart of the data
        # again according to what was selected in the check boxes
        label = ""
        if list_reorder_level:
            # Get pyplot to create a bar chart
            # list_x is the list of vehicle_ids to be plotted on the x axis
            # list_reorder_level is the list of reorder_level values to be plotted on the y axis
            # For more details about the options used for "matplotlib bar chart"
            # Refer to https://matplotlib.org/api/_as_gen/matplotlib.pyplot.bar.html
            # or Google these words
            plt.bar(list_x, list_reorder_level, align='center', color='b')
            # Concatenate the label with its previous value i.e. "" + "Reorder level (units)"
            label = label + 'Reorder level (units)'
        if list_lead_time_days:  
            # Plot a bar chart of lead_time_days
            # This chart will be plotted with any other charts selected with the check boxes  
            plt.bar(list_x, list_lead_time_days, align='center', color='g')
            # Adjust the label accordingly
            label = label + '/Lead Time (days)'
        if list_unit_price:    
            # Plot a bar chart of unit_price
            # This chart will be plotted with any other charts selected with the check boxes  
            plt.bar(list_x, list_unit_price, align='center', color='r')
            # Adjust the label accordingly
            label = label + '/Unit Price'

        # set the label of the y axis according to what has been 'concatenated' so far
        plt.ylabel(label)

        # Show the plot! 
        # Where? 
        # The plot will be shown externally in its own popup window
        # In that window, the figure can be edited (to a limited extent)
        # and saved in a variety of formats e.g. png, pdf, etc
        plt.show()

        pass


# ###########
# Main method
# ###########

if __name__ == '__main__':
    """
    The main method is only executed when the file is 'run' 
    (not imported in another file)
    """
     
    # Setup a root window (in the middle of the screen)
    root = tk.Tk()
    root.title("Dealership System")
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    width = 900
    height = 500
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    root.geometry('%dx%d+%d+%d' % (width, height, x, y))
    root.resizable(0, 0)

    # Instantiate the gui
    gui = VehicleReportGUI()

    # Create the gui
    # pass the root window as parameter
    gui.create_gui(root)

    # Run the mainloop
    # the endless window loop to process user inputs
    root.mainloop()

    pass