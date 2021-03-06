"""add_service_table

Revision ID: 1488ac3708c1
Revises: 4ad5007ea167
Create Date: 2022-02-08 20:16:45.274652

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1488ac3708c1'
down_revision = '4ad5007ea167'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('services',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Text(), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.Column('bonus_work', sa.Integer(), nullable=True),
    sa.Column('is_bonus_work_percent', sa.Boolean(), nullable=True),
    sa.Column('bonus_add', sa.Integer(), nullable=True),
    sa.Column('is_bonus_add_percent', sa.Boolean(), nullable=True),
    sa.Column('date_create', sa.DateTime(), nullable=True),
    sa.Column('date_update', sa.DateTime(), nullable=True),
    sa.Column('date_delete', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_services_name'), 'services', ['name'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_services_name'), table_name='services')
    op.drop_table('services')
    # ### end Alembic commands ###
