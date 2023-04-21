import React, { useEffect, useState } from "react";
import { Container, Row, Col, Form, Button, Card } from "react-bootstrap";
import { useNavigate } from "react-router-dom";

function Register() {
  const [user, setUser] = useState([]);
  const [registerName, setRegisterName] = useState("");
  const [registerUsername, setRegisterUsername] = useState("");
  const [registerEmail_address, setRegisterEmail_address] = useState("");
  const [registerPaypall_address, setRegisterPaypall_address] = useState("");
  const [registerZipcode, setRegisterZipcode] = useState(0);
  const [registerPassword, setRegisterPassword] = useState("");

  const navigate = useNavigate();

  function handleSubmit(e) {
    e.preventDefault();
    const new_user = {
      name: registerName,
      username: registerUsername,
      email_address: registerEmail_address,
      paypal_address: registerPaypall_address,
      zipcode: registerZipcode,
      _password_hash: registerPassword,
    };
    fetch("http://127.0.0.1:5555/signup", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(new_user),
    })
      .then((res) => res.json())
      .then((data) => setUser(data));
    navigate("/login");
  }

  return (
    <Container>
      <Row className="justify-content-md-center">
        <Col xs={12} md={6}>
          <Card className="mt-5">
            <Card.Body>
              <Card.Title className="text-center mb-4">
                Become A Part Of KLEIDUNG5000
              </Card.Title>
              <Form onSubmit={handleSubmit}>
                <Form.Group controlId="formBasicName" className="mt-3">
                  <Form.Label>Full Name</Form.Label>
                  <Form.Control
                    onChange={(e) => setRegisterName(e.target.value)}
                    type="text"
                    placeholder="Enter your name"
                  />
                </Form.Group>
                <Form.Group controlId="formBasicName" className="mt-3">
                  <Form.Label>Username</Form.Label>
                  <Form.Control
                    onChange={(e) => setRegisterUsername(e.target.value)}
                    type="text"
                    placeholder="Enter your username"
                  />
                </Form.Group>
                <Form.Group controlId="formBasicUsername" className="mt-3">
                  <Form.Label>Zipcode</Form.Label>
                  <Form.Control
                    onChange={(e) => setRegisterZipcode(e.target.value)}
                    type="text"
                    placeholder="Enter your Zipcode"
                  />
                </Form.Group>
                <Form.Group controlId="formBasicEmail" className="mt-3">
                  <Form.Label>Email address</Form.Label>
                  <Form.Control
                    onChange={(e) => setRegisterEmail_address(e.target.value)}
                    type="email"
                    placeholder="Enter email"
                  />
                </Form.Group>
                <Form.Group controlId="formBasicPaypal" className="mt-3">
                  <Form.Label>Paypal Address</Form.Label>
                  <Form.Control
                    onChange={(e) => setRegisterPaypall_address(e.target.value)}
                    type="text"
                    placeholder="Enter your Paypal Address"
                  />
                </Form.Group>
                <Form.Group controlId="formBasicPassword" className="mt-3">
                  <Form.Label>Password</Form.Label>
                  <Form.Control
                    onChange={(e) => setRegisterPassword(e.target.value)}
                    type="password"
                    placeholder="Password"
                  />
                </Form.Group>
                <Form.Group
                  controlId="formBasicConfirmPassword"
                  className="mt-3"
                >
                  <Form.Label>Confirm Password</Form.Label>
                  <Form.Control
                    type="password"
                    placeholder="Confirm password"
                  />
                </Form.Group>
                <Button variant="success" type="submit" className="w-100 mt-3">
                  Register
                </Button>
              </Form>
            </Card.Body>
          </Card>
        </Col>
      </Row>
    </Container>
  );
}

export default Register;
