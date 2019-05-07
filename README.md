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
This will compile all the assets needed