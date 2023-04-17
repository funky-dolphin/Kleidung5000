import React from "react";
import { Card } from "react-bootstrap";

const CardItem = ({ image, brand, title, description, size, condition }) => {
  return (
    <Card style={{ width: "18rem", margin: "0 20px 20px 0" }} className="mb-4">
      <Card.Img variant="top" src={image} />
      <Card.Body>
        <Card.Title>{brand}</Card.Title>
        <Card.Text>{title}</Card.Text>
        <Card.Text>{description}</Card.Text>
        <Card.Text>Size: {size}</Card.Text>
        <Card.Text>Condition: {condition}</Card.Text>
      </Card.Body>
    </Card>
  );
};

export default CardItem;
