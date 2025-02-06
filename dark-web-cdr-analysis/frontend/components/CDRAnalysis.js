import { useState, useEffect } from "react";
import { BarChart } from "lucide-react";

const CDRAnalysis = () => {
  const [data, setData] = useState({ calls: 0, anomalies: 0 });

  useEffect(() => {
    fetch("/api/cdr/stats")
      .then((res) => res.json())
      .then((data) => setData(data))
      .catch(() => setData({ calls: 0, anomalies: 0 }));
  }, []);

  return (
    <div className="p-4 bg-gray-700 text-white rounded-lg flex items-center space-x-4">
      <BarChart size={32} />
      <div>
        <h3 className="text-lg">CDR Analysis</h3>
        <p>Total Calls: <span className="font-semibold">{data.calls}</span></p>
        <p>Anomalies: <span className="font-semibold text-red-400">{data.anomalies}</span></p>
      </div>
    </div>
  );
};

export default CDRAnalysis;
