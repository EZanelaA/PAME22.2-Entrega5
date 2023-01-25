"""empty message

Revision ID: 803ad6c4ba0c
Revises: e716e30fbd73
Create Date: 2023-01-25 14:36:57.412223

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '803ad6c4ba0c'
down_revision = 'e716e30fbd73'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Employees', schema=None) as batch_op:
        batch_op.alter_column('entry_date',
               existing_type=sa.DATETIME(),
               type_=sa.String(length=10),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Employees', schema=None) as batch_op:
        batch_op.alter_column('entry_date',
               existing_type=sa.String(length=10),
               type_=sa.DATETIME(),
               existing_nullable=True)

    # ### end Alembic commands ###