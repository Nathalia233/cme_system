// src/components/TrackMaterial.js

import React, { useState } from 'react';
import axios from 'axios';
import { Form, Title, Label, Input, Button } from './CreateUserStyles'; // Reutilizando os estilos do CreateUserStyles

function TrackMaterial() {
  const [serial, setSerial] = useState('');
  const [logs, setLogs] = useState([]);

  const handleSearch = async () => {
    try {
      const response = await axios.get(`http://localhost:8000/api/processlogs?serial=${serial}`);
      setLogs(response.data);
    } catch (error) {
      console.error('Erro ao buscar rastreabilidade:', error);
    }
  };

  return (
    <Form>
      <Title>Rastreabilidade de Materiais</Title>
      <Label>
        Serial:
        <Input type="text" value={serial} onChange={(e) => setSerial(e.target.value)} />
      </Label>
      <Button type="button" onClick={handleSearch}>Buscar</Button>
      <Title>Logs de Processo:</Title>
      {logs.length > 0 ? (
        <ul>
          {logs.map((log, index) => (
            <li key={index}>{log.status} - {log.timestamp}</li>
          ))}
        </ul>
      ) : <p>Nenhum log encontrado.</p>}
    </Form>
  );
}

export default TrackMaterial;
