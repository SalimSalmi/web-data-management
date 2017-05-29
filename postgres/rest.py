

from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import func
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.ext.declarative import declarative_base

# Eve imports
from eve import Eve
from eve_sqlalchemy import SQL
from eve_sqlalchemy.validation import ValidatorSQL

# Eve-SQLAlchemy imports
from eve_sqlalchemy.decorators import registerSchema

Base = declarative_base()


class CommonColumns(Base):
    __abstract__ = True
    _created = Column(DateTime, default=func.now())
    _updated = Column(
        DateTime,
        default=func.now(),
        onupdate=func.now())
    _etag = Column(String)
    _id = Column(Integer, primary_key=True, autoincrement=True)


@registerSchema('movies')
class Movies(Base):
    __tablename__ = 'movies'
    idmovies = Column(Integer, primary_key=True)
    title = Column(String(2000))
    year = Column(Integer)


pg_url = 'postgresql://localhost/moviedb'

SETTINGS = {
    'SQLALCHEMY_DATABASE_URI': pg_url,
    'RESOURCE_METHODS': ['POST', 'GET'],
    'ITEM_METHODS': ['GET'],
    'DOMAIN': {
            'movies': Movies._eve_schema['movies'],
        },
}

application = Eve(auth=None, settings=SETTINGS, data=SQL)

# bind SQLAlchemy
db = application.data.driver
Base.metadata.bind = db.engine
db.Model = Base
db.create_all()

if __name__ == "__main__":
    application.run(debug=True)
