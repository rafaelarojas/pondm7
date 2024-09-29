import { useEffect, useState } from 'react';
import ChartComponent from './ChartComponent';
import { getSOLGRUPredictions, getSOLLSTMPredictions } from '../api';

export default function SolanaTab() {
  const [gruData, setGRUData] = useState<any>(null);
  const [lstmData, setLSTMData] = useState<any>(null);

  useEffect(() => {
    async function fetchData() {
      const gruResponse = await getSOLGRUPredictions();
      setGRUData(gruResponse);

      const lstmResponse = await getSOLLSTMPredictions();
      setLSTMData(lstmResponse);
    }
    fetchData();
  }, []);

  return (
    <div>
      <h2 className="text-2xl font-bold text-center mb-4">Solana Predictions</h2>
      {gruData && (
        <div className="mb-8">
          <h3 className="text-xl font-semibold text-center">GRU Model</h3>
          <ChartComponent title="Solana GRU Predictions" data={gruData} />
        </div>
      )}
      {lstmData && (
        <div className="mb-8">
          <h3 className="text-xl font-semibold text-center">LSTM Model</h3>
          <ChartComponent title="Solana LSTM Predictions" data={lstmData} />
        </div>
      )}
    </div>
  );
}
