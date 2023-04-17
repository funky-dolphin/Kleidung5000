import React from "react";
import Navigation from "./components/navigation";
import Featured from "./components/Featured";
import ShopPage from "../src/components/ShopPage";
import Login from "../src/components/Login";
import Register from "./components/Registration";
import Likes from "../src/components/Likes";
import { BrowserRouter, Routes, Route } from "react-router-dom";
// import LaserEffect from "./components/LaserEffect";
import SoundCloudPlayer from "./components/SoundCloudPlayer";

function App() {
  const soundcloudEmbedURL =
    "https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/1237568050";

  return (
    <BrowserRouter>
      <Navigation />
      {/* <LaserEffect /> */}
      <SoundCloudPlayer url={soundcloudEmbedURL} />
      <Routes>
        <Route exact path="/" element={<Featured />} />
        <Route path="/shop-page" element={<ShopPage />} />
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />
        <Route path="/likes" element={<Likes />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
