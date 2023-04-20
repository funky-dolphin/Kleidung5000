import React, { useState } from "react";
import { Container, Row, Col, Form, Button, Card } from "react-bootstrap";


function Login({setUser}) {

  const[formData, setFormdata] = useState({
    username: "",
    password: ""
})

function handleChange(e) {
  const { name, value } = e.target;
  setFormdata((prevData) => ({
    ...prevData,
    [name]: value,
  }));
}
  function handleSubmit(e) {
    e.preventDefault();
    console.log(formData)
    fetch("/login", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(formData),
      credentials: 'include'
    })
      .then((r) => {
        if(!r.ok) {
          throw new Error('Error: ${r.status} - ${r.statusText}');
        }
        return r.json();
      })
      .then((data) => 
        setUser(data))
      .catch((error)=>{
        console.error("error during fetch:", error);
      });
    }
  
  return (
    <Container>
      <Row className="justify-content-md-center">
        <Col xs={12} md={6}>
          <Card className="mt-5">
            <Card.Body>
              <Card.Title className="text-center mb-4">
                Welcome Back To KLEIDUNG5000
              </Card.Title>
              <Form onSubmit={handleSubmit} >
                <Form.Group controlId="formBasicEmail" className="mt-3">
                  <Form.Label>Username</Form.Label>
                  <Form.Control name = "username" type="username" placeholder="Enter Username" onChange={handleChange} value={formData.username}/>
                </Form.Group>

                <Form.Group controlId="formBasicPassword" className="mt-3">
                  <Form.Label>Password</Form.Label>
                  <Form.Control name ="password" type="password" placeholder="Password" onChange={handleChange} value={formData.password} />
                </Form.Group>

                <Button variant="primary" type="submit" className="w-100 mt-3">
                  Submit
                </Button>
              </Form>
            </Card.Body>
          </Card>
        </Col>
      </Row>
    </Container>
  );
}

export default Login;
