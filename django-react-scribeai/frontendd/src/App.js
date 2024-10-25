import './App.css';
import BookList from './Booklist.js';

function App() {
      
  return (
    <div className="App">
      <header className="App-header">
        <h1>DjangoReact</h1>
      </header>
      <div className="book-list">
        <div>
          <h2>Book name</h2>
          <p>Author</p>
          <p>Description</p>
          <BookList></BookList>

        </div>
      </div>
    </div>
  );
}

export default App;
