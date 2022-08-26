"""followed_stocks table

Revision ID: 676269e057a9
Revises: a9e8b30379ba
Create Date: 2022-08-20 17:42:23.943994

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '676269e057a9'
down_revision = 'a9e8b30379ba'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('followed_stocks',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('stock_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['stock_id'], ['stock.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('user_id', 'stock_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('followed_stocks')
    # ### end Alembic commands ###