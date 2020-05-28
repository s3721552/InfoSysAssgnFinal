# category_report_gui.py
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

# Must import these packages when using matplotlib to plot charts in your GUI
# Plotting matplotlib charts in your own quite can be quite complex
# I have tried to use a very simple way to do so
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# #################################################
# Import any of your classes defined in other files
# #################################################

# Each GUI class will import the corresponding data access class to communicate with the database

# From file xxx.py import class Xxxx
# From file vehicle_dao.py import class VehicleDAO (data access object)
from vehicle_dao import VehicleDAO

# ######################
# CategoryReportGui Class
# ######################

class CategoryReportGUI():
    """
    GUI class to display report of vhcuct categories
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
        # All the radio buttons point to the single intvar
        # And the value will be 1, 2, 3 or 4 depending which radio button was selected
        # And the value= option assigned to each radio button
        # Unlike check boxes where any number can be selected, 
        # only one option can be selected with radio buttons
        self.radio_button_choice = tk.IntVar() # Radiobutton

        # Set the default value to 1
        self.radio_button_choice.set(1) 

        # Messagebox title
        self.mb_title_bar = "Category Report"

        # Frame containing the canvas for displaying the matplotlib chart
        self.canvas_frame = None

        pass

    def create_gui(self, root):
        """
        Create a high level frame which contains the entire GUI 
        (of this part of the application) and adds it to the root window.

        Widgets like labels, entries, etc  (including inner frames) 
        are added to the high level frame 
        At the end, the function return a reference to the frame that was 
        created for the calling program to be able to access it.

        Parameters (apart from self):
            root: main window of application

        Return: 
            cat_report_frame: 
               the frame containing all the widgets for the vhcuct report frame

        """

        print("Creating category report GUI ...")

    
        # Create the high level frame
        cat_report_frame = tk.Frame(root)
        cat_report_frame.pack()

        # row 0: Title - span 5 columns
        tk.Label(cat_report_frame, font=('arial', 10), 
                 text = "Category Report").grid(row=0, column=0, columnspan=5)

        # row 1: 4 radio buttons and 1 button - span 5 cols
        tk.Radiobutton(cat_report_frame, text="Reorder Level", 
                       variable=self.radio_button_choice, value=1).grid(row=1, column=0) 
        tk.Radiobutton(cat_report_frame, text="Lead Time", 
                       variable=self.radio_button_choice, value=2).grid(row=1, column=1)
        tk.Radiobutton(cat_report_frame, text="Unit Price", 
                       variable=self.radio_button_choice, value=3).grid(row=1, column=2)
        tk.Radiobutton(cat_report_frame, text="Discontinued", 
                       variable=self.radio_button_choice, value=4).grid(row=1, column=3)
        tk.Button(cat_report_frame, width=10, text="Visualise", 
                  command=self.visualise).grid(row=1, column=4)
    
        # row 2: canvas
        # Need to create a frame to store the canvas
        # As will not be able to pack() the canvas in a frame that is managed by grid()
        # Use grid() to position (instead of pack())
        self.canvas_frame = tk.Frame(cat_report_frame)
        self.canvas_frame.grid(row=2, column=0, columnspan=5)

        # Return a reference to the category report frame
        # Will need the reference to be able to destroy it in the calling function
        return cat_report_frame

    def visualise(self):
        """
        Get the data from the database and display it as a matplotlib bar chart
        Parameters (apart from self):

        Return: 
        """

        print("Getting the data and visualising it ...")
        
        # get the data from the database
        # Refer to method find_categories() from vehicle_dao.py 
        # to find out about the format of the data returned
        session = db.get_db_session() # Get a session (database.py)
        result = self.vhc_dao.find_categories(session)
        session.close() # Close the session
        # Print this if you need to get an idea of the data structure
        #print("result", result) 
        
        # Display any error message encountered when fetching data from the database
        if 'message'in result.keys():
            # If a "message" entry is present in the result dictionary object
            # Display everything that is returned in the result
            messagebox.showwarning(self.mb_title_bar, result, icon="warning") 

        # Get the data
        # Load the categories dict
        result = result['categories']

        # Get the list of keys of the dict - these will be the labels for your pie chart
        #self.list_cat = result.keys() # TypeError: 'dict_keys' object does not support indexing
        # Loop through the keys of the dictionary and append the keys to a simple list
        labels = [x for x in result.keys()] # Using list comprehension instead of a traditional for loop
        sizes = []

        # Process the data to plot
        # Use a for loop to extract the "values" of each of the "keys" in the dictionary
        # For each "value", extract the values of the different entries 
        # e.g. count, reorder_level, lead_time_days, unit_price
        # And compute values that make sense
        # e.g. for some values sum does not make sense
        # OK for discontinued as they are either 1 or 0
        # but not OK for unit_price etc
        # In these cases, compute the average level/days/price of the vhcucts in that particular category
        for x in result.keys():
        #for i, x in enumerate(result.keys()): # use enumerate if need to get an index (a count)
            # Grab the dictionary object representing the "value" of that particular "key"
            val = result[x]
            #print(val)
            #count = val['count']

            # Grab all the values available
            # And compute metrics of interest
            avg_reorder_level = val['reorder_level']/val['count']
            avg_lead_time_days = val['lead_time_days']/val['count']
            avg_unit_price = val['unit_price']/val['count']
            discontinued = val['discontinued']

            # Build a list of only the values required as per radio button selection
            # The list is called "sizes" and for each pass of the for loop we are appending a value
            if self.radio_button_choice.get()==1:  # CAREFUL - must use get() method of the IntVar
                sizes.append(avg_reorder_level)
                pass

            if self.radio_button_choice.get()==2: 
                sizes.append(avg_lead_time_days)
                pass

            if self.radio_button_choice.get()==3: 
                sizes.append(avg_unit_price)
                pass

            if self.radio_button_choice.get()==4: 
                sizes.append(discontinued)
                pass

        # For debugging
        print("choice", self.radio_button_choice.get())
        print("sizes", sizes)
        print("labels", labels)
         
        """
        # Plot the pie chart outside the GUI
        plt.title('vhcuct categories')
        plt.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=140)
        plt.axis('equal')        
        plt.show()
        """

        # Plot the chart inside the GUI (in a canvas)
        # The algorithm/procedure for doing this can be very complicated
        # And there are several ways to do this
        # You might find a number of complicated methods if you google  "tkinter matplotlib"
        # I have tried to make it as simple as possible

        # Get a figure for plotting
        # For more details about "matplotlib figure", refer to 
        # https://matplotlib.org/api/_as_gen/matplotlib.pyplot.figure.html
        # figsize=(6,5) represents a figure 6 inches high and 5 inches wide
        # dpi=100 represents the resolution of 100 dots-per-inch 
        # The 2 options are "optional" 
        # If they are omitted, the default sized is 6.4 x 4.8 and the dpi is 100
        figure1 = plt.Figure(figsize=(6,5), dpi=100) 
        #figure1 = plt.Figure() 
        #figure1 = plt.Figure(figsize=(7,6))

        # Add a sub-plot to the figure
        # For more details about "matplotlib subplot" refer to
        # https://matplotlib.org/api/_as_gen/matplotlib.pyplot.subplot.html
        # The subplot grid parameters encoded as a single integer
        # e.g. subplot(111) means "1x1 grid, first subplot" 
        # subplot(234) means "2x3 grid, 4th subplot"
        # etc
        # Alternative form for add_subplot(111) is add_subplot(1, 1, 1)
        ax1 = figure1.add_subplot(111) 

        # Get a canvas for the figure - a tk drawing area
        # This was imported with the statement
        # "from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg"
        # For more details on "FigureCanvasTkAgg", 
        # refer to https://matplotlib.org/gallery/user_interfaces/embedding_in_tk_sgskip.html
        # However, be careful as the example provided there is quite sophisticated (and complex)!
        canvas1 = FigureCanvasTkAgg(figure1, self.canvas_frame) 
        # Notice that canvas1 is linked to self.canvas_frame that was created in the create_gui() method 

        #canvas1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH) 
           # Not good, keeps adding new plots to the right
        #canvas1.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH) # Pack the canvas - OK
        canvas1.get_tk_widget().pack(side=tk.BOTTOM) # Pack the canvas to make it visible - OK

        # Get matplotlib to create a pie chart
        # For more details on the options available for the pie() 
        # method to customize your "matplotlib pie chart",
        # refer to https://matplotlib.org/api/_as_gen/matplotlib.pyplot.pie.html
        ax1.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=140) 

        # Set the title of the plot according to what was selected
        if self.radio_button_choice.get()==1: 
            ax1.set_title('Reorder Level (units)')

        if self.radio_button_choice.get()==2: 
            ax1.set_title('Lead Time (days)')

        if self.radio_button_choice.get()==3: 
            ax1.set_title('Unit Price ($)')

        if self.radio_button_choice.get()==4: 
            ax1.set_title('Discontinued')

        # If you have more plots, keep repeating the above
        # e.g. figure2, etc

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
    gui = CategoryReportGUI()

    # Create the gui
    # pass the root window as parameter
    gui.create_gui(root)

    # Run the mainloop
    # the endless window loop to process user inputs
    root.mainloop()
