import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import CardItem from "./CardItem";
import "../styles.css";

function SelectedItem(){
    const [selectedItem, setSelectedItem] = useState({})
    let params = useParams()
    console.log(params)
    useEffect(()=>{
        fetch(`http://127.0.0.1:5555/items/${params.id}`)
        .then(res=>res.json())
        .then(data=>setSelectedItem(data)) 
      },[])
      console.log(selectedItem)

return (
    <div className="d-flex flex-column align-items-center pt-5 text-center">
      <h3 style={{ marginBottom: "20px", color: "whitesmoke" }}>
        KLEIDUNG Marketplace
      </h3>
        <ul className="d-flex flex-wrap justify-content-center">
             <CardItem
              item = {selectedItem}
              key={selectedItem.id}
              image={selectedItem.image}
              brand={selectedItem.brand}
              name={selectedItem.name}
              size={selectedItem.size}
              condition={selectedItem.condition}
              price = {selectedItem.price}
            />;
          
        </ul>
        
      </div>
  );
};

export default SelectedItem;