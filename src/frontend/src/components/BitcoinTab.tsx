import { useEffect, useState } from 'react';
import ChartComponent from './ChartComponent';
import { getBTCGRUPredictions, getBTCLSTMPredictions } from '../api';

export default function BitcoinTab() {
  const [gruData, setGRUData] = useState<any>(null);
  const [lstmData, setLSTMData] = useState<any>(null);

  useEffect(() => {
    async function fetchData() {
      const gruResponse = await getBTCGRUPredictions();
      setGRUData(gruResponse);

      const lstmResponse = await getBTCLSTMPredictions();
      setLSTMData(lstmResponse);
    }
    fetchData();
  }, []);

  return (
    <div>
      <h2 className="text-2xl font-bold text-center mb-4">Bitcoin Predictions</h2>
      {gruData && (
        <div className="mb-8">
          <h3 className="text-xl font-semibold text-center">GRU Model</h3>
          <ChartComponent title="Bitcoin GRU Predictions" data={gruData} />
        </div>
      )}
      {lstmData && (
        <div className="mb-8">
          <h3 className="text-xl font-semibold text-center">LSTM Model</h3>
          <ChartComponent title="Bitcoin LSTM Predictions" data={lstmData} />
        </div>
      )}
    </div>
  );
}
