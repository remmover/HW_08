# Birthday Greeting Program

This program is designed to retrieve and display upcoming birthdays within a week. It takes a list of user information, including their names and birthdates, and identifies the birthdays that fall within the next seven days.

## How to Use

1. Ensure that Python is installed on your system.
2. Download the program files from the repository.
3. Open the `birthday_greeting.py` file in a text editor.
4. Modify the `users` list with the desired user information. Each user should have a `'name'` and `'birthday'` entry. The birthday should be in the format `'dd, mm, yyyy'`.
5. Save the changes to the `birthday_greeting.py` file.
6. Run the program by executing the following command:
   ```
   python birthday_greeting.py
   ```

The program will display the upcoming birthdays within the next seven days, categorized by the day of the week. If any errors occur during the execution, appropriate error messages will be displayed.

## Important Notes

- The program uses the current year as the reference for calculating upcoming birthdays. If a leap year is involved, it adjusts the birthday to February 28th if it falls on February 29th.
- Ensure that the user information provided in the `users` list is in the correct format. The birthday should be a valid date in the format `'dd, mm, yyyy'`.
- If any errors occur during the execution, check the entered data for validity and correct any issues before running the program again.

Feel free to explore and modify the program according to your needs. Enjoy!
