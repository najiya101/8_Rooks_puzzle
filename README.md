# 8 Rooks puzzle
 This Django project includes a web-based implementation of the 8 Rooks Puzzle. It provides a visual representation of the chessboard where users can manually place rooks, check for conflicts, and see if all rooks are placed correctly without attacking each other.

## Features
- Visual Chessboard: An 8x8 interactive chessboard to place rooks manually.
- Conflict Detection: Visual indicators show cells that are under attack if a rook is placed in a conflicting position.
- Error Handling: Displays error messages if the placement of a rook is not possible.
- Responsive Design: The application is accessible on both desktop and mobile devices.
- Reset Option: A button to reset the board and start over.

## Installation
To set up this project locally, follow these steps:

1.Clone the repository.
2.Create a virtual environment:
For Ubuntu:
  - python3 -m venv env
    source env/bin/activate
For Windows:
  - env\Scripts\activate

3.Install the required depemdencies
   pip install -r requirements.txt
4.Run the Django server:
   python manage.py runserver
5.Access the application by navigating to http://127.0.0.1:8000/ (ip) in your web browser.

## Usage
- Manual Mode: Click on the cells of the chessboard to place or remove rooks. If a rook is placed in an unsafe position, an error message is displayed.
- Conflict Detection: The board visually highlights attacked cells when a rook is placed, indicating potential conflicts.
- Reset Board: Click on the reset button to clear the chessboard and start a new game.

## Technologies Used
- Backend: Django (Python)
- Frontend: HTML, CSS, JavaScript

## Screenshots
Here are some screenshots of the application:
<div> <img src="https://github.com/user-attachments/assets/0d6be875-bfa7-495e-b201-db6a951588cb" alt="Initial State" height="500"/> 
 <img src="https://github.com/user-attachments/assets/1d9b56ee-4d57-4d06-a989-aadf90baf3b1" alt="Rook's Placed" height="500"/>
 <img src="https://github.com/user-attachments/assets/ac37df07-97bb-4f17-95a3-cf8fe97e3b17" alt="Conflict" height="500"/>
 <img src="https://github.com/user-attachments/assets/e2c08e18-46e5-49dc-b184-69eb204338a3" alt="Final" height="500"/> </div>

