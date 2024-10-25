import React, { useState, useEffect } from 'react';

function BookList(){
    const [books, setBooks] = useState([])
    useEffect(() => {
        setBooks([
        {
          "name":"Otostopçunun Galaksi Rehberi", 
          "author":    "Douglas Adams", 
          "description": "Lorem ipsum"
        },
        {
          "name":"Hikayeler", 
          "author":    "Edgar Allan Poe", 
          "description": "Lorem ipsum sit door amet"
        }
      ])
      }, [])
      return (
        <div className="book-list">
          {books.map((book, index) => (
            <div key={index} className="book-item">
              <h2>{book.name}</h2>
              <p>Author: {book.author}</p>
              <p>{book.description}</p>
            </div>
          ))}
        </div>
      );
}

export default BookList;