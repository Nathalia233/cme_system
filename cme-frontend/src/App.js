import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import CreateUser from './components/CreateUser';
import CreateMaterial from './components/CreateMaterial';
import TrackMaterial from './components/TrackMaterial';
import './App.css';


function App() {
  return (
    <Router>
      <div className="App">
        <nav className="navbar">
          <ul>
            <li><Link to="/create-user">Cadastro de Usuários</Link></li>
            <li><Link to="/create-material">Cadastro de Materiais</Link></li>
            <li><Link to="/track-material">Rastreabilidade de Materiais</Link></li>
          </ul>
        </nav>
        <Routes>
          <Route path="/create-user" element={<CreateUser />} />
          <Route path="/create-material" element={<CreateMaterial />} />
          <Route path="/track-material" element={<TrackMaterial />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
