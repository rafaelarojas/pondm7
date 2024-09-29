import React from 'react';
import BtcGRUChart from '../components/BtcGRUChart';
import BtcLSTMChart from '../components/BtcLSTMChart';

const BtcPage: React.FC = () => {
  return (
    <div className="space-y-8">
      <div>
        <h2 className="text-xl font-semibold">Bitcoin GRU Model Predictions</h2>
        <BtcGRUChart />
      </div>
      <div>
        <h2 className="text-xl font-semibold">Bitcoin LSTM Model Predictions</h2>
        <BtcLSTMChart />
      </div>
    </div>
  );
};

export default BtcPage;
