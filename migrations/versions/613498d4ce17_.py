"""empty message

Revision ID: 613498d4ce17
Revises: f4c67100b5a6
Create Date: 2023-01-26 16:42:11.230456

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '613498d4ce17'
down_revision = 'f4c67100b5a6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('requests')
    with op.batch_alter_table('employees', schema=None) as batch_op:
        batch_op.add_column(sa.Column('password_hash', sa.LargeBinary(length=128), nullable=True))
        batch_op.drop_column('password')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('employees', schema=None) as batch_op:
        batch_op.add_column(sa.Column('password', sa.VARCHAR(), nullable=True))
        batch_op.drop_column('password_hash')

    op.create_table('requests',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###