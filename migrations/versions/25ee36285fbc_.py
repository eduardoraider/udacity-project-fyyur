"""empty message

Revision ID: 25ee36285fbc
Revises: caf38d837746
Create Date: 2022-03-21 12:46:57.556676

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '25ee36285fbc'
down_revision = 'caf38d837746'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('shows', 'artist_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('shows', 'venue_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('shows', 'start_time',
               existing_type=postgresql.TIMESTAMP(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('shows', 'start_time',
               existing_type=postgresql.TIMESTAMP(),
               nullable=True)
    op.alter_column('shows', 'venue_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('shows', 'artist_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###
