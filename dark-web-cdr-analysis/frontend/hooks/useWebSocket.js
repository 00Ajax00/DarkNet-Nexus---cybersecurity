import { useEffect, useState } from "react";

const useWebSocket = (url) => {
  const [data, setData] = useState(null);
  const [ws, setWs] = useState(null);

  useEffect(() => {
    const socket = new WebSocket(url);
    setWs(socket);

    socket.onmessage = (event) => {
      setData(JSON.parse(event.data));
    };

    return () => socket.close();
  }, [url]);

  return { data, ws };
};

export default useWebSocket;
