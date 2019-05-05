class CreateUsers < ActiveRecord::Migration[5.2]
  def change
    create_table :users do |t|
      t.string :email, null: false
      t.string :name, null: false

      t.timestamps
    end

    create_table :spotify_accounts do |t|
      t.integer :user_id, index: true, unique: true

      t.string :username, index: true, unique: true, null: false
      t.string :spotify_id, index: true, unique: true, null: false

      t.timestamps
    end

    create_table :group_spotify_accounts do |t|
      t.integer :group_id, index: true, null: false
      t.integer :spotify_account_id, index: true, null: false
    end

    create_table :groups do |t|
      t.integer :user_id, index: true, null: false
      t.string :title, null: false

      t.timestamps
    end

    create_table :user_genres do |t|
      t.integer :user_id, index: true, null: false
      t.integer :genre_id, index: true, null: false
    end

    create_table :genres do |t|
      t.string :name, index: true, unique: true

      t.timestamps
    end

    create_table :tracks do |t|
      t.string :name, index: true
      t.integer :duration # represented in seconds

      t.string :spotify_id, index: true, unique: true

      t.timestamps
    end

    create_table :group_tracks do |t|
      t.integer :group_id, index: true, null: false
      t.integer :track_id, index: true, null: false
      t.integer :rank, default: 0
    end

    create_table :track_artists do |t|
      t.integer :track_id, index: true
      t.integer :artist_id, index: true
    end

    create_table :artists do |t|
      t.string :name
      t.string :spotify_id, index: true, unique: true

      t.timestamps
    end

    create_table :spotify_playlists do |t|
      t.integer :group_id, index: true, null: false
      t.integer :user_id, index: true, null: false
      t.string :spotify_id

      t.timestamps
    end
  end
end
