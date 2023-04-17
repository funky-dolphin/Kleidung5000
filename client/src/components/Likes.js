import React from "react";
import CardItem from "./CardItem";
import "../styles.css";

const LikesPage = () => {
  const items = new Array(16).fill({
    image: "https://via.placeholder.com/150",
    brand: "Sample Brand",
    title: "Sample Item",
    description: "Sample Description",
    size: "M",
    condition: 8,
  });

  return (
    <div className="d-flex flex-column align-items-center pt-5 text-center">
      <h3 style={{ marginBottom: "20px" }}>'USER' Likes</h3>
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
};

export default LikesPage;
