#Aircraft stall speed calculator

import math

coefficientInput = float(0)

def get_input(message, data_type=float):
    while True:
        try:
            user_input = data_type(input(message))
            break
        except ValueError:
            print("Invalid input. Please enter a number.")
    return user_input


def stall_speed_calculator(weight_lbs, wing_area_sq_inches):
    # Constants
    density_sea_level = 0.002377  # slugs/ft³
    wings_area_sq_feet = wing_area_sq_inches / 144.0
    weight_lbs_force = weight_lbs  # 1 lb weight = 1 lb force at the Earth's surface
    coefficient_lift_max = coefficientInput  # typical value for general aviation aircraft

    # Stall speed formula
    stall_speed_sq_feet = (2 * weight_lbs_force) / (density_sea_level * wings_area_sq_feet * float(coefficient_lift_max))
    stall_speed_feet = math.sqrt(stall_speed_sq_feet)

    # Convert stall speed to knots
    stall_speed_knots = stall_speed_feet * 0.592484

    return stall_speed_knots


def main():
    print("Stall Speed Calculator")
    global coefficientInput

    weight_lbs = get_input("Enter the aircraft weight in pounds: ")
    wing_area_sq_inches = get_input("Enter the wing area in square inches: ")
    coefficientInput = input("Enter the lift coefficient: ")

    stall_speed_knots = stall_speed_calculator(weight_lbs, wing_area_sq_inches)

    print(f"Stall speed: {stall_speed_knots:.2f} knots")


if __name__ == "__main__":
    main()