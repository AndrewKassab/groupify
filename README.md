# Groupify

## Installation

Different parts of this application run using different programs.

TODO: Setup a Procfile/Docker compose to run everything at once

### Frontend (React)

The frontend is written in react and uses the Yarn package manager to run/install.

```bash
# Install Node
# Mac:
brew install node # etc.

# Yarn:
npm install -g yarn

# Install dependencies
yarn install

# Start dev server
yarn start
```

### Database

Migrations for the app are tracked using the Standalone Migrations gem to utilize
Rails ActiveRecord migrations.

```bash
# Ruby install
brew install rbenv ruby-build
rbenv install 2.6.3

bundle install
```

The database assumes we are using Postgres, and can be migrated with `rake db:migrate`
