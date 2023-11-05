# jabuty-reviewers-quest
Reviewer's Quest (Jabuty's project)

## Building the frontend

1. Ensure you have `npm` installed
2. `cd frontend && npm run build`

## Running the backend

1. Install `poetry`, e.g. through `pipx install poetry`
2. Run `poetry install --with dev --sync` to install dependencies (`--with dev` is optional; required for linting & formatting)
2. Run `poetry run app` in the root of the project

## Checking your code

- For the backend: after installing (dev) dependencies, run:
    1. `poetry run ruff format reviewers_quest` to format your code (use `--check` to just check if it's formatted)
    2. `poetry run ruff check reviewers_quest` to lint your code
