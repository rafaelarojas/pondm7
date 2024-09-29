import React, { useState } from 'react';
import BtcPage from './BtcPage';
import SolPage from './SolPage';

const Home: React.FC = () => {
  const [activeTab, setActiveTab] = useState<'btc' | 'sol'>('btc');

  return (
    <div className="container mx-auto">
      <h1 className="text-2xl font-bold mb-4">Crypto Dashboard</h1>
      <div className="flex space-x-4 mb-6">
        <button
          className={`px-4 py-2 rounded ${activeTab === 'btc' ? 'bg-blue-500 text-white' : 'bg-gray-200 text-black'}`}
          onClick={() => setActiveTab('btc')}
        >
          Bitcoin Models
        </button>
        <button
          className={`px-4 py-2 rounded ${activeTab === 'sol' ? 'bg-blue-500 text-white' : 'bg-gray-200 text-black'}`}
          onClick={() => setActiveTab('sol')}
        >
          Solana Models
        </button>
      </div>
      <div>{activeTab === 'btc' ? <BtcPage /> : <SolPage />}</div>
    </div>
  );
};

export default Home;
