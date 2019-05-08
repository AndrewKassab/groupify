class SimplifyTracks < ActiveRecord::Migration[5.2]
  def change
    remove_foreign_key :group_tracks, :groups
    remove_foreign_key :group_tracks, :tracks

    remove_foreign_key :track_artists, :artists
    remove_foreign_key :track_artists, :tracks

    drop_table :group_tracks
    drop_table :track_artists
    drop_table :artists

    add_column :tracks, :group_id, :integer, index: true
    add_column :tracks, :rank, :integer
    add_column :tracks, :artists, :string
  end
end
