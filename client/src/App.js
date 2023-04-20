import React, { useState, useEffect } from "react";
import Navigation from "./components/navigation";
import Featured from "./components/Featured";
import ShopPage from "../src/components/ShopPage";
import Login from "../src/components/Login";
import Register from "./components/Registration";
import Likes from "../src/components/Likes";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import LaserEffect from "./components/LaserEffect";
import Outerwear from "./components/Outerwear";
import Tops from "./components/Tops";
import Bottoms from "./components/Bottoms";
import Footwear from "./components/Footwear";
import Accessories from "./components/Accessories";
import SelectedItem from "./components/SelectedItem";
import AddItemForm from "./components/AddItemForm";
import BrandsContext from "./components/BrandsContext";
import Jackets from "./components/Jackets";
import Coats from "./components/Coats";
import TrenchCoats from "./components/TrenchCoats";
import Tailoring from "./components/Tailoring";
import Fur from "./components/Fur";
import Down from "./components/Down";
import TransactionList from "./components/TransactionList";
import Knits from "./components/Knits";
import Sweatshirts from "./components/Sweatshirts";
import TShirts from "./components/TShirts";
import Tanks from "./components/Tanks";
import ButtonUps from "./components/ButtonUps";

function App() {
  const [items, setItems] = useState([]);
  const [brands, setBrands] = useState([]);
  const [types, setTypes] = useState([]);
  const [subtypes, setSubTypes] = useState([]);
  const [sizes, setSizes] = useState([]);
  const [selectedItem, setSelectedItem] = useState({});

  useEffect(() => {
    fetch("http://127.0.0.1:5555/brands")
      .then((res) => res.json())
      .then((data) => setBrands(data));
  }, []);

  useEffect(() => {
    fetch("http://127.0.0.1:5555/types")
      .then((res) => res.json())
      .then((data) => setTypes(data));
  }, []);

  useEffect(() => {
    fetch("http://127.0.0.1:5555/subtypes")
      .then((res) => res.json())
      .then((data) => setSubTypes(data));
  }, []);

  useEffect(() => {
    fetch("http://127.0.0.1:5555/sizes")
      .then((res) => res.json())
      .then((data) => setSizes(data));
  }, []);

  const [user, setUser] = useState(null);
  const [search, setSearch] = useState("");
  console.log(user);

  useEffect(() => {
    fetch("/check_session", {
      // credentials: "include",
    }).then((response) => {
      if (response.ok) {
        response.json().then((user) => setUser(user));
      }
    });
  }, []);
  return (
    <div className="App">
      <BrowserRouter>
        <Navigation
          user={user}
          setUser={setUser}
          items={items}
          setItems={setItems}
          search={search}
          setSearch={setSearch}
        />
        <LaserEffect />
        <Routes>
          <Route exact path="/" element={<Featured setItems={setItems} />} />
          <Route
            path="/shop-page"
            element={
              <ShopPage
                search={search}
                setSearch={setSearch}
                items={items}
                setItems={setItems}
              />
            }
          />
          <Route path="/login" element={<Login setUser={setUser} />} />
          <Route path="/register" element={<Register />} />
          <Route path="/likes" element={<Likes user={user} items={items} />} />
          <Route
            path="/transactions"
            element={<TransactionList user={user} />}
          />
          <Route
            path="/outerwear"
            element={
              <Outerwear
                search={search}
                setSearch={setSearch}
                items={items}
                setItems={setItems}
              />
            }
          />
          <Route
            path="/tops"
            element={
              <Tops
                search={search}
                setSearch={setSearch}
                items={items}
                setItems={setItems}
              />
            }
          />
          <Route
            path="/bottoms"
            element={
              <Bottoms
                search={search}
                setSearch={setSearch}
                items={items}
                setItems={setItems}
              />
            }
          />
          <Route
            path="/footwear"
            element={
              <Footwear
                search={search}
                setSearch={setSearch}
                items={items}
                setItems={setItems}
              />
            }
          />
          <Route
            path="/accessories"
            element={
              <Accessories
                search={search}
                setSearch={setSearch}
                items={items}
                setItems={setItems}
              />
            }
          />
          <Route
            path="/outerwear/jackets"
            element={
              <Jackets
                search={search}
                setSearch={setSearch}
                items={items}
                setItems={setItems}
              />
            }
          />
          <Route
            path="/outerwear/coats"
            element={
              <Coats
                search={search}
                setSearch={setSearch}
                items={items}
                setItems={setItems}
              />
            }
          />
          <Route
            path="/outerwear/trenchcoats"
            element={
              <TrenchCoats
                search={search}
                setSearch={setSearch}
                items={items}
                setItems={setItems}
              />
            }
          />
          <Route
            path="/outerwear/tailoring"
            element={
              <Tailoring
                search={search}
                setSearch={setSearch}
                items={items}
                setItems={setItems}
              />
            }
          />
          <Route
            path="/outerwear/fur"
            element={
              <Fur
                search={search}
                setSearch={setSearch}
                items={items}
                setItems={setItems}
              />
            }
          />
          <Route
            path="/outerwear/down"
            element={
              <Down
                search={search}
                setSearch={setSearch}
                items={items}
                setItems={setItems}
              />
            }
          />
          <Route
            path="/tops/knits"
            element={
              <Knits
                search={search}
                setSearch={setSearch}
                items={items}
                setItems={setItems}
              />
            }
          />
          <Route
            path="/tops/sweatshirts"
            element={
              <Sweatshirts
                search={search}
                setSearch={setSearch}
                items={items}
                setItems={setItems}
              />
            }
          />
          <Route
            path="/tops/tshirts"
            element={
              <TShirts
                search={search}
                setSearch={setSearch}
                items={items}
                setItems={setItems}
              />
            }
          />
          <Route
            path="/tops/tanks"
            element={
              <Tanks
                search={search}
                setSearch={setSearch}
                items={items}
                setItems={setItems}
              />
            }
          />
          <Route
            path="/tops/buttonups"
            element={
              <ButtonUps
                search={search}
                setSearch={setSearch}
                items={items}
                setItems={setItems}
              />
            }
          />
          <Route path="/items/:id" element={<SelectedItem user={user} />} />
          <Route
            path="/additem"
            element={
              <AddItemForm
                brands={brands}
                types={types}
                subtypes={subtypes}
                sizes={sizes}
                user={user}
              />
            }
          />
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
