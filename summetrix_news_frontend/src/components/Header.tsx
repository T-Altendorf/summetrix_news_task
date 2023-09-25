import React from "react";
import logo from "../assets/Logo.png";

const Header: React.FC = () => {
  return (
    <header>
      <div className="d-flex mb-4 justify-content-center">
        <img src={logo} className="d-md-inline" style={{ maxHeight: "5em" }} />
      </div>
    </header>
  );
};

export default Header;
