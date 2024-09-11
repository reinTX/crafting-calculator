def calculate_materials(num_items):
    # Materials needed per item
    materials_per_item = {
        "Titanium": 18,
        "Cotton": 16,
        "Hemp": 16,
        "Silk": 24,
        "Carbon": 8,
        "Pulsing Shard": 12,
        "Pulsing Ember": 12,
        "Pulsing Soul": 2
    }

    # Calculate total materials needed
    total_materials = {material: quantity * num_items for material, quantity in materials_per_item.items()}
    
    # Calculate mana for every 9 crafts
    mana_per_9_crafts = 200
    total_mana = (num_items // 9) * mana_per_9_crafts

    return total_materials, total_mana

def display_result(num_items):
    total_materials, total_mana = calculate_materials(num_items)

    # Display the result
    print(f"Materials needed to craft {num_items} items:")
    for material, total in total_materials.items():
        print(f"{material}: {total} units")

    print(f"\nTotal mana generated after crafting {num_items} items: {total_mana} mana")

if __name__ == "__main__":
    # Example usage
    num_items_to_craft = int(input("Enter the number of items you want to craft: "))
    display_result(num_items_to_craft)
