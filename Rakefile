require "bundler/setup"
require "dotenv/load"

require 'standalone_migrations'

ActiveRecord::Base.schema_format = :sql
StandaloneMigrations::Tasks.load_tasks

namespace :db do
  namespace :schema do
    task :copy => ["db:schema:dump"] do
      cp 'db/structure.sql', 'db/schema.rb', verbose: false
    end
  end
end

Rake::Task["db:structure:dump"].enhance(["db:schema:copy"])

puts "loaded rake"
