from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from sqlalchemy import Column, Integer, String, DateTime, func


engine = create_engine(
    'postgresql://ad_agent:agent_password@127.0.0.1:5432/ad_site_pgdb'
)

# Session = session.sessionmaker(engine)


Session = sessionmaker(engine)

Base = declarative_base(bind=engine)


# модель пользователя:
class User(Base):

    __tablename__ = 'ad_users'  # имя таблицы прописывается явно

    # колонки не создаются по умолчанию, как в Джанго - здесь сами делаем:

    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True
        )
    username = Column(
        String,
        nullable=False,
        unique=True,
        index=True
        )
    password = Column(
        String,
        nullable=False
        )
    email = Column(
        String,
        nullable=False,
        index=True
        )
    creation_time = Column(
        DateTime,
        server_default=func.now())


# модель объявления:
class Ad(Base):
    __tablename__ = 'ads'

    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True
        )
    header = Column(
        String,
        nullable=False,
        index=True
        )
    description = Column(
        String
        )
    creation_time = Column(
        DateTime,
        server_default=func.now()
        )
    user_id = Column(
        Integer,
        nullable=False
    )


# первая миграция:
Base.metadata.create_all()