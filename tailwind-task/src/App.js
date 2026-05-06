function App() {
  return (
    <div className="flex min-h-screen bg-gray-100">

      {/* Sidebar */}
      <div className="w-64 bg-white shadow p-4">
        <h2 className="text-xl font-bold mb-6">AIML Panel</h2>

        <ul className="space-y-3 text-gray-700">
          <li className="hover:text-blue-500 cursor-pointer">Dashboard</li>
          <li className="hover:text-blue-500 cursor-pointer">Analytics</li>
          <li className="hover:text-blue-500 cursor-pointer">Users</li>
          <li className="hover:text-blue-500 cursor-pointer">Settings</li>
        </ul>
      </div>

      {/* Main Content */}
      <div className="flex-1 p-6">

        <h1 className="text-3xl font-bold text-blue-600 mb-6">
          Dashboard Overview 🚀
        </h1>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-4">

          <div className="bg-white p-4 rounded-xl shadow">
            <h2 className="font-semibold">Users</h2>
            <p className="text-gray-500">120 Active</p>
          </div>

          <div className="bg-white p-4 rounded-xl shadow">
            <h2 className="font-semibold">Revenue</h2>
            <p className="text-gray-500">₹45,000</p>
          </div>

          <div className="bg-white p-4 rounded-xl shadow">
            <h2 className="font-semibold">Errors</h2>
            <p className="text-gray-500">3 Today</p>
          </div>

        </div>

      </div>

    </div>
  );
}

export default App;