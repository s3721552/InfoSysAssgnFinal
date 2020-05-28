# dealership_main_gui.py
# Omar Adnan
# 18-05-2020

# ########
# Packages
# ########
import tkinter as tk
from tkinter import messagebox
import database as db
"""
# #################################################
# Import any of your classes defined in other files
# #################################################

# Import all the GUI classes implementing each menu option
# e.g. VehicleGUI, SalesPersonGUI, SupplierGUI, PurchaseOrderGUI
# Each GUI class will import the corresponding data access class 
# to communicate with the database
# The GUI classes also import a single Validation class containing 
# all necessary validation methods

# From file xxx.py import class Xxxx
"""
from vehicle_gui import VehicleGUI
from salesperson_gui import SalesPersonGUI
"""
#from supplier_gui import SupplierGUI # ==> Not implemented
#from purchase_order_gui import PurchaseOrderGUI

# Reports GUI
#from salesperson_report_gui import SalesPersonReportGUI
#from category_report_gui import CategoryReportGUI


# ################
# Global Constants 
# ################


# ####################
# DealershipGui Class
# ####################
"""
class DealershipGUI():

    def __init__(self):   

        print("Creating Dealership GUI ...")

        self.current_gui = None # Reference to current GUI 

        # Step 1. Create main window of the application
        # 900x500 pixels in the middle of the screen
        # Can minimise to 0x0 pixels
        self.root = tk.Tk()
        self.root.title("Dealership System")
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        width = 900
        height = 600
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)
        print("Main window coordinates (width, height, x, y) :", 
              width, height, x, y)
        self.root.geometry('%dx%d+%d+%d' % (width, height, x, y))
        self.root.resizable(0, 0)

        # Step 2. Add a menu

        # Create a toplevel menu
        menubar = tk.Menu(self.root)

        # File menu (pulldown)
        # Create a pulldown menu
        filemenu = tk.Menu(menubar, tearoff=0)
        # Add menu items
        filemenu.add_command(label="Open", command="")
        filemenu.add_command(label="Save", command="")
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.root.quit)
        # Add pulldown menu to toplevel menu
        menubar.add_cascade(label="File", menu=filemenu)
       
        # Vehicle menu (pulldown)
        # Create a pulldown menu
        vehicle_menu = tk.Menu(menubar, tearoff=0)
        # Add menu items
        # do not use self.create_vehicle_gui()
        vehicle_menu.add_command(label="Vehicle", 
            command=self.create_vehicle_gui) 
        # Add pulldown menu to toplevel menu
        menubar.add_cascade(label="Vehicle", menu=vehicle_menu)
      
        # SalesPerson menu (pulldown)
        # Create a pulldown menu
        salesperson_menu = tk.Menu(menubar, tearoff=0)
        # Add menu items
        salesperson_menu.add_command(label="SalesPerson", 
            command=self.create_salesperson_gui) 
        # Add pulldown menu to toplevel menu
        menubar.add_cascade(label="SalesPerson", menu=salesperson_menu)

        '''
        # Supplier menu (pulldown) ==> Not implemented
        # Create a pulldown menu
        supplier_menu = tk.Menu(menubar, tearoff=0)
        # Add menu items
        supplier_menu.add_command(label="Supplier", 
            command=self.create_supplier_gui) 
        # Add pulldown menu to toplevel menu
        menubar.add_cascade(label="Supplier", menu=supplier_menu)
        '''
        
        # Purchase order menu (pulldown)
       # purchase_order_menu = tk.Menu(menubar, tearoff=0)
        # Add menu items
        #purchase_order_menu.add_command(label="Purchase-Order", 
         #   command=self.create_purchase_order_gui) 
        # Add pulldown menu to toplevel menu
        #menubar.add_cascade(label="Purchase-Order", menu=purchase_order_menu)

        # Reports menu (pulldown)
        reports_menu = tk.Menu(menubar, tearoff=0)
        reports_menu.add_command(label="SalesPerson Report", 
                                 command=self.create_salesperson_report_gui)
        reports_menu.add_command(label="SalesPerson Category Report", 
                                 command=self.create_category_report_gui)
        menubar.add_cascade(label="Reports", menu=reports_menu)

        # Display the menu
        self.root.config(menu=menubar)

        pass
            
    # Functions to create child frames 
    # when menu options are selected

    def create_vehicle_gui(self):

        if self.current_gui:
            self.current_gui.destroy()

        vehicle_gui = VehicleGUI()
        self.current_gui = vehicle_gui.create_gui(self.root)

        pass

    def create_salesperson_gui(self):

        if self.current_gui:
            self.current_gui.destroy()

        salesperson_gui = SalesPersonGUI()
        self.current_gui = salesperson_gui.create_gui(self.root)

        pass
        
    #def create_supplier_gui(self):
        pass 

   # def create_purchase_order_gui(self):
        pass

    def create_salesperson_report_gui(self):
        pass        

    def create_category_report_gui(self):
        pass        

# ###########
# Main method
# ###########

if __name__ == '__main__':
    """
    The main method is only executed when the file is 'run' 
    (not imported in another file)
    """
    # Instantiate the main application gui 
    # it will create all the necessary GUIs
    gui = DealershipGUI()

    # Run the mainloop 
    # the endless window loop to process user inputs
    gui.root.mainloop()
    pass        