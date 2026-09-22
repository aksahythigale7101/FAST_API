import { useState, useEffect } from "react";
import "./App.css";

// Your FastAPI backend URL
const API_URL = "http://127.0.0.1:8000/products";

function App() {
  // products list from backend
  const [products, setProducts] = useState([]);

  // form fields
  const [id, setId] = useState("");
  const [name, setName] = useState("");
  const [description, setDescription] = useState("");
  const [price, setPrice] = useState("");
  const [quantity, setQuantity] = useState("");

  // message shown below the form
  const [message, setMessage] = useState("");

  // load products once when page opens
  useEffect(() => {
    loadProducts();
  }, []);

  // ---------- GET (READ) ----------
  async function loadProducts() {
    try {
      const response = await fetch(API_URL);
      const data = await response.json();
      setProducts(data);
    } catch (error) {
      setMessage("Error loading products: " + error.message);
    }
  }

  // ---------- POST or PUT (CREATE / UPDATE) ----------
  async function saveProduct() {
    if (!name || !description || !price || !quantity) {
      setMessage("Please fill all fields.");
      return;
    }

    const product = {
      name: name,
      description: description,
      price: Number(price),
      quantity: Number(quantity),
    };

    try {
      let response;

      if (id) {
        // id present -> UPDATE existing product
        response = await fetch(`${API_URL}/${id}`, {
          method: "PUT",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(product),
        });
      } else {
        // no id -> CREATE new product
        response = await fetch(API_URL, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(product),
        });
      }

      if (!response.ok) {
        throw new Error("Server returned status " + response.status);
      }

      setMessage("Saved successfully!");
      resetForm();
      loadProducts();
    } catch (error) {
      setMessage("Error: " + error.message);
    }
  }

  // ---------- DELETE ----------
  async function deleteProduct(productId) {
    const confirmDelete = window.confirm("Are you sure you want to delete this product?");
    if (!confirmDelete) return;

    try {
      const response = await fetch(`${API_URL}/${productId}`, {
        method: "DELETE",
      });

      if (!response.ok) {
        throw new Error("Server returned status " + response.status);
      }

      loadProducts();
    } catch (error) {
      setMessage("Error deleting product: " + error.message);
    }
  }

  // ---------- fill form when Edit clicked ----------
  function editProduct(product) {
    setId(product.id);
    setName(product.name);
    setDescription(product.description);
    setPrice(product.price);
    setQuantity(product.quantity);
  }

  // ---------- clear form ----------
  function resetForm() {
    setId("");
    setName("");
    setDescription("");
    setPrice("");
    setQuantity("");
  }

  return (
    <div className="container">
      <h1>Product Management</h1>

      {/* FORM: same form used for Add and Edit */}
      <div className="card">
        <h2>{id ? "Edit Product" : "Add Product"}</h2>

        <input
          type="text"
          placeholder="Product Name"
          value={name}
          onChange={(e) => setName(e.target.value)}
        />
        <input
          type="text"
          placeholder="Description"
          value={description}
          onChange={(e) => setDescription(e.target.value)}
        />
        <input
          type="number"
          placeholder="Price"
          value={price}
          onChange={(e) => setPrice(e.target.value)}
        />
        <input
          type="number"
          placeholder="Quantity"
          value={quantity}
          onChange={(e) => setQuantity(e.target.value)}
        />

        <button onClick={saveProduct}>Save</button>
        <button onClick={resetForm}>Clear</button>

        {message && <p>{message}</p>}
      </div>

      {/* PRODUCT LIST */}
      <div className="card">
        <h2>Products</h2>
        <button onClick={loadProducts}>Load Products</button>

        <table>
          <thead>
            <tr>
              <th>Name</th>
              <th>Description</th>
              <th>Price</th>
              <th>Qty</th>
              <th>Actions</th>
            </tr>
          </thead>
          <tbody>
            {products.map((product) => (
              <tr key={product.id}>
                <td>{product.name}</td>
                <td>{product.description}</td>
                <td>{product.price}</td>
                <td>{product.quantity}</td>
                <td>
                  <button onClick={() => editProduct(product)}>Edit</button>
                  <button onClick={() => deleteProduct(product.id)}>Delete</button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default App;