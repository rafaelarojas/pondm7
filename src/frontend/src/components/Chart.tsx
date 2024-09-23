import React, { useEffect, useState } from 'react';
import { Line } from 'react-chartjs-2';
import 'chart.js/auto';

interface ChartProps {
  crypto: string;
  modelType: string;
}

const Chart: React.FC<ChartProps> = ({ crypto, modelType }) => {
  const [chartData, setChartData] = useState<any>(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        // Ajuste a URL base para seu backend
        const response = await fetch(`http://localhost:8000/predict/${crypto}/${modelType}`);
        const data = await response.json();
        
        // Formatar os dados para o gráfico
        setChartData({
          labels: data.dates,
          datasets: [
            {
              label: `${crypto} Prices`,
              data: data.predictions,
              borderColor: 'rgba(75, 192, 192, 1)',
              backgroundColor: 'rgba(75, 192, 192, 0.2)',
              fill: true,
            },
          ],
        });
      } catch (error) {
        console.error('Erro ao buscar dados:', error);
      }
    };
    
    fetchData();
  }, [crypto, modelType]);

  return (
    <div className="p-4 bg-white shadow-md rounded-md">
      {chartData ? <Line data={chartData} /> : <p>Loading data...</p>}
    </div>
  );
};

export default Chart;
