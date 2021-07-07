"""empty message

Revision ID: daba206749f8
Revises: 13170309d8bc
Create Date: 2021-07-07 13:52:43.134060

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'daba206749f8'
down_revision = '13170309d8bc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('rentals', sa.Column('total', sa.Float(), nullable=False))
    op.add_column('rentals', sa.Column('discont', sa.Float(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('rentals', 'discont')
    op.drop_column('rentals', 'total')
    # ### end Alembic commands ###