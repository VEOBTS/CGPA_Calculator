# BHU-NACOS CGPA Calculator For 100lvl Students

# HOW WE MADE THE CGPA CALCULATOR
	
1. Setting Up the Environment:
   - We started by importing the necessary modules from the ‘tkinter’ library, which is used for creating graphical user interfaces (GUIs) in Python.

2. Designing the Interface:
   - The main window (‘window’) was created with a specified title and size using ‘tk.Tk()’ and ‘window.geometry()’ functions.

3. Creating Labels and Entry Fields:
   - Labels and entry fields were designed to display course information and allow users to input their grades. These were positioned in the window using the ‘Label’ and ‘Entry’ widgets.

4. Initializing Variables:
   - String variables (‘StringVar()’) were initialized to store the grades entered by the user and the results (CGPA and class).
   - Dictionaries were also created to store course data and grade points.

5. Calculating CGPA:
   - Functions were defined to calculate grade points based on the entered grades and to calculate the overall CGPA by summing up the products of grade points and credit units for each course.

6. Classifying CGPA:
   - Another function was created to classify the CGPA into different categories (First Class, Second Class Upper, Second Class Lower, Third Class, or Fail) based on predefined criteria.

7. Displaying Results:
   - Labels were used to display the results on the interface, such as the calculated CGPA and its classification.

8. User Interaction:
   - A button was implemented to trigger the calculation process when clicked. This button was connected to a function (‘calculate_cgpa()’) that executed the necessary calculations.
   - A button was also implemented to trigger an exit process when clicked. This button was connected to a command that when clicked, would close the main window, effectively exiting the program.

9.  User-Friendly Interface:
   - The interface was designed to be user-friendly, providing a welcoming message, clear instructions, and a visually appealing layout.

10.  Handling Errors:
   - In the initial version, we included error handling to check for invalid grades. However, after further consideration, this part was later removed. Hereby declaring that any input other than [‘A’, ‘B’, ‘C’, ‘D,’ ‘E’, ‘F’] would be regarded as [‘F’]

11.  Running the Program:
    - The main event loop (‘window.mainloop()’) was started to run the program, allowing users to interact with the graphical interface.


By following these steps, we created a fully functional CGPA calculator that students at Bingham University can use to easily calculate their academic performance and gain insights into their CGPA classification.


# For further research, or more info about tkinter and GUIs:
We recommend the following;

1.	Everything about Tkinter: 
Programming Knowledge YouTube Channel: 
https://youtube.com/playlist?list=PLS1QulWo1RIY6fmY_iTjEhCMsdtAjgbZM&si=90MXYVN-FBJi4BHT

3.	Everything about Graphical User Interface (GUI):
Realpython.com:
https://realpython.com/learning-paths/python-gui-programming/





THIS ENTIRE PROJECT WAS PLANNED, CREATED & DOCUMENTED BY:

The Acting Group Leader;

FAVOUR LAWRENCE EJIOGU – BHU/23/04/09/0058 – 07083123998

With Contributions From;

Nomtheik Esther Kure - BHU/23/04/05/0032 - 09065660700,
Emmanuella Japari Waba - BHU/23/04/05/0067 - 09042393832,
Stephanie Chinaza Anyanwu - BHU/23/04/05/0038 - 08074409307 &
Victor Adeyemo – BHU/23/04/09/0005 – 08051288810
