"""add_user_create_in_patient_table

Revision ID: d391eac496a7
Revises: 2b56ca5a4b40
Create Date: 2022-02-23 21:06:17.344913

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd391eac496a7'
down_revision = '2b56ca5a4b40'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('patients', sa.Column('user_create_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'patients', 'users', ['user_create_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'patients', type_='foreignkey')
    op.drop_column('patients', 'user_create_id')
    # ### end Alembic commands ###
