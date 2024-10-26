import './App.css';

import Form from './components/Form.js';
import Main from './components/Main.js';

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
        <Main></Main>        

      </section>
      
    </div>
  );
}

export default App;
