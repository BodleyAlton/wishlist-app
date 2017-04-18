"""empty message

Revision ID: 2473b8f1fc99
Revises: 1cd4e5b01d0f
Create Date: 2017-04-17 19:23:13.004930

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2473b8f1fc99'
down_revision = '1cd4e5b01d0f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('wish_list', sa.Column('id', sa.Integer(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('wish_list', 'id')
    # ### end Alembic commands ###
