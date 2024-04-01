"""init

Revision ID: 4aff1e605420
Revises: 
Create Date: 2024-03-20 21:43:24.210950

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = '4aff1e605420'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('connection',
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('type', sa.Enum('RADARR', 'SONARR', name='arrtype'), nullable=False),
    sa.Column('url', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('api_key', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('monitor', sa.Enum('MONITOR_ALL', 'MONITOR_MISSING', 'MONITOR_NEW', 'MONITOR_SYNC', name='monitortype'), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('added_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('movie',
    sa.Column('radarr_id', sa.Integer(), nullable=False),
    sa.Column('title', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('year', sa.Integer(), nullable=False),
    sa.Column('language', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('overview', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('runtime', sa.Integer(), nullable=False),
    sa.Column('website', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('youtube_trailer_id', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('folder_path', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('imdb_id', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('tmdb_id', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('poster_url', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('fanart_url', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('poster_path', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('fanart_path', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('trailer_exists', sa.Boolean(), nullable=False),
    sa.Column('monitor', sa.Boolean(), nullable=False),
    sa.Column('radarr_monitored', sa.Boolean(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('connection_id', sa.Integer(), nullable=False),
    sa.Column('added_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.Column('downloaded_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['connection_id'], ['connection.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_movie_connection_id'), 'movie', ['connection_id'], unique=False)
    op.create_index(op.f('ix_movie_imdb_id'), 'movie', ['imdb_id'], unique=False)
    op.create_index(op.f('ix_movie_language'), 'movie', ['language'], unique=False)
    op.create_index(op.f('ix_movie_title'), 'movie', ['title'], unique=False)
    op.create_index(op.f('ix_movie_tmdb_id'), 'movie', ['tmdb_id'], unique=False)
    op.create_index(op.f('ix_movie_year'), 'movie', ['year'], unique=False)
    op.create_table('series',
    sa.Column('sonarr_id', sa.Integer(), nullable=False),
    sa.Column('title', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('year', sa.Integer(), nullable=False),
    sa.Column('language', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('overview', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('runtime', sa.Integer(), nullable=False),
    sa.Column('website', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('youtube_trailer_id', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('folder_path', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('imdb_id', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('tvdb_id', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('poster_url', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('fanart_url', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('poster_path', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('fanart_path', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('trailer_exists', sa.Boolean(), nullable=False),
    sa.Column('monitor', sa.Boolean(), nullable=False),
    sa.Column('sonarr_monitored', sa.Boolean(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('connection_id', sa.Integer(), nullable=False),
    sa.Column('added_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.Column('downloaded_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['connection_id'], ['connection.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_series_connection_id'), 'series', ['connection_id'], unique=False)
    op.create_index(op.f('ix_series_imdb_id'), 'series', ['imdb_id'], unique=False)
    op.create_index(op.f('ix_series_language'), 'series', ['language'], unique=False)
    op.create_index(op.f('ix_series_title'), 'series', ['title'], unique=False)
    op.create_index(op.f('ix_series_tvdb_id'), 'series', ['tvdb_id'], unique=False)
    op.create_index(op.f('ix_series_year'), 'series', ['year'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_series_year'), table_name='series')
    op.drop_index(op.f('ix_series_tvdb_id'), table_name='series')
    op.drop_index(op.f('ix_series_title'), table_name='series')
    op.drop_index(op.f('ix_series_language'), table_name='series')
    op.drop_index(op.f('ix_series_imdb_id'), table_name='series')
    op.drop_index(op.f('ix_series_connection_id'), table_name='series')
    op.drop_table('series')
    op.drop_index(op.f('ix_movie_year'), table_name='movie')
    op.drop_index(op.f('ix_movie_tmdb_id'), table_name='movie')
    op.drop_index(op.f('ix_movie_title'), table_name='movie')
    op.drop_index(op.f('ix_movie_language'), table_name='movie')
    op.drop_index(op.f('ix_movie_imdb_id'), table_name='movie')
    op.drop_index(op.f('ix_movie_connection_id'), table_name='movie')
    op.drop_table('movie')
    op.drop_table('connection')
    # ### end Alembic commands ###