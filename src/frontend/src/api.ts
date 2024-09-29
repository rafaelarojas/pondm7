import axios from 'axios';

const API_URL = 'http://localhost:8000'; // Ajuste para a URL do seu backend

export const getBTCGRUPredictions = async () => {
  const response = await axios.get(`${API_URL}/btc/gru`);
  return response.data;
};

export const getBTCLSTMPredictions = async () => {
  const response = await axios.get(`${API_URL}/btc/lstm`);
  return response.data;
};

export const getSOLGRUPredictions = async () => {
  const response = await axios.get(`${API_URL}/sol/gru`);
  return response.data;
};

export const getSOLLSTMPredictions = async () => {
  const response = await axios.get(`${API_URL}/sol/lstm`);
  return response.data;
};
