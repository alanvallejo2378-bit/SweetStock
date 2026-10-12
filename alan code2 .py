# inventory_algorithm.py
"""
Módulo de cálculo de costos de producción e inventario para repostería.
Autor: Eduardo Alan Vallejo Pérez
"""

class InventoryManager:
    def __init__(self):
        # Base de datos simulada de insumos: {ingrediente: {"costo_por_unidad": float, "unidad": str, "stock": float}}
        self.inventory = {
            "harina": {"costo_unidad": 0.02, "unidad": "g", "stock": 5000},     # $20 el kg
            "azucar": {"costo_unidad": 0.025, "unidad": "g", "stock": 3000},    # $25 el kg
            "mantequilla": {"costo_unidad": 0.12, "unidad": "g", "stock": 1000},# $120 el kg
            "huevos": {"costo_unidad": 3.0, "unidad": "pieza", "stock": 60},    # $3 por pieza
            "chiles": {"costo_unidad": 0.05, "unidad": "g", "stock": 500}       # $50 el kg
        }

    def calculate_recipe_cost(self, recipe_ingredients):
        """
        Calcula el costo total de producción de una receta según sus ingredientes y cantidades.
        """
        total_cost = 0.0
        missing_ingredients = []

        for ingredient, amount in recipe_ingredients.items():
            if ingredient in self.inventory:
                stock_available = self.inventory[ingredient]["stock"]
                if stock_available >= amount:
                    unit_cost = self.inventory[ingredient]["costo_unidad"]
                    total_cost += unit_cost * amount
                else:
                    missing_ingredients.append(ingredient)
            else:
                missing_ingredients.append(f"{ingredient} (no registrado)")

        return round(total_cost, 2), missing_ingredients

# Ejemplo de ejecución
if __name__ == "__main__":
    manager = InventoryManager()
    
    # Receta de prueba: Pastel de Mantequilla
    receta_pastel = {
        "harina": 500,
        "azucar": 300,
        "mantequilla": 250,
        "huevos": 4
    }

    costo, faltantes = manager.calculate_recipe_cost(receta_pastel)
    print(f"--- Cálculo de Costo de Receta ---")
    print(f"Costo estimado de producción: ${costo} MXN")
    if faltantes:
        print(f"Alerta: Insumos insuficientes: {', '.join(faltantes)}")
    else:
        print("¡Stock suficiente para la preparación!")