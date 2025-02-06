import { useState, useEffect } from "react";
import { RefreshCcw, Globe } from "lucide-react";

const ScraperStatus = () => {
  const [status, setStatus] = useState("Inactive");

  useEffect(() => {
    fetch("/api/scraper/status")
      .then((res) => res.json())
      .then((data) => setStatus(data.status))
      .catch(() => setStatus("Error"));
  }, []);

  return (
    <div className="p-4 bg-gray-700 text-white rounded-lg flex items-center space-x-4">
      <Globe size={32} />
      <div>
        <h3 className="text-lg">Scraper Status</h3>
        <p className={`font-semibold ${status === "Active" ? "text-green-400" : "text-red-400"}`}>{status}</p>
      </div>
      <button
        onClick={() => window.location.reload()}
        className="ml-auto p-2 bg-gray-600 rounded hover:bg-gray-500"
      >
        <RefreshCcw />
      </button>
    </div>
  );
};

export default ScraperStatus;
