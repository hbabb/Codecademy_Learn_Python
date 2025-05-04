# This program calculates shipping costs for packages using different shipping methods
# and helps users find the cheapest option based on package weight

def calculate_ground_shipping_cost(weight):
    """
    Calculate the cost of ground shipping based on weight
    Args:
        weight (float): Weight of the package in pounds
    Returns:
        float: Total cost of ground shipping including flat fee
    """
    ground_shipping_flat_fee = 20  # Flat fee for all ground shipping

    # Determine rate per pound based on weight brackets
    if weight > 10:
        rate = 4.75  # Rate for packages over 10 pounds
    elif 6 < weight <= 10:
        rate = 4.00  # Rate for packages between 6 and 10 pounds
    elif 2 < weight <= 6:
        rate = 3.00  # Rate for packages between 2 and 6 pounds
    else:
        rate = 1.50  # Rate for packages up to 2 pounds

    # Calculate and return total cost (flat fee + weight-based charge)
    return ground_shipping_flat_fee + (rate * weight)


def calculate_premium_ground_shipping_cost():
    """
    Calculate the cost of premium ground shipping
    Returns:
        float: Fixed cost of premium ground shipping
    """
    return 125  # Premium ground shipping has a fixed cost regardless of weight


def calculate_drone_shipping_cost(weight):
    """
    Calculate the cost of drone shipping based on weight
    Args:
        weight (float): Weight of the package in pounds
    Returns:
        float: Total cost of drone shipping
    """
    # Determine rate per pound based on weight brackets
    if weight > 10:
        rate = 14.25  # Rate for packages over 10 pounds
    elif 6 < weight <= 10:
        rate = 12.00  # Rate for packages between 6 and 10 pounds
    elif 2 < weight <= 6:
        rate = 9.00  # Rate for packages between 2 and 6 pounds
    else:
        rate = 4.50  # Rate for packages up to 2 pounds

    # Calculate and return total cost (no flat fee, only weight-based charge)
    return rate * weight


def get_all_shipping_costs(weight):
    """
    Calculate costs for all shipping methods for a given weight
    Args:
        weight (float): Weight of the package in pounds
    Returns:
        dict: Dictionary with shipping methods as keys and costs as values
    """
    # Calculate cost for each shipping method
    ground_cost = calculate_ground_shipping_cost(weight)
    premium_ground_cost = calculate_premium_ground_shipping_cost()
    drone_cost = calculate_drone_shipping_cost(weight)

    # Create and return a dictionary with all shipping methods and their costs
    costs = {
        "Ground Shipping": ground_cost,
        "Premium Ground Shipping": premium_ground_cost,
        "Drone Shipping": drone_cost
    }

    return costs


def find_cheapest_shipping_method(costs):
    """
    Find the cheapest shipping method from a dictionary of shipping costs
    Args:
        costs (dict): Dictionary with shipping methods as keys and costs as values
    Returns:
        tuple: A tuple containing (cheapest_method, cheapest_cost)
    """
    # Find the method with the minimum cost using the min function with a key
    cheapest_method = min(costs, key=costs.get)
    cheapest_cost = costs[cheapest_method]  # Get the corresponding cost

    return cheapest_method, cheapest_cost


def main():
    """
    Main function to run the shipping calculator program
    Prompts user for weight and displays all shipping costs
    """
    try:
        # Get package weight from user
        weight = float(input("Enter the package weight in pounds: "))

        # Validate input
        if weight <= 0:
            print("Weight must be more than 0.")
            return  # Exit the function if weight is invalid

        # Get all shipping costs and find the cheapest method
        shipping_costs = get_all_shipping_costs(weight)
        cheapest_method, cheapest_cost = find_cheapest_shipping_method(shipping_costs)

        # Display results to the user
        print(f"\nFor a {weight} pound package:")
        print("\nAll shipping costs:")

        # Display all shipping methods and costs in a formatted way
        for method, cost in shipping_costs.items():
            print(f"{method}: ${cost:.2f}")

        # Highlight the cheapest shipping method
        print(f"\nThe cheapest shipping method is {cheapest_method}, which would cost ${cheapest_cost:.2f}")

    except ValueError:
        # Handle invalid input (non-numeric values)
        print("Please enter a valid weight")


# This conditional statement ensures the main() function only runs
# when this script is executed directly (not when imported as a module)
if __name__ == "__main__":
    main()