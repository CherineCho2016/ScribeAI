import './App.css';

import Form from './components/Form.js';
import Main from './components/Main.js';
// import {} from '../public/'
function App() {
      
  return (
    <div className="App">
        <header className="App-header">
          <h1>scribe.ai</h1>
        </header>
      <div className="wrapper">
      <aside className='aside'>
        <button className='new'>
          + New 
        </button>
      </aside>
      <section className='right'>

        <Main></Main>        

      </section>
      </div>
    </div>
  );
}

export default App;
