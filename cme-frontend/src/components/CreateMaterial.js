// src/components/CreateMaterial.js

import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Form, Title, Label, Input, Select, Button } from './CreateUserStyles'; // Reutilizando os estilos do CreateUserStyles

function CreateMaterial() {
  const [formData, setFormData] = useState({ name: '', type: '', expirationDate: '', serial: '' });

  useEffect(() => {
    // Gerar serial automaticamente baseado no nome do material
    setFormData((prevFormData) => ({
      ...prevFormData,
      serial: prevFormData.name ? `${prevFormData.name}-${Math.floor(Math.random() * 10000)}` : ''
    }));
  }, [formData.name]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('http://localhost:8000/api/materials/', formData);
      console.log('Material criado:', response.data);
    } catch (error) {
      console.error('Erro ao criar material:', error);
    }
  };

  return (
    <Form onSubmit={handleSubmit}>
      <Title>Criar Material</Title>
      <Label>
        Nome do Material:
        <Input type="text" value={formData.name} onChange={(e) => setFormData({ ...formData, name: e.target.value })} />
      </Label>
      <Label>
        Tipo do Material:
        <Select value={formData.type} onChange={(e) => setFormData({ ...formData, type: e.target.value })}>
          <option value="">Selecione um tipo</option>
          <option value="esteril">Esteril</option>
          <option value="nao-esteril">Não Esteril</option>
        </Select>
      </Label>
      <Label>
        Data de Validade:
        <Input type="date" value={formData.expirationDate} onChange={(e) => setFormData({ ...formData, expirationDate: e.target.value })} />
      </Label>
      <Label>
        Serial (Gerado Automaticamente):
        <Input type="text" value={formData.serial} readOnly />
      </Label>
      <Button type="submit">Cadastrar</Button>
    </Form>
  );
}

export default CreateMaterial;
