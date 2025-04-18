from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


class PostgresService:
    engine: Engine
    Base: declarative_base
    Session: sessionmaker

    def __init__(self, url: str) -> None:
        self.engine = create_engine(url)
        self.Base = declarative_base()
        self.Session = sessionmaker(bind=self.engine)

    def init_database(self) -> None:
        self.Base.metadata.create_all(self.engine)

    def drop_database(self) -> None:
        self.Base.metadata.drop_all(self.engine)