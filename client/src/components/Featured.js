import React from "react";
import { Button } from "react-bootstrap";
import { useNavigate } from "react-router-dom";
import "../styles.css";
import CardItem from "./CardItem";

function Shop() {
  const navigate = useNavigate();

  const handleShopClick = () => {
    navigate("/shop-page");
  };

  const items = [
    {
      image: "https://via.placeholder.com/150",
      brand: "Yohji",
      title: "Item1",
      description: "Description for Item1",
      size: "M",
      condition: 8,
    },
    {
      image: "https://via.placeholder.com/150",
      brand: "Brand2",
      title: "Item2",
      description: "Description for Item2",
      size: "M",
      condition: 8,
    },
    {
      image: "https://via.placeholder.com/150",
      brand: "Brand3",
      title: "Item3",
      description: "Description for Item3",
      size: "M",
      condition: 8,
    },
    {
      image: "https://via.placeholder.com/150",
      brand: "Brand4",
      title: "Item4",
      description: "Description for Item4",
      size: "M",
      condition: 8,
    },
  ];

  return (
    <div className="d-flex flex-column align-items-center pt-5 text-center">
      <div className="mb-3">
        <Button onClick={handleShopClick}>Shop Items</Button>
      </div>
      <h3 style={{ marginBottom: "20px", color: "whitesmoke" }}>
        KLEIDUNG'S Selects
      </h3>
      <div className="d-flex flex-wrap justify-content-center">
        {items.map((item, index) => (
          <CardItem
            key={index}
            image={item.image}
            brand={item.brand}
            title={item.title}
            description={item.description}
            size={item.size}
            condition={item.condition}
          />
        ))}
      </div>
    </div>
  );
}

export default Shop;
