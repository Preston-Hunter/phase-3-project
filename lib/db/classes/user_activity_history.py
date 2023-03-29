from sqlalchemy import Column, Integer, String, ForeignKey
from classes.base import Base
from sqlalchemy.orm import relationship, backref, Session

class UserActivityHistory(Base):
     __tablename__ = 'users-activities'

     id = Column(Integer(), primary_key=True)
     user_id = Column(Integer(), ForeignKey('users.id'))
     activity_id = Column(Integer(), ForeignKey('activities.id'))
     
     user = relationship("User", back_populates="user_activities")    
     activity = relationship("Activity",back_populates="user_activities")

     def addToDB(self, engine):
        with Session(engine) as session:
            session.add(self)
            session.commit()
        

     def deleteFromDB(self, session):
          print(self.name)
          session.delete(self)
          session.commit()
     