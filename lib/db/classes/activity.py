from sqlalchemy import Column, Integer, String
from classes.base import Base
from sqlalchemy.orm import relationship, Session
class Activity(Base):
    __tablename__ = 'activities'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    user_activities = relationship("UserActivityHistory", back_populates="activity")

    def addToDB(self, engine):
        with Session(engine) as session:
            session.add(self)
            session.commit()
        pass
    
    def deleteFromDB(self, session):
        session.delete(self)
        session.commit()