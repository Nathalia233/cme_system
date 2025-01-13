// src/components/CreateUser.js

import React, { useState } from 'react';
import axios from 'axios';
import { Form, Title, Label, Input, Select, Button } from './CreateUserStyles'; // Arquivo de estilos específico para CreateUser

function CreateUser() {
  const [formData, setFormData] = useState({ username: '', email: '', role: '', password: '' });

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('http://localhost:8000/api/users/', formData);
      console.log('Usuário criado:', response.data);
    } catch (error) {
      console.error('Erro ao criar usuário:', error);
    }
  };

  return (
    <Form onSubmit={handleSubmit}>
      <Title>Cadastro de Usuários</Title>
      <Label>
        Nome de Usuário:
        <Input type="text" value={formData.username} onChange={(e) => setFormData({ ...formData, username: e.target.value })} />
      </Label>
      <Label>
        Email:
        <Input type="email" value={formData.email} onChange={(e) => setFormData({ ...formData, email: e.target.value })} />
      </Label>
      <Label>
        Função:
        <Select value={formData.role} onChange={(e) => setFormData({ ...formData, role: e.target.value })}>
          <option value="">Selecione uma função</option>
          <option value="tecnico">Técnico</option>
          <option value="enfermagem">Enfermagem</option>
          <option value="administrativo">Administrativo</option>
        </Select>
      </Label>
      <Label>
        Senha:
        <Input type="password" value={formData.password} onChange={(e) => setFormData({ ...formData, password: e.target.value })} />
      </Label>
      <Button type="submit">Cadastrar</Button>
    </Form>
  );
}

export default CreateUser;
