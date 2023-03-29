from sqlalchemy import Column, Integer, String
from classes.base import Base
from sqlalchemy.orm import relationship, backref, Session


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    user_activities = relationship("UserActivityHistory", back_populates="user")

    def addToDB(self, engine):
        with Session(engine) as session:
            session.add(self)
            session.commit()
        
    def deleteFromDB(self, session):
        session.delete(self)
        session.commit()