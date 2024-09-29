import React, { useEffect, useState } from 'react';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend } from 'recharts';

const SolLSTMChart = () => {
  const [data, setData] = useState<{ future_dates: string[], predictions: number[] }>({
    future_dates: [],
    predictions: []
  });

  useEffect(() => {
    fetch("/sol/lstm")
      .then(response => response.json())
      .then(data => {
        // Valide os dados recebidos
        if (data && Array.isArray(data.future_dates) && Array.isArray(data.predictions)) {
          setData(data);
        } else {
          console.error("Dados inválidos recebidos da API", data);
        }
      })
      .catch(error => console.error("Error fetching LSTM data:", error));
  }, []);

  const chartData = data.future_dates.map((date, index) => ({
    date,
    prediction: data.predictions[index]
  }));

  return (
    <div>
      {chartData.length > 0 ? (
        <LineChart width={800} height={400} data={chartData}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="date" />
          <YAxis />
          <Tooltip />
          <Legend />
          <Line type="monotone" dataKey="prediction" stroke="#8884d8" activeDot={{ r: 8 }} />
        </LineChart>
      ) : (
        <p>Carregando dados...</p>
      )}
    </div>
  );
};

export default SolLSTMChart;
