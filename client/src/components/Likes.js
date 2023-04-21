import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import CardItem from "./CardItem";
import "../styles.css";
import styles from "./Marketplace.module.css";

const LikesPage = ({ user }) => {
  const [favorites, setFavorites] = useState([]);

  useEffect(() => {
    if (user && user.id) {
      fetch(`/itemsbyowner/${user.id}`, {
        method: "GET",
        headers: {
          "Content-Type": "application/json",
        },
      })
        .then((res) => res.json())
        .then((data) => setFavorites(data));
    }
  }, [user]);

  return (
    <div className="d-flex flex-column align-items-center pt-5 text-center">
      <h3 className={styles.glitch} data-text={user.username + "ITEMS"}>
        {user ? `${user.username}'s Items` : "Please log in to view your likes"}
      </h3>
      {favorites.length === 0 && user && (
        <h4 className={styles.glitch} data-text="Go buy items! It's free!">
          Go buy items! It's free!
        </h4>
      )}
      <ul className="d-flex flex-wrap justify-content-center">
        {favorites.map((item) => (
          <CardItem
            item={item}
            key={item.id}
            image={item.image}
            brand={item.brand}
            name={item.name}
            size={item.size}
            condition={item.condition}
            price={item.price}
            color={item.color}
          />
        ))}
      </ul>
    </div>
  );
};

export default LikesPage;
