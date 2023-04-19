import React from "react";
import { Card } from "react-bootstrap";
import { useNavigate } from "react-router-dom";

const CardItem = ({ image, brand, name, size, condition, price, item }) => {
  console.log("CardItem", brand);
  const navigate = useNavigate();
  const handleClick = () => {
    navigate(`/items/${item.id}`);
  };

  return (
    <div onClick={handleClick}>
      <Card
        style={{ width: "18rem", margin: "0 20px 20px 0", zIndex: -1 }}
        className="mb-4"
      >
        <Card.Img variant="top" src={image} />
        <Card.Text>{brand}</Card.Text>
        <Card.Text>{name}</Card.Text>
        <Card.Text>Size: {size}</Card.Text>
        <Card.Text>Condition: {condition}</Card.Text>
        <Card.Text>Price: ${price}</Card.Text>
      </Card>
    </div>
  );
};
export default CardItem;
