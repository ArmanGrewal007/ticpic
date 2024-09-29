# Notes for myself

1. Create `pyproject.toml`
2. Python version is `3.10.0` `python -m venv venv`
3. `source venv/bin/activate`
3. `pip install poetry`
4. `Create flask_api and app.py`

## Adding Users and Roles
1. Need to setup the DB and roles
    - `flask db init`
    - `flask db migrate -m "Initial migration"`
    - `flask db upgrade`
    - `flask shell`
    ```python
    from app import user_datastore, db
    user_datastore.create_role(name="Admin", description="Administrator role")
    user_datastore.create_role(name="User", description="Regular user role")
    db.session.commit()
    ```
2.

