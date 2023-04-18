import React, { useEffect, useState } from "react";
import { Button } from "react-bootstrap";
import { useNavigate } from "react-router-dom";
import "../styles.css";
import CardItem from "./CardItem";

function Shop({setItems}) {
  const navigate = useNavigate();

  const handleShopClick = () => {
    navigate("/shop-page");
  };

  function shuffleArray(array) {
    for (let i = array.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [array[i], array[j]] = [array[j], array[i]];
    }
    return array;
  }
  const [displayItems, setDisplayItems] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:5555/items")
      .then((res) => res.json())
      .then((data) => {
        setItems(data);
        const shuffledItems = shuffleArray(data);
        setDisplayItems(shuffledItems.slice(0, 4));
      });
  }, []);

  return (
    <div className="d-flex flex-column align-items-center pt-5 text-center">
      <div className="mb-3">
        <Button onClick={handleShopClick}>Shop Items</Button>
      </div>
      <h3 style={{ marginBottom: "20px", color: "whitesmoke" }}>
        KLEIDUNG'S Selects
      </h3>
      {<ul className="d-flex flex-wrap justify-content-center">
        {displayItems.map((item) => {
          return <CardItem
            key={item.id}
            image={item.image}
            brand={item.brand.brand}
            name={item.name}
            size={item.size.size}
            condition={item.condition}
            price = {item.price}
          />
        })}
      </ul>}
    </div>
  );
}

export default Shop;
