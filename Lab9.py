#Lab 9
# Author: Maksym Fedenko

"""_summary_

This lab is designed to create a simple web application using streamlit and create a simple Date counter using datetime.
"""

# 1. We will first need to activate and install streamlit.


# 2. Import streamlit and datetime
import streamlit as st
import datetime as dt

# 3. Create a title for the web application
st.title("Simple Date Counter App")

# 4. Create a subheader for the web application
st.subheader("Enter a date to calculate days from today")

# 5. Create a date input for the user
user_date = st.date_input("Choose a date")

# 6. Create a button for the user to click
button_clicked = st.button("Calculate Days")

# 7. Create a function to calculate days
def calculate_days(target_date):
    # Get the current date
    current_date = dt.date.today()
    # Calculate the difference
    difference = target_date - current_date
    # Return the number of days
    return difference.days

# 8. Create an app function
def run_app():
    # Check if the button has been clicked
    if button_clicked:
        try:
            # Call the calculate_days function
            days_until = calculate_days(user_date)
            # Print the result
            st.write(f"Days until {user_date}: {days_until}")
        except Exception as e:
            st.error("An error occurred: " + str(e))




# 8. Create an app function that will run the web applicatio1111n.
# Check if the button has been clicked, then call the calculate_days function and pass in the date entered by the user. Use a try except block to catch any errors.
# Save the result into a variable.
# Print out the result.


# 9. Run the web application by typing streamlit run Lab9.py in the terminal.
# 10. Enter a date in the format of YYYY-MM-DD and click the button.
# 11. Check to see if the number of days until the date entered is correct.
# 12. If the number of days is correct, then you have completed the lab.
# 13. If the number of days is incorrect, then you will need to debug your code.

if __name__ == '__main__':
    run_app()