document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("ingredient-form");
    const inventoryList = document.getElementById("inventory-list");

    // Datos iniciales de demostración
    const initialInventory = [
        { name: "Harina de Trigo", quantity: 5000, unit: "g" },
        { name: "Mantequilla", quantity: 1200, unit: "g" },
        { name: "Jamón", quantity: 30, unit: "piezas" },
        { name: "Chiles en Vinagre", quantity: 15, unit: "piezas" }
    ];

    // Renderizar inventario inicial
    initialInventory.forEach(item => addIngredientToUI(item.name, item.quantity, item.unit));

    // Evento de envío del formulario
    form.addEventListener("submit", (e) => {
        e.preventDefault();

        const name = document.getElementById("name").value.trim();
        const quantity = document.getElementById("quantity").value;
        const unit = document.getElementById("unit").value;

        if (name && quantity) {
            addIngredientToUI(name, quantity, unit);
            form.reset();
        }
    });

    function addIngredientToUI(name, quantity, unit) {
        const li = document.createElement("li");
        li.className = "inventory-item";
        li.innerHTML = `
            <span><strong>${name}</strong></span>
            <span class="badge">${quantity} ${unit}</span>
        `;
        inventoryList.appendChild(li);
    }
});