# AI_NOTES

# AI Usage Report

## Overview

I used ChatGPT as a learning and development assistant while building this project. The AI helped me understand FastAPI, REST API development, project structure, testing, and Git/GitHub. I implemented the project step by step, verified the outputs, and made changes whenever necessary.

---

## Parts Written by Me

The following work was completed by me during the development of the project:

- Created the project folder structure.
- Created the Python virtual environment.
- Installed all required dependencies.
- Created the required files and folders.
- Ran the FastAPI server and verified that it started successfully.
- Created and maintained the JSON file used to store expenses.
- Tested every API endpoint using Swagger UI.
- Ran all unit tests using Pytest until all tests passed.
- Fixed environment issues related to Python version compatibility.
- Configured Git and pushed the project to GitHub.
- Added project documentation files and organized the repository.

---

## Where I Used AI Assistance

I used ChatGPT to help with the following tasks:

### Project Setup

- Understanding the recommended FastAPI project structure.
- Explaining how each file should be organized.
- Explaining how FastAPI applications are structured.

### API Development

ChatGPT helped generate the initial implementation of:

- Expense model (Pydantic model)
- Add Expense endpoint
- View All Expenses endpoint
- Filter Expenses endpoint
- Total Expenses endpoint
- Delete Expense endpoint
- JSON file read/write helper functions

### Testing

ChatGPT helped generate:

- Initial Pytest test cases
- Test for adding an expense
- Test for retrieving expenses
- Test for filtering expenses

### Documentation

ChatGPT assisted in creating:

- README.md
- AI_NOTES.md
- API endpoint descriptions
- Installation instructions
- Testing instructions

### Git & GitHub

ChatGPT guided me through:

- Git initialization
- Creating commits
- Connecting the local repository to GitHub
- Resolving Git push issues
- Removing unnecessary files from version control

---

## Code I Reviewed and Modified

Although ChatGPT generated parts of the initial code, I reviewed and validated everything before keeping it.

I personally:

- Verified every endpoint using Swagger UI.
- Corrected import errors during development.
- Fixed project structure issues.
- Updated HTTP status codes where appropriate.
- Added endpoint summaries for better Swagger documentation.
- Added additional test cases.
- Ensured all tests passed successfully before submission.

---

## AI Suggestions I Did Not Use

Some suggestions provided by ChatGPT were intentionally not included because they were outside the assignment scope.

These include:

- Database integration (SQLite/PostgreSQL)
- User authentication
- User accounts
- JWT authentication
- Advanced logging
- Deployment to cloud services

The assignment specifically allowed storing data in a JSON file, so I kept the implementation simple and focused on the required functionality.

---

## Validation Process

To ensure the project worked correctly, I performed the following checks:

- Tested every endpoint through Swagger UI.
- Verified that expenses were correctly stored in the JSON file.
- Verified filtering by category.
- Verified total expense calculation.
- Verified deleting expenses.
- Executed the complete Pytest suite.
- Confirmed that all tests passed successfully.

Final test result:

```
4 passed
```

---

## Reflection

Using ChatGPT helped me understand FastAPI development much better. Rather than copying code without understanding it, I followed the implementation step by step, tested each feature, fixed errors as they appeared, and learned how the different components of a FastAPI project work together.
