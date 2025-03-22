from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context

# Import your Base class and models
from app.core.database import Base
from app.models.admin_model import Admin
from app.models.team_model import Team
from app.models.player_model import Player
from app.models.auction_history_model import AuctionHistory
from app.models.player_stats_model import PlayerStats
from app.models.auction_settings_model import AuctionSettings

# Load Alembic configuration
config = context.config
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Set target metadata for autogeneration
target_metadata = Base.metadata

def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online() -> None:
    """Run migrations in 'online' mode."""
    from app.core.config import DATABASE_URL  # Import the actual DB URL

    connectable = engine_from_config(
        {"sqlalchemy.url": DATABASE_URL},
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
