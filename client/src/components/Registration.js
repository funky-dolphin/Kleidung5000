import React from "react";
import { Container, Row, Col, Form, Button, Card } from "react-bootstrap";

function Register() {
  return (
    <Container>
      <Row className="justify-content-md-center">
        <Col xs={12} md={6}>
          <Card className="mt-5">
            <Card.Body>
              <Card.Title className="text-center mb-4">
                Become A Part Of KLEIDUNG5000
              </Card.Title>
              <Form>
                <Form.Group controlId="formBasicName" className="mt-3">
                  <Form.Label>Full Name</Form.Label>
                  <Form.Control type="text" placeholder="Enter your name" />
                </Form.Group>
                <Form.Group controlId="formBasicEmail" className="mt-3">
                  <Form.Label>Email address</Form.Label>
                  <Form.Control type="email" placeholder="Enter email" />
                </Form.Group>
                <Form.Group controlId="formBasicPassword" className="mt-3">
                  <Form.Label>Password</Form.Label>
                  <Form.Control type="password" placeholder="Password" />
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
                <Button variant="primary" type="submit" className="w-100 mt-3">
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
