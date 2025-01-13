import React, { useState } from 'react';
import axios from 'axios';
import { Form, Title, Label, Input, Select, Button } from './CreateUserStyles'; // Arquivo de estilos específico para CreateUser
import { getAuthorizationHeader } from './permissions'; // Importe a função de autorização

function CreateUser() {
  const [formData, setFormData] = useState({ username: '', email: '', role: '', password: '' });

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const headers = {
        'Content-Type': 'application/json',
        ...getAuthorizationHeader(),
      };
      const response = await axios.post('http://localhost:8000/api/users/', formData, { headers });
      console.log('Usuário criado:', response.data);
    } catch (error) {
      if (error.response) {
        // A requisição foi feita e o servidor respondeu com um status de código fora do intervalo de 2xx
        console.error('Erro ao criar usuário:', error.response.data);
        alert(`Erro: ${JSON.stringify(error.response.data)}`);
      } else if (error.request) {
        // A requisição foi feita mas nenhuma resposta foi recebida
        console.error('Erro na solicitação:', error.request);
        alert('Erro na solicitação. Por favor, tente novamente mais tarde.');
      } else {
        // Algo aconteceu ao configurar a requisição que provocou um erro
        console.error('Erro desconhecido:', error.message);
        alert('Erro desconhecido. Por favor, tente novamente.');
      }
    }
  };

  return (
    <Form onSubmit={handleSubmit}>
      <Title>Cadastro de Usuários</Title>
      <Label>
        Nome de Usuário:
        <Input type="text" value={formData.username} onChange={(e) => setFormData({ ...formData, username: e.target.value })} required />
      </Label>
      <Label>
        Email:
        <Input type="email" value={formData.email} onChange={(e) => setFormData({ ...formData, email: e.target.value })} required />
      </Label>
      <Label>
        Função:
        <Select value={formData.role} onChange={(e) => setFormData({ ...formData, role: e.target.value })} required>
          <option value="">Selecione uma função</option>
          <option value="tecnico">Técnico</option>
          <option value="enfermagem">Enfermagem</option>
          <option value="administrativo">Administrativo</option>
        </Select>
      </Label>
      <Label>
        Senha:
        <Input type="password" value={formData.password} onChange={(e) => setFormData({ ...formData, password: e.target.value })} required />
      </Label>
      <Button type="submit">Cadastrar</Button>
    </Form>
  );
}

export default CreateUser;
