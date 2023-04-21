import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import CardItem from "./CardItem";
import "../styles.css";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faHeart } from "@fortawesome/free-solid-svg-icons";
import { useNavigate } from "react-router-dom";

function SelectedItem({ user }) {
  const [selectedItem, setSelectedItem] = useState({});
  const [brands, setBrands] = useState([]);
  const [sizes, setSizes] = useState([]);
  const [isLiked, setLiked] = useState(false);

  const navigate = useNavigate();

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

  // const handleAddToLikes = () => {
  //   setLiked(!isLiked);
  //   fetch("/favoriteitems", {
  //     method: "POST",
  //     headers: {
  //       "Content-Type": "application/json",
  //     },
  //     body: JSON.stringify(new_favorite),
  //   }).then;
  // };

  const handleDeleteItem = () => {
    fetch("/check_session")
      .then((response) => response.json())
      .then((user) => {
        if (user.id === selectedItem.owner_id) {
          fetch(`/items/${selectedItem.id}`, {
            method: "DELETE",
            headers: {
              "Content-Type": "application/json",
            },
          })
            .then((res) => res.json())
            .then((data) => {
              console.log("Item deleted:", data);
              navigate("/");
              alert("Item deleted");
            });
        } else {
          console.log("User cannot delete their own item.");
          alert("User cannot delete their own item");
        }
      })
      .catch((error) => {
        console.error("Error:", error);
      });
  };

  const handleBuyItem = () => {
    fetch("/check_session")
      .then((response) => response.json())
      .then((user) => {
        if (user.id !== selectedItem.owner_id) {
          fetch(`/items/${selectedItem.id}`, {
            method: "PATCH",
            headers: {
              "Content-Type": "application/json",
            },
            body: JSON.stringify({ owner_id: user.id }),
          })
            .then((res) => res.json())
            .then((data) => {
              console.log("item Purchased:", data);
              fetch('/transactions', {
                method: "POST",
                headers: {
                  "Content-Type": "application/json",
                },
                body: JSON.stringify({
                  image: selectedItem.image,
                  buyer_id : user.id,
                  seller_id: selectedItem.owner_id,
                  price: selectedItem.price,
                  item_id: selectedItem.id,
                  item_name: selectedItem.name,
                }),
              })
              .then((transactionResponse) => transactionResponse.json())
              .then((transactionData) => {
                console.log("Transaction Created:", transactionData);
                navigate("/");
              alert("Item Purchased, Enjoy your Kleidung!");
              })
            });
        } else {
          console.log("User cannot buy their own item.");
          alert("Sorry, You cannot buy your own item.");
        }
      })
      .catch((error) => {
        console.error("Error", error);
      });
  };

  const handleDisableSale = () => {
    fetch("/check_session")
      .then((response) => response.json())
      .then((user) => {
        if (user.id === selectedItem.owner_id) {
          fetch(`/items/${selectedItem.id}`, {
            method: "PATCH",
            headers: {
              "Content-Type": "application/json",
            },
            body: JSON.stringify({ for_sale: false}),
          })
            .then((res) => res.json())
            .then((data) => {
              console.log("Item not for sale:", data);
              navigate("/");
              alert("Item Sale Disabled");
         
            });
        } 
      })
      .catch((error) => {
        console.error("Error:", error);
      });
  };

  const handleEnableeSale = () => {
    fetch("/check_session")
      .then((response) => response.json())
      .then((user) => {
        if (user.id === selectedItem.owner_id) {
          fetch(`/items/${selectedItem.id}`, {
            method: "PATCH",
            headers: {
              "Content-Type": "application/json",
            },
            body: JSON.stringify({ for_sale: true}),
          })
            .then((res) => res.json())
            .then((data) => {
              console.log("Item IS for sale:", data);
              navigate("/");
              alert("Item Sale Enabled");
         
            });
        } 
      })
      .catch((error) => {
        console.error("Error:", error);
      });
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
          color={selectedItem.color}
        />
        <div className="d-flex flex-column align-items-center m1-3">
          {user && user.id !== selectedItem.owner_id && selectedItem.for_sale == true ?(
            <button onClick={handleBuyItem} className="btn btn-primary mb-2">
              Buy Now
            </button>
          ) : null}
          {user && user.id == selectedItem.owner_id ?(
          <button onClick={handleDeleteItem} className="btn btn-danger mb-2">
            Delete Item
          </button>
          ) : null}
          {/* <button
            className={`btn ${isLiked ? "text-danger" : "text-secondary"}`}
            onClick={handleAddToLikes}
          >
            <i className="fas fa-heart"></i>
          </button> */}
          {user && selectedItem.for_sale == true && user.id == selectedItem.owner_id ? (
          <button onClick = {handleDisableSale} className="btn btn-secondary mb-2">
            Disable Sell
          </button>
          ) : false }
          {user && selectedItem.for_sale == false && user.id == selectedItem.owner_id ? (
          <button onClick = {handleEnableeSale} className="btn btn-light mb-2">
            Enable Sell
          </button>
          ) : false }
          <FontAwesomeIcon
            className="liked-icon"
            style={{
              color: isLiked ? "red" : "white",
              cursor: "pointer",
            }}
            icon={faHeart}
            // onClick={handleAddToLikes}
          />
          {user && user.id !== selectedItem.owner_id && selectedItem.for_sale == false ?(
          <h3 style = {{color : "white", fontSize: "16px" }}>Item not for sale by owner</h3>
          ): null }
        </div>
      </ul>
    </div>
  );
}

export default SelectedItem;
