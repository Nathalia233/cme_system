import React, { useState } from 'react';
import { BrowserRouter as Router, Routes, Route, Link, Navigate } from 'react-router-dom';
import CreateUser from './components/CreateUser';
import CreateMaterial from './components/CreateMaterial';
import TrackMaterial from './components/TrackMaterial';
import Login from './components/Login';
import './App.css'; // Importe o arquivo CSS

function App() {
  const [isAuthenticated, setIsAuthenticated] = useState(false); // Use estado para autenticação

  return (
    <Router>
      <div className="App">
        {isAuthenticated ? (
          <nav className="navbar">
            <ul>
              <li><Link to="/create-user">Cadastro de Usuários</Link></li>
              <li><Link to="/create-material">Cadastro de Materiais</Link></li>
              <li><Link to="/track-material">Rastreabilidade de Materiais</Link></li>
            </ul>
          </nav>
        ) : null}
        <Routes>
          <Route path="/login" element={<Login setIsAuthenticated={setIsAuthenticated} />} />
          <Route path="/create-user" element={isAuthenticated ? <CreateUser /> : <Navigate to="/login" />} />
          <Route path="/create-material" element={isAuthenticated ? <CreateMaterial /> : <Navigate to="/login" />} />
          <Route path="/track-material" element={isAuthenticated ? <TrackMaterial /> : <Navigate to="/login" />} />
          <Route path="/" element={<Navigate to="/login" />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
