import pytest\nfrom fastapi.testclient import TestClient\nfrom app.main import app\n

# create a test client\nclient = TestClient(app)\n\n\n# test the root route\ndef test_root():\n    response = client.get('/')\n    assert response.status_code == 200\n    assert response.json() == {'message': 'Welcome to the e-commerce platform'}