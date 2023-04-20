"""empty message

<<<<<<< HEAD:server/migrations/versions/49bba02c4d54_.py
Revision ID: 49bba02c4d54
Revises: 
Create Date: 2023-04-20 18:34:45.292205
=======
<<<<<<<< HEAD:server/migrations/versions/a03c6a76bb55_.py
Revision ID: a03c6a76bb55
Revises: 
Create Date: 2023-04-20 14:41:46.405060
========
Revision ID: e4a9b5e1451d
Revises: 
Create Date: 2023-04-20 11:16:39.660433
>>>>>>>> origin/Nick1:server/migrations/versions/e4a9b5e1451d_.py
>>>>>>> 2b8a9f8a946f8033d7d3de959c3f81f8daaddacc:server/migrations/versions/e4a9b5e1451d_.py

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
<<<<<<< HEAD:server/migrations/versions/49bba02c4d54_.py
revision = '49bba02c4d54'
=======
<<<<<<<< HEAD:server/migrations/versions/a03c6a76bb55_.py
revision = 'a03c6a76bb55'
========
revision = 'e4a9b5e1451d'
>>>>>>>> origin/Nick1:server/migrations/versions/e4a9b5e1451d_.py
>>>>>>> 2b8a9f8a946f8033d7d3de959c3f81f8daaddacc:server/migrations/versions/e4a9b5e1451d_.py
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('brands',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('brand', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('sizes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('size', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('types',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('type', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('email_address', sa.String(), nullable=True),
    sa.Column('paypal_address', sa.String(), nullable=True),
    sa.Column('zipcode', sa.Integer(), nullable=True),
    sa.Column('_password_hash', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('messages',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('message', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('user_1', sa.Integer(), nullable=True),
    sa.Column('user_2', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_2'], ['users.id'], name=op.f('fk_messages_user_2_users')),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('subtypes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('subtype', sa.String(), nullable=True),
    sa.Column('type_id', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['type_id'], ['types.id'], name=op.f('fk_subtypes_type_id_types')),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('items',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('condition', sa.Integer(), nullable=False),
    sa.Column('image', sa.String(), nullable=True),
    sa.Column('color', sa.String(), nullable=True),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('price', sa.Float(), nullable=True),
    sa.Column('for_sale', sa.Boolean(), nullable=True),
    sa.Column('owner_id', sa.Integer(), nullable=True),
    sa.Column('type_id', sa.Integer(), nullable=True),
    sa.Column('subtype_id', sa.Integer(), nullable=True),
    sa.Column('size_id', sa.Integer(), nullable=True),
    sa.Column('brand_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['brand_id'], ['brands.id'], name=op.f('fk_items_brand_id_brands')),
    sa.ForeignKeyConstraint(['owner_id'], ['users.id'], name=op.f('fk_items_owner_id_users')),
    sa.ForeignKeyConstraint(['size_id'], ['sizes.id'], name=op.f('fk_items_size_id_sizes')),
    sa.ForeignKeyConstraint(['subtype_id'], ['subtypes.id'], name=op.f('fk_items_subtype_id_subtypes')),
    sa.ForeignKeyConstraint(['type_id'], ['types.id'], name=op.f('fk_items_type_id_types')),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('favoriteitems',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('item_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['item_id'], ['items.id'], name=op.f('fk_favoriteitems_item_id_items')),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name=op.f('fk_favoriteitems_user_id_users')),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('transactions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('buyer_id', sa.Integer(), nullable=True),
    sa.Column('seller_id', sa.Integer(), nullable=True),
    sa.Column('price', sa.Float(), nullable=True),
    sa.Column('item_id', sa.Integer(), nullable=True),
    sa.Column('item_name', sa.String(), nullable=True),
    sa.Column('image', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['image'], ['items.image'], name=op.f('fk_transactions_image_items')),
    sa.ForeignKeyConstraint(['item_id'], ['items.id'], name=op.f('fk_transactions_item_id_items')),
    sa.ForeignKeyConstraint(['item_name'], ['items.name'], name=op.f('fk_transactions_item_name_items')),
    sa.ForeignKeyConstraint(['price'], ['items.price'], name=op.f('fk_transactions_price_items')),
    sa.ForeignKeyConstraint(['seller_id'], ['users.id'], name=op.f('fk_transactions_seller_id_users')),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('transactions')
    op.drop_table('favoriteitems')
    op.drop_table('items')
    op.drop_table('subtypes')
    op.drop_table('messages')
    op.drop_table('users')
    op.drop_table('types')
    op.drop_table('sizes')
    op.drop_table('brands')
    # ### end Alembic commands ###
