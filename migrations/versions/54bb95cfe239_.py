"""empty message

Revision ID: 54bb95cfe239
Revises: 723e0138d4ca
Create Date: 2023-01-25 15:52:53.810504

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '54bb95cfe239'
down_revision = '723e0138d4ca'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Employees', schema=None) as batch_op:
        batch_op.alter_column('username',
               existing_type=sa.VARCHAR(length=50),
               type_=sa.Date(),
               existing_nullable=True)
        batch_op.alter_column('entry_date',
               existing_type=sa.VARCHAR(length=10),
               type_=sa.Date(),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Employees', schema=None) as batch_op:
        batch_op.alter_column('entry_date',
               existing_type=sa.Date(),
               type_=sa.VARCHAR(length=10),
               existing_nullable=True)
        batch_op.alter_column('username',
               existing_type=sa.Date(),
               type_=sa.VARCHAR(length=50),
               existing_nullable=True)

    # ### end Alembic commands ###