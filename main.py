from fastapi import FastAPI
from crud import *

app = FastAPI(
    title="Global Quotes Insight Platform"
)

@app.get("/quotes")
def get_quotes_api():
    return get_all_quotes()

@app.post("/quotes")
def add_quote(text: str, author: str):

    create_quote(text, author)

    return {
        "message": "Quote added"
    }

@app.put("/quotes/{quote_id}")
def update_quote(
    quote_id: int,
    text: str,
    author: str
):

    update_quote_db(
        quote_id,
        text,
        author
    )

    return {
        "message": "Quote updated"
    }

@app.delete("/quotes/{quote_id}")
def delete_quote(quote_id: int):

    delete_quote_db(quote_id)

    return {
        "message": "Quote deleted"
    }