from sqlalchemy import Integer, Text, Column
from database import Base

class Concept(Base):
    __tablename__ = 'concepts'
    id = Column(Integer, primary_key=True)
    title = Column(Text, nullable=False)
    definition = Column(Text, nullable=False)
    example = Column(Text, nullable = False)
    explanation = Column(Text, nullable=False)
    common_misconception = Column(Text, nullable=False)
    related_concepts = Column(Text)


