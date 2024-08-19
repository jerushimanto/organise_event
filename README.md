# Event Scheduling and Registration System

This is a simple web application that allows users to schedule events, register for them, and maintains a record of the events and registrations. The application uses MySQL for its database, and you have two options to set up the database:


## MySQL Installation

1. Install MySQL on your local machine and configure a username and password.
2. Replace the inactive RDS instance endpoint in the `views.py` file with the appropriate local MySQL connection details.
3. Update the `username` and `password` in the `database_creation.py` file with the credentials you used while installing MySQL.
4. Use `localhost` for the database host
5. Run `database_creation.py` to create the necessary database, tables, and relationships.



# Running the Application

Follow the steps below to run the Event Scheduling and Registration System application using a local MySQL installation:

1. **Install MySQL instance:**
   - Install MySQL(Follow above steps).

2. **Install Required Libraries:**
   - Open a terminal and run the following command:
     ```bash
     pip install -r requirements.txt
     ```
3. **Create Database and Tables:**
   - Run `database_creation.py` to create the necessary database.
   - Update the `username` and `password` in the `settings.py` file with the credentials you will use to establish a connection.
   - Create and apply the migrations to update the database schema:

      ```bash
      python manage.py makemigrations
      python manage.py migrate
      ```

4. **Run the Server:**
   - Execute the following command to run the server:
     ```bash
     python manage.py runserver
     ```

5. **Access the Application:**
   - Use the local address
     ```bash
     127.0.0.0/
     ```

## **Important Note** ##
  - This application is built for educational purposes and it is not for production.
  - It's essential to follow security best practices when deploying applications to production environments. 
  - Avoid exposing sensitive information, such as database credentials, in public repositories. Consider using environment variables or other secure methods for configuration.

**Feel free to explore and modify the code to suit your needs. If you encounter any issues or have suggestions for improvements, please open an issue on this repository.**


