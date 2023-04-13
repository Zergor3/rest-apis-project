"""empty message

Revision ID: 7ae48df338d2
Revises: bb5da1e68550
Create Date: 2022-10-14 11:27:41.795824

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7ae48df338d2'
down_revision = 'bb5da1e68550'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('email', sa.String(), nullable=False))
    op.create_unique_constraint("email", 'users', ['email'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint("email", 'users', type_='unique')
    op.drop_column('users', 'email')
    # ### end Alembic commands ###