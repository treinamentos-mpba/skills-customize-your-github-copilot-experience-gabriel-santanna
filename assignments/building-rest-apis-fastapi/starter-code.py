from fastapi import FastAPI, HTTPException, Response, status
from pydantic import BaseModel

app = FastAPI(title="Book Catalog API")


class BookInput(BaseModel):
    title: str
    author: str
    year: int


class Book(BookInput):
    id: int


books = [
    Book(id=1, title="The Hobbit", author="J. R. R. Tolkien", year=1937),
    Book(id=2, title="A Wizard of Earthsea", author="Ursula K. Le Guin", year=1968),
]
next_book_id = 3


@app.get("/books", response_model=list[Book])
def list_books():
    # TODO: Return the current collection of books.
    raise NotImplementedError


@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int):
    # TODO: Find and return the book, or raise HTTPException with status 404.
    raise NotImplementedError


@app.post("/books", response_model=Book, status_code=status.HTTP_201_CREATED)
def create_book(book_input: BookInput):
    global next_book_id
    # TODO: Create a Book with the next ID, add it to books, and return it.
    raise NotImplementedError


@app.put("/books/{book_id}", response_model=Book)
def update_book(book_id: int, book_input: BookInput):
    # TODO: Replace the matching book's fields, or raise HTTPException with status 404.
    raise NotImplementedError


@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id: int):
    # TODO: Remove the matching book, or raise HTTPException with status 404.
    return Response(status_code=status.HTTP_204_NO_CONTENT)