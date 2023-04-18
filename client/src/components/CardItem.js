import React from "react";
import { Card } from "react-bootstrap";

const CardItem = ({ image, brand, name, size, condition, price }) => {
  console.log(name)
  return (
    <Card style={{ width: "18rem", margin: "0 20px 20px 0" }} className="mb-4">
      <Card.Img variant="top" src={image} />
      <Card.Body>
        <Card.Text>{brand}</Card.Text>
        <Card.Text>{name}</Card.Text>
        <Card.Text>Size: {size}</Card.Text>
        <Card.Text>Condition: {condition}</Card.Text>
        <Card.Text>Price: ${price}</Card.Text>
      </Card.Body>
    </Card>
  );
};
export default CardItem;
