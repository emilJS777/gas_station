"""asdad

Revision ID: dc773f55cdc1
Revises: 8a55cfc10929
Create Date: 2022-03-18 16:08:24.260550

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dc773f55cdc1'
down_revision = '8a55cfc10929'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('device', sa.Column('cash_box_id', sa.Integer(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('device', 'cash_box_id')
    # ### end Alembic commands ###
