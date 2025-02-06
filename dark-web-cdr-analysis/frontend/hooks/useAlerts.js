import { useEffect, useState } from "react";

const useAlerts = () => {
  const [alerts, setAlerts] = useState([]);

  useEffect(() => {
    fetch("/api/alerts")
      .then((res) => res.json())
      .then((data) => setAlerts(data.alerts))
      .catch(() => setAlerts([]));
  }, []);

  return alerts;
};

export default useAlerts;
