from sqlalchemy.orm import Session
from app import models, schemas 


def create_survey(db: Session, survey: schemas.SurveyCreate):
    liked_str = ",".join(survey.liked_most)
    db_survey = models.StudentSurvey(
        **survey.dict(exclude={"liked_most"}),
        liked_most=liked_str
    )
    db.add(db_survey)
    db.commit()
    db.refresh(db_survey)
    return db_survey

def get_surveys(db: Session):
    return db.query(models.StudentSurvey).all()
