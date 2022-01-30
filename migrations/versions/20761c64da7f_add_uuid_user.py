"""add_uuid_user

Revision ID: 20761c64da7f
Revises: 623a53b549c5
Create Date: 2022-01-29 18:21:00.943861

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '20761c64da7f'
down_revision = '623a53b549c5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('uuid', sa.Text(), nullable=True))
    op.create_unique_constraint(None, 'users', ['uuid'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='unique')
    op.drop_column('users', 'uuid')
    # ### end Alembic commands ###
