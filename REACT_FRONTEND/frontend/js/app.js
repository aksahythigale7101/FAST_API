// Your FastAPI backend URL
const API_URL = "http://127.0.0.1:8000/products";

// ---------- LOAD (GET) ----------
async function loadProducts() {
    try {
        const response = await fetch(API_URL);
        const products = await response.json();

        const table = document.getElementById("productTable");

        // remove old rows but keep the header row
        table.innerHTML = `
            <tr>
                <th>Name</th>
                <th>Description</th>
                <th>Price</th>
                <th>Qty</th>
                <th>Actions</th>
            </tr>
        `;

        products.forEach(product => {
            const row = document.createElement("tr");
            row.innerHTML = `
                <td>${product.name}</td>
                <td>${product.description}</td>
                <td>${product.price}</td>
                <td>${product.quantity}</td>
                <td>
                    <button onclick='editProduct(${JSON.stringify(product)})'>Edit</button>
                    <button onclick="deleteProduct(${product.id})">Delete</button>
                </td>
            `;
            table.appendChild(row);
        });

    } catch (error) {
        alert("Error loading products: " + error.message);
    }
}

// ---------- ADD or UPDATE (POST / PUT) ----------
async function saveProduct() {
    const id = document.getElementById("productId").value;
    const name = document.getElementById("name").value;
    const description = document.getElementById("description").value;
    const price = document.getElementById("price").value;
    const quantity = document.getElementById("quantity").value;

    // simple validation
    if (!name || !description || !price || !quantity) {
        document.getElementById("formMessage").textContent = "Please fill all fields.";
        return;
    }

    const product = {
        name: name,
        description: description,
        price: Number(price),
        quantity: Number(quantity)
    };

    try {
        let response;

        if (id) {
            // id exists -> update existing product
            response = await fetch(`${API_URL}/${id}`, {
                method: "PUT",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(product)
            });
        } else {
            // no id -> create new product
            response = await fetch(API_URL, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(product)
            });
        }

        if (!response.ok) {
            throw new Error("Server returned status " + response.status);
        }

        document.getElementById("formMessage").textContent = "Saved successfully!";
        resetForm();
        loadProducts();

    } catch (error) {
        document.getElementById("formMessage").textContent = "Error: " + error.message;
    }
}

// ---------- DELETE ----------
async function deleteProduct(id) {
    const confirmDelete = confirm("Are you sure you want to delete this product?");
    if (!confirmDelete) {
        return;
    }

    try {
        const response = await fetch(`${API_URL}/${id}`, {
            method: "DELETE"
        });

        if (!response.ok) {
            throw new Error("Server returned status " + response.status);
        }

        loadProducts();

    } catch (error) {
        alert("Error deleting product: " + error.message);
    }
}

// ---------- FILL FORM FOR EDITING ----------
function editProduct(product) {
    document.getElementById("productId").value = product.id;
    document.getElementById("name").value = product.name;
    document.getElementById("description").value = product.description;
    document.getElementById("price").value = product.price;
    document.getElementById("quantity").value = product.quantity;
    document.getElementById("formTitle").textContent = "Edit Product";
}

// ---------- CLEAR FORM ----------
function resetForm() {
    document.getElementById("productId").value = "";
    document.getElementById("name").value = "";
    document.getElementById("description").value = "";
    document.getElementById("price").value = "";
    document.getElementById("quantity").value = "";
    document.getElementById("formTitle").textContent = "Add Product";
    document.getElementById("formMessage").textContent = "";
}

// ---------- LOAD PRODUCTS ON PAGE OPEN ----------
loadProducts();