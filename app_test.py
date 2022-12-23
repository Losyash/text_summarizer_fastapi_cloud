from fastapi.testclient import TestClient
from app import app

default_text = "Актуальность проблемы. Электронная информация играет все большую роль во всех сферах жизни современного общества. В последние годы объем научно-технической текстовой информации в электронном виде возрос настолько, что возникает угроза обесценивания этой информации в связи с трудностями поиска необходимых сведений среди множества доступных текстов. Развитие информационных ресурсов Интернет многократно усугубило проблему информационной перегрузки. В этой ситуации особенно актуальными становятся методы автоматизации реферирования текстовой информации, то есть методы получения сжатого представления текстовых документов–рефератов (аннотаций). Постановка проблемы автоматического реферирования текста и соответственно попытки ее решения с использованием различных подходов предпринимались многими исследователями."

client = TestClient(app)


def test_summarize_response_method():
    response = client.post("/")

    assert response.status_code == 405


def test_index_response_data():
    response = client.get("/")

    json_data = response.json()

    assert response.status_code == 200
    assert json_data['annotation'] == 'Электронная информация становится все более значимой в жизни современного человека.'


def test_summarize_response_method():
    response = client.get("/summarize")

    assert response.status_code == 405


def test_summarize_response_data():
    response = client.post("/summarize", json={"text": default_text})

    json_data = response.json()

    assert response.status_code == 200
    assert json_data['annotation'] == 'Электронная информация становится все более значимой в жизни современного человека.'


def test_read_summarize_none_body():
    response = client.post("/summarize", json=None)

    assert response.status_code == 422


def test_read_summarize_none_text():
    response = client.post("/summarize", json={"text": None})

    assert response.status_code == 422
