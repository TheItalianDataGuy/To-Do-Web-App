# To-Do List App

This project is a simple To-Do list application built with Streamlit for the frontend and Python for the backend. The app allows users to add, display, and remove tasks from a list. The tasks are stored in a text file, ensuring persistence across sessions.

## Features

- **Add Tasks**: Users can add new tasks to the list.
- **Display Tasks**: The app displays all the tasks in the list with checkboxes.
- **Remove Tasks**: Users can mark tasks as completed by checking them off, which will remove them from the list.
- **Persistent Storage**: Tasks are stored in a text file, so they persist even after the app is closed.

## Project Structure

```plaintext
.
├── ToDo.txt                    # File storing the to-do tasks
├── app.py                      # Main Streamlit application file (Frontend)
├── functions.py                # Backend functions to manage the tasks
├── png.jpg                     # Image displayed in the app
└── README.md                   # Project documentation
```

## Installation
1. Clone the repository:

  ```bash
  git clone https://github.com/yourusername/todo-list-app.git
  cd todo-list-app
  ```
2. Install the required packages:
- Ensure you have Python installed, then install the necessary packages:

  ```bash
  pip install streamlit
  ```
3. Create the ToDo.txt file:
  If not already present, create a file named ToDo.txt in the project directory. This file will be used to store your tasks.

## Usage
1. Run the Streamlit App:

  ```bash
  streamlit run app.py
  ```

2. Interact with the To-Do List:

  - Add a Task: Use the text input field to add a new task.
  - Remove a Task: Click the checkbox next to a task to mark it as completed and remove it from the list.

3. Tasks Storage:
  - All tasks are stored in the ToDo.txt file in the project directory. This ensures that your tasks are saved even after the app is closed.

## Backend Functionality
- get_todos(filepath=FILEPATH): Reads the tasks from the ToDo.txt file and returns them as a list.
- write_todos(todos_arg, filepath=FILEPATH): Writes the tasks list to the ToDo.txt file.

## Example
Here is a simple example of how the app works:

- You open the app and see your current to-do list.
- You can add a new task by typing into the input field and pressing enter.
- You can remove a task by checking the checkbox next to it, which will automatically update the list.

## License
This project is licensed under the MIT License.

## Acknowledgments
Streamlit for making it easy to create web applications in Python.
