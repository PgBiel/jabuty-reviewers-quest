# jabuty-reviewers-quest
Reviewer's Quest (Jabuty's project)

## Building the frontend

1. Ensure you have `npm` installed
2. `cd frontend` (go to the `frontend` folder)
3. Run `npm install` once to install dependencies
4. Run `npm run build`

## Running the backend

1. Make sure you have Python **3.11** installed
2. Install `poetry` **1.7.0**, e.g. through `pipx install poetry==1.7.0`

     - If you do not have `pipx` / would not like to install it, you can do it as follows:
       1. Use `python -m venv .venv` to create a virtual environment
       2. Run `source .venv/bin/activate` to activate it
       3. Run `pip install -U pip setuptools` to update pip
       4. Run `pip install poetry==1.7.0` to install `poetry` with the correct version
3. Run `poetry install --with dev --sync` to install dependencies (`--with dev` is optional; required for linting & formatting)
4. Ensure the database exists and was initialized with the name `database.db`

   - If it does not exist, use `poetry run regendb` to create it **(CAUTION: THAT COMMAND DELETES THE EXISTING DATABASE! DO NOT USE IN PRODUCTION!)**
   - The same command can be used to update the database after a model change **(but heed the warning above)**.

5. Run `poetry run app` in the root of the project to start the app.

### Populating the database with sample data

Run `poetry run populatedb` after the database has been created (see above) to populate the database with sample data,
including sample games, users and reviews.

### A note on the database's location

For `poetry run app`, `poetry run regendb` and `poetry run populatedb`, you can specify the environment variable
`JABRQ_DATABASE=/some/path.db` to override where the app will look for / create `database.db` (by default, it's at the
same directory at which you run the command in question).

For instance, running the command below will
run the app assuming the database is located
at your Downloads directory, assuming you use Linux.

```shell
JABRQ_DATABASE=$HOME/Downloads/database.db poetry run app
```

## Checking your code

- For the frontend: after installing (dev) dependencies, run:
    1. `npm run lint` to lint your code and check formatting
        - If there are errors (such as formatting errors), run `npm run fix` to fix them.
    2. `npm run build` to check if the frontend builds
- For the backend: after installing (dev) dependencies, run:
    1. `poetry run format` to format your code (add `--check` to just check if it's formatted or not)
    2. `poetry run check` to lint your code (add `--fix` to automatically fix fixable problems)
    3. `poetry run typecheck` to check your code for type errors **(EXPERIMENTAL)**
        - **NOTE:** This last step is still experimental and not currently checked in CI. Don't worry too much if you
            get errors on `typecheck`, but make sure to warn others about it if you do and can't fix them.
