from fastapi import FastAPI, Query
from pydantic import BaseModel

from src.summarizer import summarize

class Item(BaseModel):
    text: str

app = FastAPI()

default_text = "Актуальность проблемы. Электронная информация играет все большую роль во всех сферах жизни современного общества. В последние годы объем научно-технической текстовой информации в электронном виде возрос настолько, что возникает угроза обесценивания этой информации в связи с трудностями поиска необходимых сведений среди множества доступных текстов. Развитие информационных ресурсов Интернет многократно усугубило проблему информационной перегрузки. В этой ситуации особенно актуальными становятся методы автоматизации реферирования текстовой информации, то есть методы получения сжатого представления текстовых документов–рефератов (аннотаций). Постановка проблемы автоматического реферирования текста и соответственно попытки ее решения с использованием различных подходов предпринимались многими исследователями."

@app.get('/')
async def index(q: str = Query(None)):
    if q is None:
        q = default_text

    return {
        "annotation": summarize(q),
        "text": q
    }

@app.post("/summarize")
async def annotate(item: Item):
    return {
        "annotation": summarize(item.text),
        "text": item.text
    }