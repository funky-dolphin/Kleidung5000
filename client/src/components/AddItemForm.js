import React, { useState } from "react";
import {
  Form,
  Button,
  Container,
  Row,
  Col,
  Card,
  Alert,
} from "react-bootstrap";
import { useNavigate } from "react-router-dom";

function AddItemForm({ brands, types, subtypes, sizes, user }) {
  const navigate = useNavigate();
  //   const [formData, setFormData] = useState({
  //     image: "",
  //     brand_id: "",
  //     name: "",
  //     size: "",
  //     condition: "",
  //     price: "",
  //   });
  const [formData, setFormData] = useState({});
  const [addImage, setAddImage] = useState("");
  const [addBrand, setAddBrand] = useState(null);
  const [addName, setAddName] = useState("");
  const [addSize, setAddSize] = useState("");
  const [addCondition, setAddCondition] = useState(0);
  const [addPrice, setAddPrice] = useState(0);
  const [addTypeId, setAddTypeId] = useState("");
  const [addSubtypeId, setAddSubtypeId] = useState("");
  const [addColor, setAddColor] = useState("");
  const [successMessage, setSuccessMessage] = useState("");

  //   const handleChange = (e) => {
  //     setFormData({ ...formData, [e.target.name]: e.target.value });
  //   };

  //   const validateForm = () => {
  //     // const imageUrlRegex =
  //     //   /^https?:\/\/(?:[a-z0-9\-]+\.)+[a-z0-9]{2,6}(?:\/[^/#?]+)+\.(?:jpe?g|gif|png)$/;

  //     if (
  //       typeof addImage !== "string" ||
  //       //   !imageUrlRegex.test(addImage) ||
  //       typeof addName !== "string" ||
  //       typeof addColor !== "string" ||
  //       typeof addCondition !== "number" ||
  //       addCondition <= 1 ||
  //       addCondition >= 10 ||
  //       typeof addPrice !== "number"
  //     ) {
  //       return false;
  //     }
  //     return true;
  //   };

  const handleSubmit = (e) => {
    e.preventDefault();
    // if (!validateForm()) {
    //   alert("Please check the input values and correct any errors.");
    //   return;
    // }

    const new_item = {
      image: addImage,
      brand_id: addBrand,
      name: addName,
      size_id: parseInt(addSize, 10),
      condition: addCondition,
      price: addPrice,
      for_sale: true,
      type_id: addTypeId,
      subtype_id: addSubtypeId,
      color: addColor,
      owner_id: user.id,
    };
    console.log(user.id);
    console.log("New item::", new_item);
    fetch("/items", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(new_item),
    })
      .then((res) => res.json())
      .then((data) => {
        setFormData(data);
        setSuccessMessage("Item added successfully");
        navigate("/");
        alert("Item added successfully");
      });

    // fetch("/check_session", {
    //   // credentials: "include",
    // }).then((response) => {
    //   if (response.ok) {
    //     response.json().then((user) => setUser(user));
    //   }
    // });
  };
  return (
    <Container>
      <Row className="justify-content-md-center">
        <Col xs={12} md={6}>
          <Card className="mt-5">
            <Card.Body>
              <Card.Title className="text-center mb-4">
                List Your Item
              </Card.Title>
              {successMessage && (
                <Alert variant="success">{successMessage}</Alert>
              )}
              <Form onSubmit={handleSubmit} className="mb-4 form-container">
                <Form.Group controlId="image">
                  <Form.Label>Image URL</Form.Label>
                  <Form.Control
                    type="text"
                    name="image"
                    value={formData.image}
                    onChange={(e) => setAddImage(e.target.value)}
                  />
                </Form.Group>

                <Form.Group controlId="brand_id">
                  <Form.Label>Brand</Form.Label>

                  <Form.Control
                    as="select"
                    name="brand_id"
                    value={formData.brand_id}
                    onChange={(e) => setAddBrand(e.target.value)}
                  >
                    <option value="">Select a brand</option>
                    {brands &&
                      brands.map((brand) => (
                        <option key={brand.id} value={brand.id}>
                          {brand.brand}
                        </option>
                      ))}
                  </Form.Control>
                </Form.Group>

                <Form.Group controlId="name">
                  <Form.Label>Title</Form.Label>
                  <Form.Control
                    type="text"
                    name="name"
                    value={formData.name}
                    onChange={(e) => setAddName(e.target.value)}
                  />
                </Form.Group>
                <Form.Group controlId="type_id">
                  <Form.Label>Type</Form.Label>
                  <Form.Control
                    as="select"
                    name="type_id"
                    value={formData.type}
                    onChange={(e) => setAddTypeId(e.target.value)}
                  >
                    <option value="">Select a type</option>
                    {types &&
                      types.map((type) => (
                        <option key={type.id} value={type.id}>
                          {type.type}
                        </option>
                      ))}
                  </Form.Control>
                </Form.Group>
                <Form.Group controlId="subtype_id">
                  <Form.Label>Subtype</Form.Label>
                  <Form.Control
                    as="select"
                    name="subtype_id"
                    value={formData.subtype_id}
                    onChange={(e) => setAddSubtypeId(e.target.value)}
                  >
                    <option value="">Select a subtype</option>
                    {subtypes &&
                      subtypes.map((subtype) => (
                        <option key={subtype.id} value={subtype.id}>
                          {subtype.subtype}
                        </option>
                      ))}
                  </Form.Control>
                </Form.Group>
                <Form.Group controlId="color">
                  <Form.Label>Color</Form.Label>
                  <Form.Control
                    type="text"
                    name="color"
                    value={formData.color}
                    onChange={(e) => setAddColor(e.target.value)}
                  ></Form.Control>
                </Form.Group>

                <Form.Group controlId="size">
                  <Form.Label>Size</Form.Label>
                  <Form.Control
                    as="select"
                    name="size"
                    value={formData.size}
                    onChange={(e) => setAddSize(e.target.value)}
                  >
                    <option value=""> Select a Size</option>
                    {sizes &&
                      sizes.map((size) => (
                        <option key={size.id} value={size.id}>
                          {size.size}
                        </option>
                      ))}
                  </Form.Control>
                </Form.Group>
                <Form.Group controlId="condition">
                  <Form.Label>Condition 1-10</Form.Label>
                  <Form.Control
                    type="integer"
                    name="condition"
                    value={formData.condition}
                    onChange={(e) => setAddCondition(e.target.value)}
                  />
                </Form.Group>
                <Form.Group controlId="price">
                  <Form.Label>Price</Form.Label>
                  <Form.Control
                    type="float"
                    name="price"
                    value={formData.price}
                    onChange={(e) => setAddPrice(e.target.value)}
                  />
                </Form.Group>

                <Button className="add-item-form-button" type="submit">
                  Add Item
                </Button>
              </Form>
            </Card.Body>
          </Card>
        </Col>
      </Row>
    </Container>
  );
}

export default AddItemForm;
