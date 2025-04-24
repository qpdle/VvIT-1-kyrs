from fastapi import FastAPI
from pydantic import BaseModel
import wikipedia

app = FastAPI()

wikipedia.set_lang("ru")

class Article(BaseModel):
    title: str
    summary: str

class SearchInput(BaseModel):
    query: str

class PageInput(BaseModel):
    title: str
    sentences: int = 2

@app.get("/article/{title}", response_model=Article)
def get_article(title: str):
    try:
        page = wikipedia.page(title)
        return Article(title=page.title, summary=page.summary)
    except wikipedia.exceptions.PageError:
        return {"error": "Страница не найдена"}
    except wikipedia.exceptions.DisambiguationError as e:
        return {"error": f"Уточните запрос. Возможные варианты: {', '.join(e.options[:5])}"}

@app.get("/search/", response_model=list[str])
def search_articles(query: str, limit: int = 5):
    results = wikipedia.search(query, results=limit)
    return results

@app.post("/summary/", response_model=Article)
def get_summary(input: PageInput):
    try:
        summary = wikipedia.summary(input.title, sentences=input.sentences)
        return Article(title=input.title, summary=summary)
    except wikipedia.exceptions.PageError:
        return {"error": "Страница не найдена"}