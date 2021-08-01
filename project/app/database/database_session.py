import logging
import os
from typing import Callable, Optional

import sqlalchemy
from sqlalchemy.orm import Session

from project.app.database.modelbase import Base

__factory: Optional[Callable[[], Session]] = None
log = logging.getLogger("uvicorn")


def get_db() -> Session:
    db = create_session()
    try:
        yield db
    finally:
        db.close()


def global_init() -> None:
    global __factory

    if __factory:
        return

    conn_str = str(
        os.environ.get("DATABASE_URL", "sqlite:///project/db/local_database.db")
    )
    log.info("Connecting to the database...")
    engine = sqlalchemy.create_engine(conn_str, echo=False)
    __factory = sqlalchemy.orm.sessionmaker(bind=engine)

    from project.app.models.register import Register

    Base.metadata.create_all(engine)


def create_session() -> Session:
    global __factory

    if not __factory:
        raise Exception("You must call global_init() before using this method")

    session: Session = __factory()
    session.expire_on_commit = False

    return session
