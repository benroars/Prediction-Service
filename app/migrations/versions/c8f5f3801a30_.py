"""empty message

Revision ID: c8f5f3801a30
Revises: None
Create Date: 2016-06-29 16:25:56.666570

"""

# revision identifiers, used by Alembic.
revision = 'c8f5f3801a30'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('activities',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date', sa.Date(), nullable=True),
    sa.Column('steps', sa.Float(), nullable=True),
    sa.Column('user_id', sa.String(), nullable=True),
    sa.Column('total_sleep', sa.Float(), nullable=True),
    sa.Column('resting_hr', sa.Float(), nullable=True),
    sa.Column('outlier_tag', sa.Integer(), nullable=True),
    sa.Column('step_score', sa.Float(), nullable=True),
    sa.Column('sleep_score', sa.Float(), nullable=True),
    sa.Column('hr_score', sa.Float(), nullable=True),
    sa.Column('step_week_slope', sa.Float(), nullable=True),
    sa.Column('sleep_week_slope', sa.Float(), nullable=True),
    sa.Column('hr_week_slope', sa.Float(), nullable=True),
    sa.Column('curr_health_score', sa.Float(), nullable=True),
    sa.Column('health_score_in_week', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('activities')
    ### end Alembic commands ###
