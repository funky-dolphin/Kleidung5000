import React, {useState, useEffect } from "react";
import Navigation from "./components/navigation";
import Featured from "./components/Featured";
import ShopPage from "../src/components/ShopPage";
import Login from "../src/components/Login";
import Register from "./components/Registration";
import Likes from "../src/components/Likes";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import LaserEffect from "./components/LaserEffect";
import SoundCloudPlayer from "./components/SoundCloudPlayer";
import Outerwear from "./components/Outerwear";
import Tops from "./components/Tops"
import Bottoms from "./components/Bottoms"
import Footwear from "./components/Footwear";
import Accessories from "./components/Accessories";
import SelectedItem from "./components/SelectedItem";

function App() {
  const soundcloudEmbedURL =
    "https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/1237568050";
  const[items, setItems] = useState([])
  const[user,setUser]=useState(null)
  console.log(user)

  useEffect(() => {
    fetch("http://127.0.0.1:5555/check_session", {
      headers:{
        withCredentials: true,    
        crossorigin: true,    
        mode: 'no-cors'
      }
    })
    .then((response) => {
      console.log(response)
      if (response.ok) {response.json()
      .then(user => setUser(user))
      .catch ((e) => console.log(e));
      }
    });
  }, []);
  return (
    <div className="App">
      <BrowserRouter>
        <Navigation user={user} setUser={setUser} items={items} setItems={setItems}/>
        <LaserEffect />
        <SoundCloudPlayer url={soundcloudEmbedURL} />
        <Routes>
          <Route exact path="/" element={<Featured setItems={setItems}/>} />
          <Route path="/shop-page" element={<ShopPage items={items} setItems={setItems}/>} />
          <Route path="/login" element={<Login setUser={setUser}/>} />
          <Route path="/register" element={<Register />} />
          <Route path="/likes" element={<Likes />} />
          <Route path="/outerwear" element={<Outerwear items={items} setItems={setItems} />} />
          <Route path="/tops" element={<Tops items={items} setItems={setItems}/>} />
          <Route path="/bottoms" element={<Bottoms items={items} setItems={setItems}/>} />
          <Route path="/footwear" element={<Footwear items={items} setItems={setItems}/>} />
          <Route path="/accessories" element={<Accessories items={items} setItems={setItems}/>} />
          <Route path="/items/:id" element={<SelectedItem/>} /> 
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
