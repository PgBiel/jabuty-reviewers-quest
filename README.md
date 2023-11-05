# jabuty-reviewers-quest
Reviewer's Quest (Jabuty's project)

## Building the frontend

1. Ensure you have `npm` installed
2. `cd frontend` (go to the `frontend` folder)
3. Run `npm install` once to install dependencies
4. Run `npm run build`

## Running the backend

1. Install `poetry`, e.g. through `pipx install poetry`
2. Run `poetry install --with dev --sync` to install dependencies (`--with dev` is optional; required for linting & formatting)
2. Run `poetry run app` in the root of the project

## Checking your code

- For the frontend: after installing (dev) dependencies, run:
    1. `npm run lint` to lint your code and check formatting
        - If there are errors (such as formatting errors), run `npm run fix` to fix them.
    2. `npm run build` to check if the frontend builds
- For the backend: after installing (dev) dependencies, run:
    1. `poetry run format` to format your code (add `--check` to just check if it's formatted or not)
    2. `poetry run check` to lint your code
