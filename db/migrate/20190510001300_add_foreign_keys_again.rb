class AddForeignKeysAgain < ActiveRecord::Migration[5.2]
  def change
    add_foreign_key :auth_tokens, :users
    add_foreign_key :group_users, :groups
    add_foreign_key :group_users, :users

  end
end
