from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session

from .. import schemas, crud
from ..database import get_db


router = APIRouter(
    prefix='/reactions',
    tags=['Reactions']
)


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.ReactionRead)
def create_reaction(request: schemas.ReactionWrite, db: Session = Depends(get_db)):
    return crud.create_reaction(db, request)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED, response_model=schemas.ReactionRead)
def update_reaction(request: schemas.ReactionWrite, db: Session = Depends(get_db)):
    return crud.update_reaction(db, request)


@router.delete('/{id}', status_code=status.HTTP_202_ACCEPTED)
def remove_reaction(id: int, db: Session = Depends(get_db)):
    return crud.remove_reaction(db, id)

