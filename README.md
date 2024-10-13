# TaskNest

TaskNest is a modern and intuitive task management web application designed to help users organize and manage their daily tasks efficiently. Built with Django, TaskNest allows users to prioritize tasks, set due dates, and keep track of completed tasks with a simple and user-friendly interface.

## Features

- **User Registration & Authentication**: 
  - Secure user registration, login, and logout functionalities.
  - Password validation ensures strong security during registration.

- **Task Management**:
  - Add, update, and delete tasks easily.
  - Each task includes a name, due date, priority level, and completion status.
  - Automatically track overdue tasks and highlight them for immediate attention.

- **Priority Levels**:
  - Tasks can be assigned one of three priority levels: **Low**, **Medium**, or **High**.
  - Tasks are sorted by priority and due date, ensuring important tasks are always at the top of your list.

- **Due Dates**:
  - Set due dates for each task, with the ability to mark tasks as overdue if they are past their due date and incomplete.

- **Task Filtering**:
  - View tasks based on their priority, due date, or completion status.

- **Responsive Design**:
  - Fully responsive interface, allowing users to manage their tasks across devices seamlessly.

- **Messages & Alerts**:
  - Feedback messages for successful actions like task addition, updates, and deletion.
  - Alerts for invalid input, such as weak passwords or duplicate usernames.


## Tech Stack

### Backend:
- **Django**: A powerful web framework used for rapid development.
  - Django's built-in **ORM** to interact with the SQLite database.
  - **Django Forms** for handling and validating form input.
  - **Django Authentication** system for secure user registration and login.
  
### Frontend:
- **HTML5, CSS3, JavaScript**: For creating a clean and responsive user interface.
- **Bootstrap**: A front-end framework for styling, making the app responsive across various devices.
  
### Database:
- **SQLite**: Lightweight, file-based database used for development.

### Other Tools & Libraries:
- **Django Messages Framework**: For providing success/error messages.
- **Django Templating Engine**: Used for rendering dynamic content in HTML templates.

## Installation & Setup

### Requirements:
- Python 3.x
- Django 4.x

### Setup Instructions:

1. Clone the repository:
   ```bash
   git clone https://github.com/AbhinavJian3/TaskNest.git
   cd TaskNest
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Migrate the database:
   ```bash
   python manage.py migrate
   ```

5. Create a superuser to access the admin panel (optional):
   ```bash
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```bash
   python manage.py runserver
   ```

7. Open the application in your browser:
   ```
   http://127.0.0.1:8000/
   ```

## Usage

- After registering an account, log in to manage your tasks.
- Add new tasks with names, due dates, and priority levels.
- View your task list sorted by priority and due date.
- Mark tasks as complete or delete them as needed.
- Overdue tasks will be highlighted in the task list.
