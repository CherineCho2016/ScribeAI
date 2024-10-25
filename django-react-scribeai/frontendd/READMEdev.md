Front End
- React Frontend
    - npx create-react-app frontend in root dir
    - cd frontend & npm start
- Common Hooks
    - useState
        - ```const [books, setBooks] = useState([])```
        - books is the thing we are watching
        - setBooks updates what we are watching
        - useState([]) sets the initial books = []
    - useEffecct
        - ```useEffect(() => {...}, [])```
        - runs once at start, and runs the {...}
        - use case: if we use like setBooks, we can render in the info/db here
    -HOW TO make it appear:
        - ```{books.map((book, index) => (
            <div key={index} className="book-item">
              <h2>{book.name}</h2>
              <p>Author: {book.author}</p>
              <p>{book.description}</p>
            </div>
          ))}```
        - put them into a function/componenet, import it to app, and inside the return <\functionname\><> like u would normally add components to the page
