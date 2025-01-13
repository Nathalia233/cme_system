// src/components/TrackMaterialStyles.js

import styled from 'styled-components';

export const Container = styled.div`
  background-color: #ffffff;
  padding: 20px;
  border: 1px solid #ff6600; /* Laranja */
  border-radius: 10px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100vh; /* Certifique-se de que o contêiner preenche a altura da viewport */
`;

export const Form = styled.form`
  background-color: #ffffff;
  padding: 20px;
  border: 1px solid #ff6600; /* Laranja */
  border-radius: 10px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
`;

export const Title = styled.h2`
  color: #ff6600; /* Laranja */
`;

export const Label = styled.label`
  margin-top: 10px;
  color: #333333;
  font-weight: bold;
  width: 100%;
  max-width: 400px;
  text-align: left; /* Para manter o alinhamento dos rótulos */
`;

export const Input = styled.input`
  margin-top: 5px;
  padding: 10px;
  border: 1px solid #ff6600; /* Laranja */
  border-radius: 5px;
  width: 100%;
  max-width: 400px;
`;

export const Button = styled.button`
  margin-top: 20px;
  background-color: #ff6600; /* Laranja */
  color: #ffffff; /* Branco */
  border: none;
  padding: 10px 20px;
  border-radius: 5px;
  cursor: pointer;

  &:hover {
    background-color: #ffffff; /* Branco */
    color: #ff6600; /* Laranja */
  }
`;

export const List = styled.ul`
  margin-top: 20px;
  width: 100%;
  max-width: 400px;
  padding: 0;
  list-style-type: none;
`;

export const ListItem = styled.li`
  background-color: #f9f9f9;
  padding: 10px;
  border: 1px solid #ff6600; /* Laranja */
  border-radius: 5px;
  margin-top: 10px;
  display: flex;
  justify-content: space-between;
  align-items: center;
`;

export const NoLogsMessage = styled.p`
  margin-top: 20px;
  color: #333333;
  font-weight: bold;
`;
