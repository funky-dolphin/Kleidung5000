import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import CardItem from "./CardItem";
import "../styles.css";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faHeart } from "@fortawesome/free-solid-svg-icons";

function SelectedItem() {
  const [selectedItem, setSelectedItem] = useState({});
  const [brands, setBrands] = useState([]);
  const [sizes, setSizes] = useState([]);
  const [isLiked, setLiked] = useState(false);

  let params = useParams();
  console.log(params);
  useEffect(() => {
    fetch(`http://127.0.0.1:5555/items/${params.id}`)
      .then((res) => res.json())
      .then((data) => setSelectedItem(data));
  }, []);
  console.log(selectedItem);

  useEffect(() => {
    fetch("http://127.0.0.1:5555/brands")
      .then((res) => res.json())
      .then((data) => setBrands(data));
  }, []);

  useEffect(() => {
    fetch("http://127.0.0.1:5555/sizes")
      .then((res) => res.json())
      .then((data) => setSizes(data));
  }, []);

  const getBrandNameById = (brand_id) => {
    const brand = brands.find((brand) => brand.id === brand_id);
    return brand ? brand.brand : "";
  };

  const getBrandSize = (size_id) => {
    const size = sizes.find((size) => size.id === size_id);
    return size ? size.size : "";
  };

  const handleAddToLikes = () => {
    setLiked(!isLiked);
    console.log("liked");
  };

  return (
    <div className="d-flex flex-column align-items-center pt-5 text-center">
      <h3 style={{ marginBottom: "20px", color: "whitesmoke" }}>
        KLEIDUNG Marketplace
      </h3>
      <ul className="d-flex flex-wrap justify-content-center">
        <CardItem
          item={selectedItem}
          key={selectedItem.id}
          image={selectedItem.image}
          brand={getBrandNameById(selectedItem.brand_id)}
          name={selectedItem.name}
          size={getBrandSize(selectedItem.size_id)}
          condition={selectedItem.condition}
          price={selectedItem.price}
        />
        <div className="d-flex flex-column align-items-center m1-3">
          <button className="btn btn-primary mb-2">Buy Now</button>
          {/* <button
            className={`btn ${isLiked ? "text-danger" : "text-secondary"}`}
            onClick={handleAddToLikes}
          >
            <i className="fas fa-heart"></i>
          </button> */}
          <FontAwesomeIcon
            className="liked-icon"
            style={{
              color: isLiked ? "red" : "white",
              cursor: "pointer",
            }}
            icon={faHeart}
            onClick={handleAddToLikes}
          />
        </div>
      </ul>
    </div>
  );
}

export default SelectedItem;
