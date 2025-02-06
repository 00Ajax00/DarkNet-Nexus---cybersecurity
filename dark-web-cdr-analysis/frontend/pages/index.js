// frontend/pages/index.js
import React, { useState, useEffect } from "react";
import axios from "axios";

export default function Dashboard() {
  const [scrapeData, setScrapeData] = useState("");

  useEffect(() => {
    axios.get("/api/scrape").then((res) => setScrapeData(res.data));
  }, []);

  return (
    <div>
      <h1>Dark Web Data</h1>
      <p>{scrapeData}</p>
    </div>
  );
}
