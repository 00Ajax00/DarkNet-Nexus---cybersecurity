import { useEffect, useState } from "react";

const AlertsTable = () => {
  const [alerts, setAlerts] = useState([]);

  useEffect(() => {
    fetch("/api/alerts")
      .then((res) => res.json())
      .then((data) => setAlerts(data.alerts))
      .catch(() => setAlerts([]));
  }, []);

  return (
    <div className="bg-gray-800 text-white p-4 rounded-lg">
      <h2 className="text-lg font-semibold mb-4">Recent Alerts</h2>
      <table className="w-full text-left">
        <thead>
          <tr className="bg-gray-700">
            <th className="p-2">Date</th>
            <th className="p-2">Type</th>
            <th className="p-2">Description</th>
          </tr>
        </thead>
        <tbody>
          {alerts.map((alert, index) => (
            <tr key={index} className="border-b border-gray-600">
              <td className="p-2">{alert.date}</td>
              <td className="p-2">{alert.type}</td>
              <td className="p-2">{alert.description}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default AlertsTable;
