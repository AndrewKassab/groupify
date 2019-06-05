class AddVisability < ActiveRecord::Migration[5.2]
  def change
    add_column :group_users, :visible, :boolean, null: false, default: true
  end
end
