from sqlalchemy import Column, Integer, String
from classes.base import Base
from sqlalchemy.orm import relationship, Session
class Activity(Base):
    __tablename__ = 'activities'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    duration = Column(Integer())
    family_friendly = Column(Integer())
    city = Column(String())
    address = Column(String())    
    activity_type = Column(String())
    
    user_activities = relationship("UserActivityHistory", back_populates="activity")

    def addToDB(self, engine):
        with Session(engine) as session:
            session.add(self)
            session.commit()
        pass
    
    def deleteFromDB(self, session):
        session.delete(self)
        session.commit()

    def __repr__(self) -> str:
        return f"{self.name} ({self.activity_type}) in {self.address}, {self.city}. {self.duration} hours, {'' if self.family_friendly == 1 else 'not'} family friendly"
    
    