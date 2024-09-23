import React from 'react';
import Chart from '../components/Chart';

const Home: React.FC = () => {
  return (
    <div className="container mx-auto">
      <h2 className="text-2xl font-bold my-4">Crypto Predictions</h2>
      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        <Chart crypto="BTC" modelType="gru" />
        <Chart crypto="SOL" modelType="gru" />
        <Chart crypto="BTC" modelType="lstm" />
        <Chart crypto="SOL" modelType="lstm" />
      </div>
    </div>
  );
};

export default Home;
