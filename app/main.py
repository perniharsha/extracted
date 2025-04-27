from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas, crud, database  

# THIS must come before using `@app` decorators
app = FastAPI()


@app.post("/surveys/")
def create_survey(survey: schemas.SurveyCreate, db: Session = Depends(database.get_db)):

    raffle_nums = [int(num.strip()) for num in survey.raffle.split(",") if num.strip().isdigit()]
    if len(raffle_nums) < 10 or not all(1 <= n <= 100 for n in raffle_nums):
        raise HTTPException(status_code=400, detail="Raffle must contain at least ten numbers between 1 and 100.")
    return crud.create_survey(db, survey)

@app.get("/surveys/")
def read_surveys(db: Session = Depends(database.get_db)):
    return crud.get_surveys(db)


Base.metadata.create_all(bind=engine)
