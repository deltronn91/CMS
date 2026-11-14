from fastapi import APIRouter, HTTPException, Depends
from database import get_db
from models import Concept
from schemas import ConceptCreate, UpdateConcept

router = APIRouter()


@router.get("/concepts")
def get_concepts(session=Depends(get_db)):
    concepts = session.query(Concept).order_by(Concept.title).all()
    return concepts


@router.post("/concepts")
def create_concept(concept: ConceptCreate, session=Depends(get_db)):
    new_concept = Concept(
        title=concept.title,
        definition=concept.definition,
        example=concept.example,
        explanation=concept.explanation,
        common_misconception=concept.common_misconception,
        related_concepts=concept.related_concepts
    )

    session.add(new_concept)
    session.commit()
    session.refresh(new_concept)
    return new_concept


@router.get("/concepts/{concept_id}")
def get_concept(concept_id: int, session=Depends(get_db)):
    concept = session.query(Concept).filter(
        Concept.id == concept_id
    ).first()

    if concept is None:
        raise HTTPException(status_code=404, detail="Concept not found")

    return concept


@router.put("/concepts/{concept_id}")
def update_concept(
    concept: UpdateConcept,
    concept_id: int,
    session=Depends(get_db)
):
    db_concept = session.query(Concept).filter(
        Concept.id == concept_id
    ).first()

    if db_concept is None:
        raise HTTPException(status_code=404, detail="Concept not found")

    if concept.title is not None:
        db_concept.title = concept.title
    if concept.definition is not None:
        db_concept.definition = concept.definition
    if concept.example is not None:
        db_concept.example = concept.example
    if concept.explanation is not None:
        db_concept.explanation = concept.explanation
    if concept.common_misconception is not None:
        db_concept.common_misconception = concept.common_misconception
    if concept.related_concepts is not None:
        db_concept.related_concepts = concept.related_concepts

    session.commit()
    session.refresh(db_concept)
    return db_concept


@router.delete("/concepts/{concept_id}")
def delete_concept(concept_id: int, session=Depends(get_db)):
    db_concept = session.query(Concept).filter(
        Concept.id == concept_id
    ).first()

    if db_concept is None:
        raise HTTPException(status_code=404, detail="Concept not found")

    session.delete(db_concept)
    session.commit()

    return {"message": "Concept deleted"}