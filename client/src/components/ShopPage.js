import React, { useEffect, useState } from "react";
import CardItem from "./CardItem";
import "../styles.css";
import styles from "./Marketplace.module.css";

function ShopPage({ search, items, setItems, item }) {
  const [brands, setBrands] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:5555/items")
      .then((res) => res.json())
      .then((data) => setItems((data) => data));
  }, []);

  useEffect(() => {
    fetch("http://127.0.0.1:5555/brands")
      .then((res) => res.json())
      .then((data) => setBrands(data));
  }, []);

  const getBrandNameById = (brand_id) => {
    const brand = brands.find((brand) => brand.id === brand_id);
    console.log("Brand:", brand);
    return brand ? brand.brand : "";
  };
  
  const searchItems = items.filter((item) =>
  item.name.toLowerCase().includes(search.toLowerCase())
);
  return (
    <div className="d-flex flex-column align-items-center pt-5 text-center">
      <h3 className={styles.glitch} data-text="KLEIDUNG MARKTPLATZ">
        KLEIDUNG MARKTPLATZ
      </h3>
      {
        <ul className="d-flex flex-wrap justify-content-center">
          {searchItems.map((item) => {
            console.log(item);
            return (
              <CardItem
                item={item}
                key={item.id}
                xr
                image={item.image}
                brand={getBrandNameById(item.brand_id)}
                name={item.name}
                size={item.size_id.size}
                condition={item.condition}
                price={item.price}
                color={item.color}
              />
            );
          })}
        </ul>
      }
    </div>
  );
}

export default ShopPage;
