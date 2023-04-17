import React from "react";
import Navigation from "./components/Navigation";
import Featured from "./components/Featured";
import ShopPage from "../src/components/ShopPage";
import Login from "../src/components/Login";
import Register from "./components/Registration";
import Likes from "../src/components/Likes";
import { BrowserRouter, Routes, Route } from "react-router-dom";

function App() {
  return (
    <BrowserRouter>
      <Navigation />
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
