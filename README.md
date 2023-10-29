# BugTracker App

The BugTracker App is a tool designed to help manage and track bugs, issues, or tasks within a project. It provides functionalities to record, monitor, and resolve reported issues, ensuring a smoother project development cycle.

## Features

- **Bug Creation**: Users can create new bug reports with detailed information, including title, description, severity, and status.
- **Update and Resolve Bugs**: Ability to update bug status, assign to team members, and mark bugs as resolved.
- **Delete Bugs**: Users with appropriate permissions can remove bugs that are no longer relevant or have been mistakenly created.
- **User Authentication**: coming soon.

## Technologies Used

- **FastAPI**: A modern, fast (high-performance), web framework for building APIs with Python.
- **SQLAlchemy**: An SQL toolkit and Object-Relational Mapping (ORM) that provides efficient database management.
- **Python 3.x**: The programming language used for the backend logic.

## Installation

1. **Clone the Repository**: `git clone https://github.com/yourusername/BugTracker.git`
2. **Install Dependencies**: `cd BugTracker` then `pip install uvicorn`, `pip install fastapi`, `pip install sqlalchemy`, `pip install alembic`
3. **Database Setup**: Set up your database and ensure the connection details are configured in the application.
4. **Run the Application**: `uvicorn main:app --reload`

## API Endpoints
- **Create Bug**:
  - `POST /bugs/`
  - Description: Create a new bug report with detailed information.
  - Request Body: BugData (Bug details including title, description, and other necessary fields).
  - Example:
    ```bash
    curl -X POST "http://yourdomain.com/bugs/" -H "Content-Type: application/json" -d '{"title": "Bug Title", "description": "Bug Description", ...}'
    ```

- **Update Bug**:
  - `PUT /bugs/{bug_id}`
  - Description: Update the status or details of a specific bug identified by its ID.
  - Request Body: Updated BugData (Bug details to be modified).
  - Example:
    ```bash
    curl -X PUT "http://yourdomain.com/bugs/123" -H "Content-Type: application/json" -d '{"title": "New Bug Title", ...}'
    ```

- **Delete Bug**:
  - `DELETE /bugs/{bug_id}`
  - Description: Delete a bug by its ID from the system.
  - Example:
    ```bash
    curl -X DELETE "http://yourdomain.com/bugs/123"
    ```
The BugTracker app exposes the following API endpoints (if applicable):

- `POST /bugs`: Create a new bug report.
- `PUT /bugs/{bug_id}`: Update the status or information of a specific bug.
- `DELETE /bugs/{bug_id}`: Remove a bug from the system.
- Other endpoints related to authentication, user management (coming soon).




