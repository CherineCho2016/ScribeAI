import './App.css';
import BookList from './components/Booklist.js';

function App() {
      
  return (
    <div className="App">
      <aside>
        <button>
          + New 
        </button>
      </aside>
      <section className='right'>
        <header className="App-header">
          <h1>ScribeAI</h1>
        </header>
        <main>
          <div>
            <p>Lorem ipsum odor amet, consectetuer adipiscing elit. Tempor dictum in adipiscing erat porttitor ultricies; feugiat mi. Morbi orci primis odio porta ante ornare venenatis dignissim convallis. Aliquam condimentum ligula ridiculus duis varius porta magna odio purus. Habitant potenti scelerisque interdum suscipit quam tempus facilisi mattis. Ac felis eleifend ad diam ultrices vulputate. Proin habitasse cursus magnis aenean nisi dis urna! Facilisis ad phasellus maximus vehicula curae ligula. Accumsan vivamus justo consectetur augue lobortis neque lobortis finibus in.

              Morbi nisi adipiscing est nulla dignissim ridiculus dapibus proin congue. Sem sit nisl placerat suspendisse adipiscing natoque elit. Lorem velit duis eu non; consequat molestie congue? Conubia himenaeos eget nec, est quisque tellus. Fermentum netus vulputate senectus torquent lacus suscipit urna duis. Aliquam turpis mus purus vulputate lobortis elementum ad. Nec dictumst mus mattis; augue tristique varius cubilia. Leo curabitur ornare dictum, tempus nunc hendrerit tincidunt fringilla ex. Morbi velit molestie primis dignissim; dapibus sodales.
              Lorem ipsum odor amet, consectetuer adipiscing elit. Tempor dictum in adipiscing erat porttitor ultricies; feugiat mi. Morbi orci primis odio porta ante ornare venenatis dignissim convallis. Aliquam condimentum ligula ridiculus duis varius porta magna odio purus. Habitant potenti scelerisque interdum suscipit quam tempus facilisi mattis. Ac felis eleifend ad diam ultrices vulputate. Proin habitasse cursus magnis aenean nisi dis urna! Facilisis ad phasellus maximus vehicula curae ligula. Accumsan vivamus justo consectetur augue lobortis neque lobortis finibus in.

              Morbi nisi adipiscing est nulla dignissim ridiculus dapibus proin congue. Sem sit nisl placerat suspendisse adipiscing natoque elit. Lorem velit duis eu non; consequat molestie congue? Conubia himenaeos eget nec, est quisque tellus. Fermentum netus vulputate senectus torquent lacus suscipit urna duis. Aliquam turpis mus purus vulputate lobortis elementum ad. Nec dictumst mus mattis; augue tristique varius cubilia. Leo curabitur ornare dictum, tempus nunc hendrerit tincidunt fringilla ex. Morbi velit molestie primis dignissim; dapibus sodales.
              Lorem ipsum odor amet, consectetuer adipiscing elit. Tempor dictum in adipiscing erat porttitor ultricies; feugiat mi. Morbi orci primis odio porta ante ornare venenatis dignissim convallis. Aliquam condimentum ligula ridiculus duis varius porta magna odio purus. Habitant potenti scelerisque interdum suscipit quam tempus facilisi mattis. Ac felis eleifend ad diam ultrices vulputate. Proin habitasse cursus magnis aenean nisi dis urna! Facilisis ad phasellus maximus vehicula curae ligula. Accumsan vivamus justo consectetur augue lobortis neque lobortis finibus in.

              Morbi nisi adipiscing est nulla dignissim ridiculus dapibus proin congue. Sem sit nisl placerat suspendisse adipiscing natoque elit. Lorem velit duis eu non; consequat molestie congue? Conubia himenaeos eget nec, est quisque tellus. Fermentum netus vulputate senectus torquent lacus suscipit urna duis. Aliquam turpis mus purus vulputate lobortis elementum ad. Nec dictumst mus mattis; augue tristique varius cubilia. Leo curabitur ornare dictum, tempus nunc hendrerit tincidunt fringilla ex. Morbi velit molestie primis dignissim; dapibus sodales.
            </p>
          </div>
          
          <div className="book-list">
          <div>
            <h2>Book name</h2>
            <p>Author</p>
            <p>Description</p>
            <BookList></BookList>
          </div>
        </div>
        </main>
        <form>
          <section className="user-input">
            <label for="query"></label>
            <textarea name="query" placeholder="Type here..."></textarea>
            <input type="submit" value="Submit"/>
          </section>
        </form>
        

      </section>
      
    </div>
  );
}

export default App;
