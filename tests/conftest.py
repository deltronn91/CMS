import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi.testclient import TestClient
import models

# Load environment variables from the .env file so Python can access configuration
# values, such as the database URL. Tests use a separate test database URL
# to keep test operations separate from the main database.

from main import app

TEST_DATABASE_URL = "postgresql+psycopg://delseangross:haola@localhost/cms_test_db"

from database import get_db, Base

test_engine = create_engine(TEST_DATABASE_URL)
Base.metadata.create_all(bind=test_engine)

TestingSession = sessionmaker(bind=test_engine)


@pytest.fixture
#this databse session is created and closed around the request.
def client():
    def override_get_db():
        db = TestingSession()
        try:
            yield db
        finally:
            db.close()

    #override registration process
    #this registration saves the replacement function on the fast api "app"
    app.dependency_overrides[get_db] = override_get_db

    with TestClient(app) as test_client:
        yield test_client

    app.dependency_overrides.clear()

