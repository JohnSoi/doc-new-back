"""add_patient_table

Revision ID: 28539e34c2ef
Revises: c811ccc19a7b
Create Date: 2022-02-06 20:35:34.540549

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '28539e34c2ef'
down_revision = 'c811ccc19a7b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('patients',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('uuid', sa.Text(), nullable=True),
    sa.Column('name', sa.Text(), nullable=False),
    sa.Column('surname', sa.Text(), nullable=False),
    sa.Column('second_name', sa.Text(), nullable=False),
    sa.Column('telephone', sa.Text(), nullable=False),
    sa.Column('email', sa.Text(), nullable=True),
    sa.Column('doctor_id', sa.Integer(), nullable=True),
    sa.Column('ward', sa.Text(), nullable=True),
    sa.Column('discription', sa.Text(), nullable=True),
    sa.Column('comment', sa.Text(), nullable=True),
    sa.Column('type', sa.Integer(), nullable=True),
    sa.Column('num_card', sa.Integer(), nullable=True),
    sa.Column('date_birthday', sa.Date(), nullable=True),
    sa.Column('date_create', sa.Date(), nullable=True),
    sa.Column('date_update', sa.Date(), nullable=True),
    sa.Column('date_delete', sa.Date(), nullable=True),
    sa.Column('date_discharge', sa.Date(), nullable=True),
    sa.Column('date_receipt', sa.Date(), nullable=True),
    sa.ForeignKeyConstraint(['doctor_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('uuid')
    )
    op.create_index(op.f('ix_patients_email'), 'patients', ['email'], unique=False)
    op.create_index(op.f('ix_patients_name'), 'patients', ['name'], unique=False)
    op.create_index(op.f('ix_patients_second_name'), 'patients', ['second_name'], unique=False)
    op.create_index(op.f('ix_patients_surname'), 'patients', ['surname'], unique=False)
    op.create_index(op.f('ix_patients_telephone'), 'patients', ['telephone'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_patients_telephone'), table_name='patients')
    op.drop_index(op.f('ix_patients_surname'), table_name='patients')
    op.drop_index(op.f('ix_patients_second_name'), table_name='patients')
    op.drop_index(op.f('ix_patients_name'), table_name='patients')
    op.drop_index(op.f('ix_patients_email'), table_name='patients')
    op.drop_table('patients')
    # ### end Alembic commands ###
