from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

# Initialize FastAPI app
app = FastAPI(title="Book API", description="A simple API for managing books")

# Pydantic model for Book
class Book(BaseModel):
    id: Optional[int] = None
    title: str
    author: str
    price: float
    in_stock: bool = True

# In-memory database
books_db = []
counter = 1

# Routes
@app.get("/")
async def root():
    return {"message": "Welcome to the Book API!"}

@app.get("/books", response_model=List[Book])
async def get_books():
    return books_db

@app.get("/books/{book_id}", response_model=Book)
async def get_book(book_id: int):
    book = next((book for book in books_db if book.id == book_id), None)
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@app.post("/books", response_model=Book)
async def create_book(book: Book):
    global counter
    book.id = counter
    counter += 1
    books_db.append(book)
    return book

@app.put("/books/{book_id}", response_model=Book)
async def update_book(book_id: int, updated_book: Book):
    book_idx = next((idx for idx, book in enumerate(books_db) if book.id == book_id), None)
    if book_idx is None:
        raise HTTPException(status_code=404, detail="Book not found")
    
    updated_book.id = book_id
    books_db[book_idx] = updated_book
    return updated_book

@app.delete("/books/{book_id}")
async def delete_book(book_id: int):
    book_idx = next((idx for idx, book in enumerate(books_db) if book.id == book_id), None)
    if book_idx is None:
        raise HTTPException(status_code=404, detail="Book not found")
    
    books_db.pop(book_idx)
    return {"message": "Book deleted successfully"}