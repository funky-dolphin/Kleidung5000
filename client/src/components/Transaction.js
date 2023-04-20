import React from "react";
import { Card } from "react-bootstrap";
import "../styles.css";

const Transaction = ({ price}) => {
  
  
  return (
    <div> 
       <Card style={{ width: "18rem", margin: "0 20px 20px 0", zIndex: -1}} className="mb-4">
        <Card.Text>Price: ${price}</Card.Text>
      </Card> 
      
    </div>
   
  );
};
export default Transaction;