"""empty message

Revision ID: c64cf494e7b0
Revises: 16bf25817800
Create Date: 2019-04-02 11:26:36.792166

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c64cf494e7b0'
down_revision = '16bf25817800'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'city')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('city', sa.VARCHAR(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
