from conftest import client

def test_get_concept(client):
    concept_data = {
        "title": "Test Concept",
        "definition": "A definition for testing.",
        "example": "An example for testing.",
        "explanation": "An explanation for testing.",
        "common_misconception": "A misconception for testing.",
        "related_concepts": None
    }

    response = client.post("/concepts", json=concept_data)
    created_concept = response.json()
    concept_id = created_concept["id"]
    
    get_concept = client.get(f"/concepts/{concept_id}")
    
    concept_data["id"] = created_concept["id"]
    assert get_concept.status_code == 200
    assert get_concept.json() == concept_data

def test_create_concept(client):
    concept_data = {
        "title": "Test Concept",
        "definition": "A definition for testing.",
        "example": "An example for testing.",
        "explanation": "An explanation for testing.",
        "common_misconception": "A misconception for testing.",
        "related_concepts": None
    }
    
    response = client.post("/concepts", json=concept_data)

    created_concept = response.json()


    assert created_concept["title"] == concept_data["title"]
    assert created_concept["definition"] == concept_data["definition"]
    assert created_concept["example"] == concept_data["example"]
    assert created_concept["explanation"] == concept_data["explanation"]
    assert created_concept["common_misconception"] == concept_data["common_misconception"]
    assert created_concept["related_concepts"] == concept_data["related_concepts"]

def test_edit_concept(client):
    concept_data = {
        "title": "Test Concept",
        "definition": "A definition for testing.",
        "example": "An example for testing.",
        "explanation": "An explanation for testing.",
        "common_misconception": "A misconception for testing.",
        "related_concepts": None
    }

    response = client.post("/concepts", json=concept_data)
    created_concept = response.json()

    concept_id = created_concept["id"]
    created_concept["title"] = "new concept"

    modified_table = client.put(
        f"/concepts/{concept_id}",
        json=created_concept
    )

    assert modified_table.status_code == 200
    assert modified_table.json()["title"] == 'new concept'

def test_delete_concept(client):
    concept_data = {
            "title": "Test Concept",
            "definition": "A definition for testing.",
            "example": "An example for testing.",
            "explanation": "An explanation for testing.",
            "common_misconception": "A misconception for testing.",
            "related_concepts": None
        }
    response = client.post("/concepts", json=concept_data)
    created_concept = response.json()
    concept_id = created_concept["id"]

    deleted_concept = client.delete(f"/concepts/{concept_id}")

    assert deleted_concept.status_code == 200 
    assert deleted_concept.json()["message"] == "Concept deleted"