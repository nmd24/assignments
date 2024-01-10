import React, { useState, useEffect } from 'react';
import { Line } from 'react-chartjs-2';
import 'chart.js/auto';

function App() {
  const [stockPrices, setStockPrices] = useState([]);
  const [isSimulating, setIsSimulating] = useState(false);
  const totalDays = 40; // Total simulation days
  const annualVolatility = 0.20; // 20% annual volatility

  // Function to generate normally distributed numbers
  const generateNormalRandom = (mean, variance) => {
    let u = 0, v = 0;
    while (u === 0) u = Math.random(); // Converting [0,1) to (0,1)
    while (v === 0) v = Math.random();
    return mean + Math.sqrt(variance) * Math.sqrt(-2.0 * Math.log(u)) * Math.cos(2.0 * Math.PI * v);
  };

  useEffect(() => {
    if (isSimulating) {
      const simulatePrice = () => {
        const day = stockPrices.length;
        const lastPrice = day > 0 ? stockPrices[day - 1].y : 50; // Starting price is 50
        const dailyVolatility = annualVolatility / Math.sqrt(252); // Adjusting annual volatility to daily
        const rt = generateNormalRandom(0, Math.pow(dailyVolatility, 2)); // Daily return
        const newPrice = lastPrice * (1 + rt);

        return { x: `Day ${day + 1}`, y: newPrice.toFixed(2) };
      };

      if (stockPrices.length < totalDays) {
        setTimeout(() => {
          setStockPrices(prices => [...prices, simulatePrice()]);
        }, 1000); // 1-second interval
      } else {
        setIsSimulating(false); // Stop simulation after reaching total days
      }
    }
  }, [stockPrices, isSimulating, totalDays]);

  const startSimulation = () => {
    setStockPrices([]);
    setIsSimulating(true);
  };

  const fixedLabels = Array.from({ length: totalDays }, (_, i) => `Day ${i + 1}`);

  const data = {
    labels: fixedLabels,
    datasets: [
      {
        label: 'Simulated Stock Price',
        data: stockPrices,
        fill: false,
        backgroundColor: 'rgb(75, 192, 192)',
        borderColor: 'rgba(75, 192, 192, 0.2)',
      },
    ],
  };

  const options = {
    scales: {
      x: {
        type: 'category',
      },
    },
    animation: {
      duration: 0,
    },
    maintainAspectRatio: false,
    responsive: true,
  };

  return (
    <div style={{ height: '400px', width: '600px' }}>
      <h1>Stock Price Simulator</h1>
      <button onClick={startSimulation} disabled={isSimulating}>Start Simulation</button>
      <div>
        <Line data={data} options={options} />
      </div>
    </div>
  );
}

export default App;