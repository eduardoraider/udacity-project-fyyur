"""empty message

Revision ID: caf38d837746
Revises: f2acf01b089a
Create Date: 2022-03-21 12:34:37.810823

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'caf38d837746'
down_revision = 'f2acf01b089a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('shows',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('artist_id', sa.Integer(), nullable=False),
    sa.Column('venue_id', sa.Integer(), nullable=False),
    sa.Column('start_time', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['artist_id'], ['artists.id'], ),
    sa.ForeignKeyConstraint(['venue_id'], ['venues.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.alter_column('artists', 'name',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('artists', 'city',
               existing_type=sa.VARCHAR(length=120),
               nullable=False)
    op.alter_column('artists', 'state',
               existing_type=sa.VARCHAR(length=120),
               nullable=False)
    op.alter_column('artists', 'phone',
               existing_type=sa.VARCHAR(length=120),
               nullable=False)
    op.alter_column('artists', 'genres',
               existing_type=postgresql.ARRAY(sa.VARCHAR()),
               nullable=False)
    op.alter_column('artists', 'image_link',
               existing_type=sa.VARCHAR(length=500),
               nullable=False)
    op.alter_column('artists', 'facebook_link',
               existing_type=sa.VARCHAR(length=120),
               nullable=True)
    op.alter_column('artists', 'seeking_venue',
               existing_type=sa.BOOLEAN(),
               nullable=True)
    op.alter_column('venues', 'name',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('venues', 'city',
               existing_type=sa.VARCHAR(length=120),
               nullable=False)
    op.alter_column('venues', 'state',
               existing_type=sa.VARCHAR(length=120),
               nullable=False)
    op.alter_column('venues', 'address',
               existing_type=sa.VARCHAR(length=120),
               nullable=False)
    op.alter_column('venues', 'phone',
               existing_type=sa.VARCHAR(length=120),
               nullable=False)
    op.alter_column('venues', 'image_link',
               existing_type=sa.VARCHAR(length=500),
               nullable=False)
    op.alter_column('venues', 'facebook_link',
               existing_type=sa.VARCHAR(length=120),
               nullable=True)
    op.alter_column('venues', 'seeking_talent',
               existing_type=sa.BOOLEAN(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('venues', 'seeking_talent',
               existing_type=sa.BOOLEAN(),
               nullable=False)
    op.alter_column('venues', 'facebook_link',
               existing_type=sa.VARCHAR(length=120),
               nullable=True)
    op.alter_column('venues', 'image_link',
               existing_type=sa.VARCHAR(length=500),
               nullable=True)
    op.alter_column('venues', 'phone',
               existing_type=sa.VARCHAR(length=120),
               nullable=True)
    op.alter_column('venues', 'address',
               existing_type=sa.VARCHAR(length=120),
               nullable=True)
    op.alter_column('venues', 'state',
               existing_type=sa.VARCHAR(length=120),
               nullable=True)
    op.alter_column('venues', 'city',
               existing_type=sa.VARCHAR(length=120),
               nullable=True)
    op.alter_column('venues', 'name',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('artists', 'seeking_venue',
               existing_type=sa.BOOLEAN(),
               nullable=False)
    op.alter_column('artists', 'facebook_link',
               existing_type=sa.VARCHAR(length=120),
               nullable=True)
    op.alter_column('artists', 'image_link',
               existing_type=sa.VARCHAR(length=500),
               nullable=True)
    op.alter_column('artists', 'genres',
               existing_type=postgresql.ARRAY(sa.VARCHAR()),
               nullable=True)
    op.alter_column('artists', 'phone',
               existing_type=sa.VARCHAR(length=120),
               nullable=True)
    op.alter_column('artists', 'state',
               existing_type=sa.VARCHAR(length=120),
               nullable=True)
    op.alter_column('artists', 'city',
               existing_type=sa.VARCHAR(length=120),
               nullable=True)
    op.alter_column('artists', 'name',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.drop_table('shows')
    # ### end Alembic commands ###
