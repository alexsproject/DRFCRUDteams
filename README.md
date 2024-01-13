# Django REST API for Team Management
This project is a RESTful API developed with Django REST Framework. It's designed to manage teams and the people within these teams, providing functionalities to CRUD teams and members.

## Features
- CRUD operations for teams and members.
- Association of members with teams.
- RESTful endpoints for team and member management.

## Getting Started

### Prerequisites
Ensure you have the following installed on your system:

- Python 3.x
- pip (Python package manager)
- Poetry (Dependency management tool)

### Installation
1. Clone the repository
```bash
git clone https://github.com/alexsproject/DRFCRUDteams.git
cd DRFCRUDteams
```
2. Set up a virtual environment
```bash
poetry install
```
3. Create and apply migrations
```bash
poetry run python manage.py makemigrations
poetry run python manage.py migrate
```
4. Create a superuser
```bash
poetry run python manage.py createsuperuser
```
Follow the prompts to create an admin account.

### Running the Server
Start the Django server using:
```bash
poetry run python manage.py runserver
```
The API will be available at http://127.0.0.1:8000/.

## API Endpoints
### Teams
- List Teams: GET /api/teams/
- Create Team: POST /api/teams/
- Retrieve Team: GET /api/teams/{id}/
- Update Team: PUT /api/teams/{id}/
- Partial Update Team: PATCH /api/teams/{id}/
- Delete Team: DELETE /api/teams/{id}/

### Members
- List Members: GET /api/people/
- Create Member: POST /api/people/
- Retrieve Member: GET /api/people/{id}/
- Update Member: PUT /api/people/{id}/
- Partial Update Member: PATCH /api/people/{id}/
- Delete Member: DELETE /api/people/{id}/

## Admin Interface
Access the Django admin interface at http://127.0.0.1:8000/admin/ using the superuser credentials created earlier.

### License
This project is licensed under the MIT License.