# Groupify

## Installation

The app is designed to be installed/run through [Docker](https://docs.docker.com/).
This has been done to simplify setup and make the application essentialy platform
agnostic (read: I don't care if you're on linux, windows, mac, haiku, or something
else. If youcan run docker, you can run this app in development.)

### Docker setup

Before anything, you need to install Docker [following their install instruction](https://docs.docker.com/install/#supported-platforms).

After installing Docker, you also need to install Docker Compose so that you can
boot the app all at once. Install instructions are [here](https://docs.docker.com/compose/install/). (Note: If you are on Mac or Windows, this is already included with
Docker Desktop, so this step is pretty much only needed for linux users.)

On first startup, from the root folder, you need to run `docker-compose build`.
This will compile all the base images.

### Running the application

To actually run the application, in a terminal window run:

```bash
docker-compose up
```

This will start all the necessary services (React, Postgres, Python) as well as
automatically applying the latest database migrations (if any are pending). After
this, the app can be accessed at [http://localhost:3000](http://localhost:3000).
Any changes to react files will automatically get reloaded in the browser
(it should also be possible to get the backend to so this same _hot_ reloading).

### Restart Scenarios

Most of the time, the application is perfectly fine and will automatically update
the frontend/backend without a restart. There are a few scenarios that do actually
require a restart of the app though.

- New package added to Yarn `package.json` for react. This requires restarting
`docker-compose up`.
- New package added to Python `requirements.txt` for the backend. This requires
rebuilding python with `docker-compose build python` and then restarting with
`docker-compose up`.
- Database migrations added. This requires restarting `docker-compose up`.
- Edits to anything outside of `src/` or `app/` will also generally require
restarting `docker-compose up` for changes to take effect.

## Best practices

Number one priority here, "No religious wars". That said, there's some clear
considerations that should be made.

### Python

Python code should conform with best practices. For reference, Python has the
**really** well defined [PEP 8](https://www.python.org/dev/peps/pep-0008/)
style guide. We should follow this. Paramount here is following naming
conventions, etc.

### React/Frontend

Frontend has access to `eslint` using the Airbnb ruleset. This generally makes
us write better code to keep things tidy. We've already cleaned up the rules a
bit, though some still need more looking into. At the very least, it serves as a
good guideline and can autofix some of the more egregious errors (missing
semicolons, bad indentation, etc.). To run from outside of docker, use `yarn lint-docker`.

### Code style

All python code should use 4 space indentation. Other code should use 2 space
indentation. There should always be one empty newline at the end of the file
and no trailing whitespace. This can be automatically set in your editor using
[Editorconfig](https://editorconfig.org/) (just a case of adding or enabling a
package to Atom/VS Code/IntelliJ/PyCharm/Textmate etc.)

## TODOs

1. Possibly install `pylint` to keep the backend code tidy
2. Enfocing `eslint` usage and getting that ruleset working to keep frontend in line