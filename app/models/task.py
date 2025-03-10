from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from backend.db import Base  

class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    content = Column(String)
    priority = Column(Integer, default=0) 
    completed = Column(Boolean, default=False)  
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False, index=True)
    slug = Column(String, unique=True, index=True)  

    user = relationship("User", back_populates="tasks")


    def __repr__(self):
        return f"<Task(id={self.id}, title={self.title}, user_id={self.user_id}, completed={self.completed})>"