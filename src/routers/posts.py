from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from typing import List

from .. import schemas, crud
from ..database import get_db


router = APIRouter(
    prefix='/posts',
    tags=['Posts']
)


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.PostWrite)
def create_post(request: schemas.PostWrite, db: Session = Depends(get_db)):
    return crud.create_post(db, request)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def remove_post(id: int, db: Session = Depends(get_db)):
    return crud.remove_post(db, id)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_post(id: int, request: schemas.PostWrite, db: Session = Depends(get_db)):
    return crud.update_post(db, id, request)


@router.get('/', status_code=status.HTTP_200_OK, response_model=List[schemas.PostRead])
def update_post(
    skip: int | None = 0,
    limit: int | None = 100,
    db: Session = Depends(get_db)
):
    return crud.get_post_all(db=db, skip=skip, limit=limit)


@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.PostRead)
def update_post(id: int, db: Session = Depends(get_db)):
    return crud.get_post(db, id)

