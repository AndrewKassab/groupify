# Groupify
> Create group playlists that everyone will love

![Groupify Image Logo](https://github.com/AndrewKassab/groupify/blob/master/src/images/logo.svg)

This application uses the Spotify API to retrieve information about a user's
playlists and most listened tracks. It then allows a user to combine multiple people's 
listening preferences to generate a new playlist.

[Try out Groupify](https://www.groupify.winstondurand.com) 

# Spotify API

Application takes advantage of the following parts of the Spotify API:
- [Authorization](https://developer.spotify.com/documentation/general/guides/authorization-guide/#implicit-grant-flow)
- [Get users Top Tracks](https://developer.spotify.com/documentation/web-api/reference/personalization/get-users-top-artists-and-tracks/)
- [Get users Playlists](https://developer.spotify.com/documentation/web-api/reference/playlists/get-list-users-playlists/)
- [Create a Playlist](https://developer.spotify.com/documentation/web-api/reference/playlists/create-playlist/)
- [Add tracks to a playlist](https://developer.spotify.com/documentation/web-api/reference/playlists/add-tracks-to-playlist/)

Application uses spotipy on the backend to connect with the API.

# Development Set Up

The app is designed to be installed/run through [Docker](https://docs.docker.com/).

Install docker [following their install instructions](https://docs.docker.com/install/)

For Linux users, after installing Docker you must also install docker-compose separately following the instructions found [here](https://docs.docker.com/compose/install/). (Mac and Windows users should already have docker-compose included with Docker Desktop.)

# Start Up

On first startup, from the root folder run:
```bash
docker-compose build
```

# Running the application

To run the application, in a terminal window run: 

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

# TODO
