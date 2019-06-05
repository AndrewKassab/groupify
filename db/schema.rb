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

ActiveRecord::Schema.define(version: 2019_06_04_235212) do

  # These are extensions that must be enabled in order to support this database
  enable_extension "plpgsql"

  create_table "auth_tokens", force: :cascade do |t|
    t.integer "user_id", null: false
    t.string "token", null: false
    t.index ["token"], name: "index_auth_tokens_on_token"
    t.index ["user_id"], name: "index_auth_tokens_on_user_id"
  end

  create_table "group_users", force: :cascade do |t|
    t.integer "group_id", null: false
    t.integer "user_id", null: false
    t.boolean "visible", default: true, null: false
    t.index ["group_id", "user_id"], name: "index_group_users_on_group_id_and_user_id", unique: true
    t.index ["user_id"], name: "index_group_users_on_user_id"
  end

  create_table "groups", force: :cascade do |t|
    t.integer "user_id", null: false
    t.string "title", null: false
    t.index ["user_id"], name: "index_groups_on_user_id"
  end

  create_table "spotify_playlists", force: :cascade do |t|
    t.integer "group_id", null: false
    t.integer "user_id", null: false
    t.string "spotify_id"
    t.index ["group_id"], name: "index_spotify_playlists_on_group_id"
    t.index ["user_id"], name: "index_spotify_playlists_on_user_id"
  end

  create_table "tracks", force: :cascade do |t|
    t.string "name"
    t.integer "duration"
    t.string "spotify_id"
    t.integer "group_id"
    t.integer "rank"
    t.string "artists"
    t.index ["name"], name: "index_tracks_on_name"
    t.index ["spotify_id"], name: "index_tracks_on_spotify_id"
  end

  create_table "users", force: :cascade do |t|
    t.string "name", null: false
    t.string "spotify_id"
    t.string "access_token"
    t.string "refresh_token"
    t.datetime "token_expiration"
    t.string "username"
  end

  add_foreign_key "auth_tokens", "users"
  add_foreign_key "group_users", "groups"
  add_foreign_key "group_users", "users"
  add_foreign_key "groups", "users"
  add_foreign_key "spotify_playlists", "groups"
  add_foreign_key "spotify_playlists", "users"
end
