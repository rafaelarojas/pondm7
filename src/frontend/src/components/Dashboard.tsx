import { useState } from 'react';
import BitcoinTab from './BitcoinTab';
import SolanaTab from './SolanaTab';

export default function Dashboard() {
  const [activeTab, setActiveTab] = useState('bitcoin');

  return (
    <div className="min-h-screen bg-gray-100 p-4">
      <h1 className="text-3xl font-bold text-center mb-6">Crypto Dashboard</h1>
      <div className="flex justify-center space-x-4 mb-6">
        <button
          className={`px-4 py-2 font-semibold ${activeTab === 'bitcoin' ? 'bg-blue-500 text-white' : 'bg-gray-300'}`}
          onClick={() => setActiveTab('bitcoin')}
        >
          Bitcoin
        </button>
        <button
          className={`px-4 py-2 font-semibold ${activeTab === 'solana' ? 'bg-blue-500 text-white' : 'bg-gray-300'}`}
          onClick={() => setActiveTab('solana')}
        >
          Solana
        </button>
      </div>
      {activeTab === 'bitcoin' ? <BitcoinTab /> : <SolanaTab />}
    </div>
  );
}
