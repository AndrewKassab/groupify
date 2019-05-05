class AddIndices < ActiveRecord::Migration[5.2]
  def change

    add_foreign_key :spotify_accounts, :users

    add_foreign_key :group_spotify_accounts, :groups
    add_foreign_key :group_spotify_accounts, :spotify_accounts

    add_foreign_key :groups, :users

    add_foreign_key :user_genres, :users
    add_foreign_key :user_genres, :genres

    add_foreign_key :group_tracks, :groups
    add_foreign_key :group_tracks, :tracks

    add_foreign_key :track_artists, :tracks
    add_foreign_key :track_artists, :artists

    add_foreign_key :spotify_playlists, :users
    add_foreign_key :spotify_playlists, :groups
  end
end
