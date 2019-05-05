# This file is auto-generated from the current state of the database. Instead
# of editing this file, please use the migrations feature of Active Record to
# incrementally modify your database, and then regenerate this schema definition.
#
# Note that this schema.rb definition is the authoritative source for your
# database schema. If you need to create the application database on another
# system, you should be using db:schema:load, not running all the migrations
# from scratch. The latter is a flawed and unsustainable approach (the more migrations
# you'll amass, the slower it'll run and the greater likelihood for issues).
#
# It's strongly recommended that you check this file into your version control system.

ActiveRecord::Schema.define(version: 2019_05_04_085846) do

  # These are extensions that must be enabled in order to support this database
  enable_extension "plpgsql"

  create_table "artists", force: :cascade do |t|
    t.string "name"
    t.string "spotify_id"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.index ["spotify_id"], name: "index_artists_on_spotify_id"
  end

  create_table "genres", force: :cascade do |t|
    t.string "name"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.index ["name"], name: "index_genres_on_name"
  end

  create_table "group_spotify_accounts", force: :cascade do |t|
    t.integer "group_id", null: false
    t.integer "spotify_account_id", null: false
    t.index ["group_id"], name: "index_group_spotify_accounts_on_group_id"
    t.index ["spotify_account_id"], name: "index_group_spotify_accounts_on_spotify_account_id"
  end

  create_table "group_tracks", force: :cascade do |t|
    t.integer "group_id", null: false
    t.integer "track_id", null: false
    t.integer "rank", default: 0
    t.index ["group_id"], name: "index_group_tracks_on_group_id"
    t.index ["track_id"], name: "index_group_tracks_on_track_id"
  end

  create_table "groups", force: :cascade do |t|
    t.integer "user_id", null: false
    t.string "title", null: false
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.index ["user_id"], name: "index_groups_on_user_id"
  end

  create_table "spotify_accounts", force: :cascade do |t|
    t.integer "user_id"
    t.string "username", null: false
    t.string "spotify_id", null: false
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.index ["spotify_id"], name: "index_spotify_accounts_on_spotify_id"
    t.index ["user_id"], name: "index_spotify_accounts_on_user_id"
    t.index ["username"], name: "index_spotify_accounts_on_username"
  end

  create_table "spotify_playlists", force: :cascade do |t|
    t.integer "group_id", null: false
    t.integer "user_id", null: false
    t.string "spotify_id"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.index ["group_id"], name: "index_spotify_playlists_on_group_id"
    t.index ["user_id"], name: "index_spotify_playlists_on_user_id"
  end

  create_table "track_artists", force: :cascade do |t|
    t.integer "track_id"
    t.integer "artist_id"
    t.index ["artist_id"], name: "index_track_artists_on_artist_id"
    t.index ["track_id"], name: "index_track_artists_on_track_id"
  end

  create_table "track_genres", force: :cascade do |t|
    t.integer "track_id", null: false
    t.integer "genre_id", null: false
    t.index ["genre_id"], name: "index_track_genres_on_genre_id"
    t.index ["track_id"], name: "index_track_genres_on_track_id"
  end

  create_table "tracks", force: :cascade do |t|
    t.string "name"
    t.integer "duration"
    t.string "spotify_id"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.index ["name"], name: "index_tracks_on_name"
    t.index ["spotify_id"], name: "index_tracks_on_spotify_id"
  end

  create_table "user_genres", force: :cascade do |t|
    t.integer "user_id", null: false
    t.integer "genre_id", null: false
    t.index ["genre_id"], name: "index_user_genres_on_genre_id"
    t.index ["user_id"], name: "index_user_genres_on_user_id"
  end

  create_table "users", force: :cascade do |t|
    t.string "email", null: false
    t.string "name", null: false
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
  end

  add_foreign_key "group_spotify_accounts", "groups"
  add_foreign_key "group_spotify_accounts", "spotify_accounts"
  add_foreign_key "group_tracks", "groups"
  add_foreign_key "group_tracks", "tracks"
  add_foreign_key "groups", "users"
  add_foreign_key "spotify_accounts", "users"
  add_foreign_key "spotify_playlists", "groups"
  add_foreign_key "spotify_playlists", "users"
  add_foreign_key "track_artists", "artists"
  add_foreign_key "track_artists", "tracks"
  add_foreign_key "track_genres", "genres"
  add_foreign_key "track_genres", "tracks"
  add_foreign_key "user_genres", "genres"
  add_foreign_key "user_genres", "users"
end
