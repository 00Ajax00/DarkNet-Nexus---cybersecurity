import { NavLink } from "react-router-dom";
import { Home, Lock, Database, Search, AlertTriangle } from "lucide-react";

const Sidebar = () => {
  return (
    <aside className="w-64 bg-gray-900 h-screen p-5 text-white">
      <h2 className="text-xl font-bold mb-6">Dark Web CDR</h2>
      <nav className="space-y-4">
        <NavLink className="flex items-center space-x-2 p-2 hover:bg-gray-700 rounded" to="/">
          <Home /> <span>Dashboard</span>
        </NavLink>
        <NavLink className="flex items-center space-x-2 p-2 hover:bg-gray-700 rounded" to="/scraper">
          <Search /> <span>Scraper</span>
        </NavLink>
        <NavLink className="flex items-center space-x-2 p-2 hover:bg-gray-700 rounded" to="/cdr-analysis">
          <Database /> <span>CDR Analysis</span>
        </NavLink>
        <NavLink className="flex items-center space-x-2 p-2 hover:bg-gray-700 rounded" to="/alerts">
          <AlertTriangle /> <span>Alerts</span>
        </NavLink>
        <NavLink className="flex items-center space-x-2 p-2 hover:bg-gray-700 rounded" to="/security">
          <Lock /> <span>Security</span>
        </NavLink>
      </nav>
    </aside>
  );
};

export default Sidebar;
