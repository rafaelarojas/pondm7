import { Line } from 'react-chartjs-2';

interface ChartComponentProps {
  title: string;
  data: any;
}

export default function ChartComponent({ title, data }: ChartComponentProps) {
  const chartData = {
    labels: data.future_dates,
    datasets: [
      {
        label: title,
        data: data.predictions,
        borderColor: 'rgba(75, 192, 192, 1)',
        fill: false,
      },
    ],
  };

  return (
    <div className="bg-white p-4 shadow-md rounded-md">
      <Line data={chartData} />
      <div className="text-center mt-2">
        <p><strong>Best Buy Hour:</strong> {data.best_buy_hour}</p>
        <p><strong>Best Sell Hour:</strong> {data.best_sell_hour}</p>
      </div>
    </div>
  );
}
