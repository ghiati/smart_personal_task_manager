# Task Manager with NLP Feature
## Overview

This is a simple web application for managing tasks, built with Flask. It lets you add and remove tasks, and includes a feature that uses Natural Language Processing (NLP) to understand and process natural language commands, like extracting dates and times.

## Features

- **User Authentication:** Register, log in, and log out.
- **Task Management:** Add and delete tasks.
- **NLP Integration:** Parse commands to identify dates and times.

## Installation

### Prerequisites

- Python 3.x
- MongoDB running 

### Install Dependencies

1. **Clone the Repository:**

2. **Install the Required Packages:**

   Create a `requirements.txt` file 

   Then run:

   ```bash
   pip install -r requirements.txt
   ```

3. **Download spaCy Model:**

   ```bash
   python -m spacy download en_core_web_sm
   ```

## MongoDB Setup

Make sure MongoDB is installed and running. The app connects to MongoDB with the following details:

- **Database Name:** `task_manager`
- **Collections:**
  - `users`
  - `tasks`

The connection details are managed in `database.py`:

## Usage

1. **Run the Application:**

   ```bash
   python man.py
   ```

2. **Open the App:**

   Go to `http://localhost:5000` in your web browser.

3. **Use the App:**

   - **Register:** Create a new account.
   - **Login:** Access your task manager.
   - **Add Tasks:** Type tasks in natural language, like "Call the doctor tomorrow at 10 AM."
   - **Delete Tasks:** Remove tasks when needed.

## Code Explanation

### `app.py`

- **Routes:**
  - `/`: Shows the login page.
  - `/register`: Handles registration.
  - `/login`: Logs users in.
  - `/logout`: Logs users out.
  - `/tasks`: Shows the user’s tasks.
  - `/add_task`: Adds new tasks, including those parsed from natural language.
  - `/delete_task/<task_id>`: Deletes tasks by ID.

### `nlp_utils.py`

- **`parse_command(command)` Function:**
  - Uses spaCy to find dates and times in commands.
  - Returns a list with recognized dates and times.

### `database.py`

- **`get_database()`:** Connects to MongoDB and gets the `task_manager` database.
- **`get_users_collection()`:** Gets the `users` collection.
- **`get_tasks_collection()`:** Gets the `tasks` collection.

## Contributing

1. **Fork the Repository:**
2. **Create a Branch:**
3. **Make Changes:**
4. **Push Your Changes:**
5. **Submit a Pull Request:**

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
