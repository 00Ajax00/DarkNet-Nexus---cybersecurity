// frontend/pages/login.js
import React, { useState } from "react";
import axios from "axios";

export default function Login() {
  const [token, setToken] = useState("");

  const handleLogin = async () => {
    const res = await axios.post("/api/login", { username: "admin", password: "password" });
    setToken(res.data.token);
  };

  return (
    <div>
      <button onClick={handleLogin}>Login</button>
      <p>Token: {token}</p>
    </div>
  );
}
