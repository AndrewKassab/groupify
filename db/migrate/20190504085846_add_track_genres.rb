class AddTrackGenres < ActiveRecord::Migration[5.2]
  def change
    create_table :track_genres do |t|
      t.integer :track_id, index: true, null: false
      t.integer :genre_id, index: true, null: false
    end

    add_foreign_key :track_genres, :tracks
    add_foreign_key :track_genres, :genres
  end
end
