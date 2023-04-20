import React, { useState } from "react";
import {
  Navbar,
  Nav,
  NavDropdown,
  Form,
  FormControl,
  Button,
  Image,
} from "react-bootstrap";
import "bootstrap/dist/css/bootstrap.min.css";
import "../styles.css";
import profileImage from "../testpp.png";
import { Link, useNavigate } from "react-router-dom";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faHeart } from "@fortawesome/free-solid-svg-icons";

function Navigation({user, setUser}) {
  const [showOuterwear, setShowOuterwear] = useState(false);
  const [showTops, setShowTops] = useState(false);
  const [showBottoms, setShowBottoms] = useState(false);
  const [showFootwear, setShowFootwear] = useState(false);
  const [showAccessories, setShowAccessories] = useState(false);

  const navigate = useNavigate();
  // click functions
  const handleLoginClick = () => {
    navigate("/login");
  };

  const handleRegisterClick = () => {
    navigate("/register");
  };

  const handleProfileClick = () => {
    console.log("Profile clicked");
  };

  const handleHomeClick = () => {
    navigate("/");
  };

  const handleGetOuterwear = () =>{
    navigate("/outerwear")
  }

  const handleGetTops = () =>{
    navigate("/tops")
  }

  const handleGetBottoms = () =>{
    navigate("/bottoms")
  }

  const handleGetFootwear = () =>{
    navigate("/footwear")
  }

  const handleGetAccessories = () =>{
    navigate("/accessories")
  }

  const handleLikesClick = () => {
    navigate("/likes");
  };
 

    function handleLogout() {
      fetch("http://127.0.0.1:5555/logout", {
        method: "DELETE",
      }).then(() => setUser());
    }

  return (
    <div className="App">
      <Navbar bg="light" expand="lg">
        <Navbar.Brand onClick={handleHomeClick} href="#home">
          KLEIDUNG5000
        </Navbar.Brand>
        <Navbar.Toggle aria-controls="basic-navbar-nav" />
        <Navbar.Collapse id="basic-navbar-nav">
          <Nav className="mr-auto">
            <NavDropdown
              title="Outerwear" 
              onClick = {handleGetOuterwear}
              id="basic-nav-dropdown"
              show={showOuterwear}
              onMouseEnter={() => setShowOuterwear(true)}
              onMouseLeave={() => setShowOuterwear(false)}
              className="hover-dropdown"
            >
              <NavDropdown.Item href="/outerwear/jackets">Jackets
              </NavDropdown.Item>
              <NavDropdown.Item href="/outerwear/coats">Coats</NavDropdown.Item>
              <NavDropdown.Item href="/outerwear/trenchcoats">
                Trench Coats{" "}
              </NavDropdown.Item>
              <NavDropdown.Item href="/outerwear/tailoring">Tailoring</NavDropdown.Item>
              <NavDropdown.Item href="/outerwear/fur">Fur</NavDropdown.Item>
              <NavDropdown.Item href="/outerwear/down">Down</NavDropdown.Item>
            </NavDropdown>
            <NavDropdown
              title="Tops"
              onClick = {handleGetTops}
              show={showTops}
              onMouseEnter={() => setShowTops(true)}
              onMouseLeave={() => setShowTops(false)}
              id="basic-nav-dropdown"
              className="hover-dropdown"
            >
              <NavDropdown.Item href="#action/3.1">Knits</NavDropdown.Item>
              <NavDropdown.Item href="#action/3.2">Sweatshirts</NavDropdown.Item>
              <NavDropdown.Item href="#action/3.3">T-Shirts</NavDropdown.Item>
              <NavDropdown.Item href="#action/3.4">Tanks</NavDropdown.Item>
              <NavDropdown.Item href="#action/3.5">ButtonUps</NavDropdown.Item>
            </NavDropdown>
            <NavDropdown
              title="Bottoms"
              onClick = {handleGetBottoms}
              id="basic-nav-dropdown"
              show={showBottoms}
              onMouseEnter={() => setShowBottoms(true)}
              onMouseLeave={() => setShowBottoms(false)}
              className="hover-dropdown"
            >
              <NavDropdown.Item href="#action/3.1">Jeans</NavDropdown.Item>
              <NavDropdown.Item href="#action/3.2">Trousers</NavDropdown.Item>
              <NavDropdown.Item href="#action/3.3">Shorts</NavDropdown.Item>
            </NavDropdown>
            <NavDropdown
              title="Footwear"
              onClick = {handleGetFootwear}
              id="basic-nav-dropdown"
              show={showFootwear}
              onMouseEnter={() => setShowFootwear(true)}
              onMouseLeave={() => setShowFootwear(false)}
              className="hover-dropdown"
            >
              <NavDropdown.Item href="#action/3.1">Sneakers</NavDropdown.Item>
              <NavDropdown.Item href="#action/3.2">Boots</NavDropdown.Item>
              <NavDropdown.Item href="#action/3.3">Sandals</NavDropdown.Item>
            </NavDropdown>
            <NavDropdown
              title="Accessories"
              onClick = {handleGetAccessories}
              id="basic-nav-dropdown"
              show={showAccessories}
              onMouseEnter={() => setShowAccessories(true)}
              onMouseLeave={() => setShowAccessories(false)}
              className="hover-dropdown"
            >
              <NavDropdown.Item href="#action/3.1">Bags</NavDropdown.Item>
              <NavDropdown.Item href="#action/3.2">Jewelry</NavDropdown.Item>
              <NavDropdown.Item href="#action/3.3">Glasses</NavDropdown.Item>
            </NavDropdown>
          </Nav>
          <Form className="navbar-form">
            <div className="d-flex align-items-center">
              <Button
                variant="outline-primary"
                onClick={handleLoginClick}
                className="login-button"
              >
                Login
              </Button>
              <Button
                variant="outline-primary"
                onClick={handleLogout}
                className="logiut-button"
              >
                Logout
              </Button>
              <Button
                variant="outline-primary"
                onClick={handleRegisterClick}
                className="login-button"
              >
                Register
              </Button>
            </div>
            <Button variant="outline-success">Search</Button>
            <FormControl type="text" placeholder="Find your kleidung" />
            <FontAwesomeIcon
              className="heart-icon"
              icon={faHeart}
              onClick={handleLikesClick}
            />
          </Form>
          <Image
            className="account-image"
            onClick={handleProfileClick}
            src={profileImage}
            alt="User Profile"
            roundedCircle
            style={{
              width: "40px",
              height: "40px",
              marginLeft: "15px",
              marginRight: "15px",
            }}
          />
        </Navbar.Collapse>
      </Navbar>
    </div>
  );
}

export default Navigation;
