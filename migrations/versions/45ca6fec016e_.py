"""empty message

Revision ID: 45ca6fec016e
Revises: 889c4c0a76d1
Create Date: 2023-01-26 22:24:59.220630

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '45ca6fec016e'
down_revision = '889c4c0a76d1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('employees', schema=None) as batch_op:
        batch_op.add_column(sa.Column('password_hash', sa.LargeBinary(length=128), nullable=True))
        batch_op.drop_column('password')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('employees', schema=None) as batch_op:
        batch_op.add_column(sa.Column('password', sa.VARCHAR(length=50), nullable=True))
        batch_op.drop_column('password_hash')

    # ### end Alembic commands ###