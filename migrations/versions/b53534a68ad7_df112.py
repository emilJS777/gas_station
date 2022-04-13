"""df112

Revision ID: b53534a68ad7
Revises: cc22036d5769
Create Date: 2022-04-13 12:19:27.768472

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'b53534a68ad7'
down_revision = 'cc22036d5769'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('device_set', 'master_flow_auto')
    op.drop_column('device_set', 'flow_hanac_set')
    op.drop_column('device_set', 'press_gorcakic_set')
    op.drop_column('device_set', 'flow_auto_set')
    op.drop_column('device_set', 'flow_max_set')
    op.drop_column('device_set', 'dp_gorcakic_set')
    op.drop_column('device_set', 'k_gorcakic_set')
    op.drop_column('device_set', 'flow_auto_on_off')
    op.drop_column('device_set', 'flow_proc_set')
    op.drop_column('device_set', 'onoff')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('device_set', sa.Column('onoff', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True))
    op.add_column('device_set', sa.Column('flow_proc_set', mysql.VARCHAR(length=8), nullable=True))
    op.add_column('device_set', sa.Column('flow_auto_on_off', mysql.VARCHAR(length=8), nullable=True))
    op.add_column('device_set', sa.Column('k_gorcakic_set', mysql.VARCHAR(length=8), nullable=True))
    op.add_column('device_set', sa.Column('dp_gorcakic_set', mysql.VARCHAR(length=8), nullable=True))
    op.add_column('device_set', sa.Column('flow_max_set', mysql.VARCHAR(length=8), nullable=True))
    op.add_column('device_set', sa.Column('flow_auto_set', mysql.VARCHAR(length=8), nullable=True))
    op.add_column('device_set', sa.Column('press_gorcakic_set', mysql.VARCHAR(length=8), nullable=True))
    op.add_column('device_set', sa.Column('flow_hanac_set', mysql.VARCHAR(length=8), nullable=True))
    op.add_column('device_set', sa.Column('master_flow_auto', mysql.VARCHAR(length=8), nullable=True))
    # ### end Alembic commands ###
