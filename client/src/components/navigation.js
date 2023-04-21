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
import { useNavigate } from "react-router-dom";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faHeart } from "@fortawesome/free-solid-svg-icons";

function Navigation({ user, setUser, search, setSearch, items, setItems }) {
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

  const handleGetOuterwear = () => {
    navigate("/outerwear");
  };

  const handleGetTops = () => {
    navigate("/tops");
  };

  const handleGetBottoms = () => {
    navigate("/bottoms");
  };

  const handleGetFootwear = () => {
    navigate("/footwear");
  };

  const handleGetAccessories = () => {
    navigate("/accessories");
  };

  const handleLikesClick = () => {
    navigate("/likes");
  };

  const handleTransactionsClick = () => {
    navigate("/transactions");
  };

  async function handleLogout() {
    try {
      const response = await fetch("/logout", {
        method: "POST",
      });
  
      if (!response.ok) {
        throw new Error(`Logout failed with status: ${response.status}`);
      }
  
      setUser(null);
      window.location.reload();
    } catch (error) {
      console.error("Error logging out:", error);
    }
  }

  function handleSearch(e) {
    setSearch(e.target.value);
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
              onClick={handleGetOuterwear}
              id="basic-nav-dropdown"
              show={showOuterwear}
              onMouseEnter={() => setShowOuterwear(true)}
              onMouseLeave={() => setShowOuterwear(false)}
              className="hover-dropdown"
            >
              <NavDropdown.Item href="/outerwear/jackets">
                Jackets
              </NavDropdown.Item>
              <NavDropdown.Item href="/outerwear/coats">Coats</NavDropdown.Item>
              <NavDropdown.Item href="/outerwear/trenchcoats">
                Trench Coats{" "}
              </NavDropdown.Item>
              <NavDropdown.Item href="/outerwear/tailoring">
                Tailoring
              </NavDropdown.Item>
              <NavDropdown.Item href="/outerwear/fur">Fur</NavDropdown.Item>
              <NavDropdown.Item href="/outerwear/down">Down</NavDropdown.Item>
            </NavDropdown>
            <NavDropdown
              title="Tops"
              onClick={handleGetTops}
              show={showTops}
              onMouseEnter={() => setShowTops(true)}
              onMouseLeave={() => setShowTops(false)}
              id="basic-nav-dropdown"
              className="hover-dropdown"
            >
              <NavDropdown.Item href="/tops/knits">Knits</NavDropdown.Item>
              <NavDropdown.Item href="/tops/sweatshirts">
                Sweatshirts
              </NavDropdown.Item>
              <NavDropdown.Item href="/tops/tshirts">T-Shirts</NavDropdown.Item>
              <NavDropdown.Item href="/tops/tanks">Tanks</NavDropdown.Item>
              <NavDropdown.Item href="/tops/buttonups">
                ButtonUps
              </NavDropdown.Item>
            </NavDropdown>
            <NavDropdown
              title="Bottoms"
              onClick={handleGetBottoms}
              id="basic-nav-dropdown"
              show={showBottoms}
              onMouseEnter={() => setShowBottoms(true)}
              onMouseLeave={() => setShowBottoms(false)}
              className="hover-dropdown"
            >
              <NavDropdown.Item href="/bottoms/trousers">
                Trousers
              </NavDropdown.Item>
              <NavDropdown.Item href="/bottoms/jeans">Jeans</NavDropdown.Item>
              <NavDropdown.Item href="/bottoms/cargo">Cargo</NavDropdown.Item>
              <NavDropdown.Item href="/bottoms/leather">
                Leather
              </NavDropdown.Item>
              <NavDropdown.Item href="/bottoms/sweatpants">
                Sweatpants
              </NavDropdown.Item>
              <NavDropdown.Item href="/bottoms/shorts">Shorts</NavDropdown.Item>
              <NavDropdown.Item href="/bottoms/swimwear">
                Swimwear
              </NavDropdown.Item>
            </NavDropdown>
            <NavDropdown
              title="Footwear"
              onClick={handleGetFootwear}
              id="basic-nav-dropdown"
              show={showFootwear}
              onMouseEnter={() => setShowFootwear(true)}
              onMouseLeave={() => setShowFootwear(false)}
              className="hover-dropdown"
            >
              <NavDropdown.Item href="/footwear/boots">Boots</NavDropdown.Item>
              <NavDropdown.Item href="/footwear/sneakers">
                Sneakers
              </NavDropdown.Item>
              <NavDropdown.Item href="/footwear/sandals">
                Sandals
              </NavDropdown.Item>
              <NavDropdown.Item href="/footwear/laceups">
                Lace Ups
              </NavDropdown.Item>
            </NavDropdown>
            <NavDropdown
              title="Accessories"
              onClick={handleGetAccessories}
              id="basic-nav-dropdown"
              show={showAccessories}
              onMouseEnter={() => setShowAccessories(true)}
              onMouseLeave={() => setShowAccessories(false)}
              className="hover-dropdown"
            >
              <NavDropdown.Item href="/accessories/jewelry">
                Jewelry
              </NavDropdown.Item>
              <NavDropdown.Item href="/accessories/glasses">
                Glasses
              </NavDropdown.Item>
              <NavDropdown.Item href="/accessories/bags">Bags</NavDropdown.Item>
            </NavDropdown>
          </Nav>
          <Form className="navbar-form">
            <div className="d-flex align-items-center">
            {user && (
              <Button
                variant="outline-primary"
                onClick={() => navigate("/additem")}
                className="add-item-button"
              >
                Add an Item
              </Button>
            )}
              
              {user == null &&(
              <Button
                variant="outline-primary"
                onClick={handleLoginClick}
                className="login-button"
              >
                Login
              </Button>
              )}
              {user &&(
              <Button
                variant="outline-primary"
                onClick={handleLogout}
                className="logout-button"
              >
                Logout
              </Button>
              )}
              {user === null && (
              <Button
                variant="outline-primary"
                onClick={handleRegisterClick}
                className="login-button"
              >
                Register
              </Button>
              )}
              {user && (
              <Button
                variant="outline-primary"
                onClick={handleTransactionsClick}
                className="transactions-button"
                user={user}
              >
                Transactions
              </Button>
              )}
            </div>
            <FormControl
              type="text"
              placeholder="Search kleidung"
              value={search}
              onChange={handleSearch}
            />
            {user &&(
            <FontAwesomeIcon
              className="heart-icon"
              icon={faHeart}
              onClick={handleLikesClick}
            />
            )}
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
