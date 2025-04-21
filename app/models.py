from sqlalchemy import Column, Integer, String, Date
from app.database import Base

class StudentSurvey(Base):
    __tablename__ = "surveys"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    street_address = Column(String(100))
    city = Column(String(50))
    state = Column(String(50))
    zip_code = Column(String(20))
    telephone = Column(String(20))
    email = Column(String(100))
    date_of_survey = Column(Date)

    liked_most = Column(String(255))  # Store as comma-separated values
    interest_source = Column(String(50))
    recommendation = Column(String(20))
    raffle = Column(String(255))
    comments = Column(String(500))

# Only for dev/debug
if __name__ == "__main__":
    from app.database import engine
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
