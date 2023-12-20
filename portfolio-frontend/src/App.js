// import 'Header' from './'
import Header from './components/Header/Header'
import Dashboard from './components/Dashboard/Dashboard';
import About from './components/About/About';
import './App.css';

function App() {
  return (
    <div className="App">
      <Header/>
      <Dashboard/>
      <About/>
    </div>
  );
}

export default App;
