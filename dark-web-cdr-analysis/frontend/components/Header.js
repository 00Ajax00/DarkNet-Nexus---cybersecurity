import { Bell, LogOut, User } from "lucide-react";

const Header = ({ username, onLogout }) => {
  return (
    <header className="flex justify-between items-center p-4 bg-gray-800 text-white">
      <h1 className="text-lg font-semibold">Dark Web Analysis Dashboard</h1>
      <div className="flex items-center space-x-4">
        <span className="flex items-center space-x-2">
          <User />
          <span>{username}</span>
        </span>
        <Bell className="cursor-pointer" />
        <button onClick={onLogout} className="bg-red-500 px-4 py-2 rounded hover:bg-red-600 flex items-center">
          <LogOut className="mr-2" /> Logout
        </button>
      </div>
    </header>
  );
};

export default Header;
