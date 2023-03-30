from sqlalchemy import Column, Integer, String
from classes.base import Base
from sqlalchemy.orm import relationship, backref, Session


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    city = Column(String())
    address = Column(String())
    fave_type = Column(String())
    age = Column(Integer())
    user_activities = relationship("UserActivityHistory", back_populates="user")

    def addToDB(self, engine):
        with Session(engine) as session:
            session.add(self)
            session.commit()
        
    def deleteFromDB(self, session):
        session.delete(self)
        session.commit()
    def __repr__(self) -> str:
        return f"{self.name} (age: {self.age}), lives at {self.address}, {self.city}. Their favorite activty is {self.fave_type}"