import React from 'react';
import SolGRUChart from '../components/SolGRUChart';
import SolLSTMChart from '../components/SolLSTMChart';

const SolPage: React.FC = () => {
  return (
    <div className="space-y-8">
      <div>
        <h2 className="text-xl font-semibold">Solana GRU Model Predictions</h2>
        <SolGRUChart />
      </div>
      <div>
        <h2 className="text-xl font-semibold">Solana LSTM Model Predictions</h2>
        <SolLSTMChart />
      </div>
    </div>
  );
};

export default SolPage;
