"""empty message

Revision ID: e01ffb2d5ead
Revises: 04fd16b7f599
Create Date: 2023-01-26 21:14:00.879323

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e01ffb2d5ead'
down_revision = '04fd16b7f599'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('employees', schema=None) as batch_op:
        batch_op.add_column(sa.Column('hire_date', sa.String(length=10), nullable=True))
        batch_op.drop_column('entry_date')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('employees', schema=None) as batch_op:
        batch_op.add_column(sa.Column('entry_date', sa.VARCHAR(length=10), nullable=True))
        batch_op.drop_column('hire_date')

    # ### end Alembic commands ###
