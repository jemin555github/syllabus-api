from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool

from alembic import context

#-----------------------add code--------------------#

import os, sys, sqlalchemy

import database.database

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
#---------------------------------------------------#

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

#-----------------------add code--------------------#
from database.database import db_url
SQLALCHEMY_DATABASE_URL = db_url
# this line is to overwrite the sqlalchemy url in the alembic.ini file.
config.set_main_option("sqlalchemy.url", str(SQLALCHEMY_DATABASE_URL))

# Interpret the config file for Python logging.
# This line sets up loggers basically.
fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata

#-----------------------Set branch for alembic version --------------------#

# Dynamically set version directory based on environment


#-----------------------add code--------------------#

from database.base import Base

target_metadata = Base.metadata

#---------------------------------------------------#

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.

def my_compare_type(context, inspected_column, metadata_column, inspected_type, metadata_type):
    # return False if the metadata_type is the same as the inspected_type
    # or None to allow the default implementation to compare these
    # types. a return value of True means the two types do not
    # match and should result in a type change operation.

    if isinstance(inspected_type, sqlalchemy.Enum) and isinstance(metadata_type, sqlalchemy.Enum):
        inspected_enum_values = set(inspected_type.enums)
        metadata_enum_values = set(metadata_type.enums)
        return inspected_enum_values != metadata_enum_values

    return None


def run_migrations_offline():
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
        compare_type=my_compare_type,
        compare_server_default=True
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata, compare_type=my_compare_type,
            compare_server_default=True
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()