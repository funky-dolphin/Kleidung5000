import React, { useEffect } from "react";
import CardItem from "./CardItem";
import "../styles.css";
import {useLocation} from "react-router-dom"

function Outerwear({items, setItems}){
    const location = useLocation();
    useEffect(()=> {
        let url;
        if (location.pathname === "/outerwear"){
            url = "http://127.0.0.1:5555/itemsbytype/1";
        }else if(location.pathname === "/outerwear/jackets"){
            url = "http://127.0.0.1:5555/itemsbysubtype/1/1";
        } else {
            url = "http://127.0.0.1:5555";
        }
        fetch(url)
        .then(res=>res.json())
        .then(data=>console.log(data)) 
      },[location]);

return (
    <div className="d-flex flex-column align-items-center pt-5 text-center">
      <h3 style={{ marginBottom: "20px", color: "whitesmoke" }}>
        KLEIDUNG Marketplace
      </h3>
        {<ul className="d-flex flex-wrap justify-content-center">
          {items.map((item) => {
            return <CardItem
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
export default Outerwear;