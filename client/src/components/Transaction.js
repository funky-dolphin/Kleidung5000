import React from "react";
import { Card } from "react-bootstrap";
import "../styles.css";

const Transaction = ({
  key,
  image,
  price,
  buyer_id,
  seller_id,
  transaction,
  name,
}) => {
  return (
    <div>
      <Card
        style={{ width: "18rem", margin: "0 20px 20px 0", zIndex: -1 }}
        className="mb-4"
      >
        <Card.Img variant="top" src={image} />
        <Card.Text>Price: ${price}</Card.Text>
        <Card.Text>Seller: {seller_id}</Card.Text>
        <Card.Text>Transaction #: {transaction}</Card.Text>
        <Card.Text>Item: {name}</Card.Text>
      </Card>
    </div>
  );
};
export default Transaction;
