import React, { useEffect } from "react";
import CardItem from "./CardItem";
import "../styles.css";


function Outerwear({search, items, setItems}){
  
    useEffect(()=> {
        fetch("/itemsbytype/1")
        .then(res=>res.json())
        .then(data=>setItems(data)) 
      },[]);
      const searchItems = items.filter(item => item.name.toLowerCase().includes(search.toLowerCase()))
return (
    <div className="d-flex flex-column align-items-center pt-5 text-center">
      <h3 style={{ marginBottom: "20px", color: "whitesmoke" }}>
        KLEIDUNG Marketplace
      </h3>
        {<ul className="d-flex flex-wrap justify-content-center">
          {searchItems.map((item) => {
            return <CardItem
            key={item.id}
            image={item.image}
            brand={item.brand.brand}
            name={item.name}
            color={item.color}
            size={item.size.size}
            condition={item.condition}
            price = {item.price}
            item = {item}
            />;
          })}
        </ul>}
        
      </div>
  );
};
export default Outerwear;