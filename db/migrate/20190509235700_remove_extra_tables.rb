class RemoveExtraTables < ActiveRecord::Migration[5.2]
  def change
    drop_table :user_genres
    drop_table :track_genres
    drop_table :genres
    drop_table :group_spotify_accounts
    drop_table :spotify_accounts

    create_table :group_users do |t|
      t.integer :group_id, null: false
      t.integer :user_id, null: false, index: true
      t.index [:group_id, :user_id], unique: true
    end

    create_table :auth_tokens do |t|
      t.integer :user_id, null: false, index: true
      t.string :token, null: false, index: true
    end

    add_column :users, :spotify_id, :string
    add_column :users, :access_token, :string
    add_column :users, :refresh_token, :string
    add_column :users, :token_expiration, :datetime

    remove_column :users, :email

    remove_column :users, :created_at
    remove_column :users, :updated_at

    remove_column :groups, :created_at
    remove_column :groups, :updated_at

    remove_column :tracks, :created_at
    remove_column :tracks, :updated_at

    remove_column :spotify_playlists, :created_at
    remove_column :spotify_playlists, :updated_at
  end
end
