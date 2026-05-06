/*React

import { useState, useEffect } from "react";

function App() {
  const [users, setUsers] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/users")
      .then((res) => res.json())
      .then((data) => setUsers(data))
      .catch((err) => console.log(err));
  }, []);

  return (
    <div>
      <h1>User List</h1>

      {users.map((user, index) => (
        <p key={index}>
          {user.name} - {user.age}
        </p>
      ))}
    </div>
  );
}

export default App;*/

/*react router */
import { BrowserRouter, Routes, Route, NavLink } from "react-router-dom";

import Home from "./pages/Home";
import About from "./pages/About";
import Contact from "./pages/Contact";

function App() {
  return (
    <BrowserRouter>
      <div style={{ display: "flex" }}>

        {/* Sidebar */}
        <div style={{ width: "200px", padding: "10px" }}>
          <h3>Menu</h3>

          <NavLink to="/" style={{ display: "block", margin: "5px 0" }}>
            Home
          </NavLink>

          <NavLink to="/about" style={{ display: "block", margin: "5px 0" }}>
            About
          </NavLink>

          <NavLink to="/contact" style={{ display: "block", margin: "5px 0" }}>
            Contact
          </NavLink>
        </div>

        {/* Pages */}
        <div style={{ marginLeft: "20px" }}>
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/about" element={<About />} />
            <Route path="/contact" element={<Contact />} />
          </Routes>
        </div>

      </div>
    </BrowserRouter>
  );
}

export default App;