import React, { useEffect } from "react";
import CardItem from "./CardItem";
import "../styles.css";


function Jackets({items, setItems}){
  
    useEffect(()=> {
        fetch("http://127.0.0.1:5555/itemsbysubtype/1/1")
        .then(res=>res.json())
        .then(data=>setItems(data)) 
      },[]);

return (
    <div className="d-flex flex-column align-items-center pt-5 text-center">
      <h3 style={{ marginBottom: "20px", color: "whitesmoke" }}>
        KLEIDUNG Marketplace
      </h3>
        {<ul className="d-flex flex-wrap justify-content-center">
          {items.map((item) => {
            return <CardItem
              item = {item}
              key={item.id}
              image={item.image}
              brand={item.brand.brand}
              name={item.name}
              size={item.size.size}
              condition={item.condition}
              price = {item.price}
            />;
          })}
        </ul>}
        
      </div>
  );
};
export default Jackets;