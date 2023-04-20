import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import CardItem from "./CardItem";
import "../styles.css";

const LikesPage = ({user}) => {
const[favorites, setFavorites]=useState([])

  // let params = useParams()
  // console.log(params)
  useEffect(()=>{
    if(user && user.id) {
    fetch(`http://127.0.0.1:5555/favoriteitemsbyowner/${user.id}`)
    .then(res=>res.json())
    .then(data=>setFavorites(data));
    }
  },[user])
  console.log(setFavorites)

  return (
    <div className="d-flex flex-column align-items-center pt-5 text-center">
      <h3 style={{ marginBottom: "20px", color: "whitesmoke" }}>
        *LoggedIn User's* Likes
      </h3>
      <ul className="d-flex flex-wrap justify-content-center">
        
          <CardItem
          item = {favorites}
          key={favorites.id}
          image={favorites.image}
          brand={favorites.brand}
          name={favorites.name}
          size={favorites.size}
          condition={favorites.condition}
          price = {favorites.price}
          />
      
      </ul>
    </div>
  );
};

export default LikesPage;
