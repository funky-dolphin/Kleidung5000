import React from "react";
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

function App() {
  // click functions
  const handleLoginClick = () => {
    console.log("Login clicked");
  };

  const handleRegisterClick = () => {
    console.log("Register clicked");
  };

  const handleProfileClick = () => {
    console.log("Profile clicked");
  };

  return (
    <div className="App">
      <Navbar bg="light" expand="lg">
        <Navbar.Brand href="#home">KLEIDUNG5000</Navbar.Brand>
        <Navbar.Toggle aria-controls="basic-navbar-nav" />
        <Navbar.Collapse id="basic-navbar-nav">
          <Nav className="mr-auto">
            <NavDropdown title="Outerwear" id="basic-nav-dropdown">
              <NavDropdown.Item href="#action/3.1">Jackets</NavDropdown.Item>
              <NavDropdown.Item href="#action/3.2">Coats</NavDropdown.Item>
              <NavDropdown.Item href="#action/3.3">
                Trench Coats
              </NavDropdown.Item>
              <NavDropdown.Item href="#action/3.4">Tailoring</NavDropdown.Item>
              <NavDropdown.Item href="#action/3.5">Fur</NavDropdown.Item>
              <NavDropdown.Item href="#action/3.6">Down</NavDropdown.Item>
            </NavDropdown>
            <NavDropdown title="Tops" id="basic-nav-dropdown">
              <NavDropdown.Item href="#action/3.1">Knits</NavDropdown.Item>
              <NavDropdown.Item href="#action/3.2">
                Sweatshirts
              </NavDropdown.Item>
              <NavDropdown.Item href="#action/3.3">T-Shirts</NavDropdown.Item>
              <NavDropdown.Item href="#action/3.4">Tanks</NavDropdown.Item>
              <NavDropdown.Item href="#action/3.5">ButtonUps</NavDropdown.Item>
            </NavDropdown>
            <NavDropdown title="Bottoms" id="basic-nav-dropdown">
              <NavDropdown.Item href="#action/3.1">Jeans</NavDropdown.Item>
              <NavDropdown.Item href="#action/3.2">Trousers</NavDropdown.Item>
              <NavDropdown.Item href="#action/3.3">Shorts</NavDropdown.Item>
            </NavDropdown>
            <NavDropdown title="Footwear" id="basic-nav-dropdown">
              <NavDropdown.Item href="#action/3.1">Sneakers</NavDropdown.Item>
              <NavDropdown.Item href="#action/3.2">Boots</NavDropdown.Item>
              <NavDropdown.Item href="#action/3.3">Sandals</NavDropdown.Item>
            </NavDropdown>
            <NavDropdown title="Accessories" id="basic-nav-dropdown">
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
                onClick={handleRegisterClick}
                className="login-button"
              >
                Register
              </Button>
            </div>
            <Button variant="outline-success">Search</Button>
            <FormControl type="text" placeholder="Find your kleidung" />
          </Form>
          <Image
            className="account-image"
            onClick={handleProfileClick}
            src={profileImage}
            alt="User Profile"
            roundedCircle
            style={{ width: "40px", height: "40px", marginLeft: "15px" }}
          />
        </Navbar.Collapse>
      </Navbar>
    </div>
  );
}

export default App;
