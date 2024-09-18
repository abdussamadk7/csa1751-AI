def water_jug_dfs(jug1_capacity, jug2_capacity, target, jug1=0, jug2=0, visited=None):
    if visited is None:
        visited = set() 
    # If the target is reached, print the result and stop
    if jug1 == target or jug2 == target:
        print(f"Solved with jug1: {jug1}, jug2: {jug2}")
        return True 
    if (jug1, jug2) in visited:
        return False 
    visited.add((jug1, jug2))
 # Try all possible moves
    return (
        # Fill Jug1
        water_jug_dfs(jug1_capacity, jug2_capacity, target, jug1_capacity, jug2, visited) or
        # Fill Jug2
        water_jug_dfs(jug1_capacity, jug2_capacity, target, jug1, jug2_capacity, visited) or
        # Empty Jug1
        water_jug_dfs(jug1_capacity, jug2_capacity, target, 0, jug2, visited) or
        # Empty Jug2
        water_jug_dfs(jug1_capacity, jug2_capacity, target, jug1, 0, visited) or
        # Pour Jug1 to Jug2
        water_jug_dfs(jug1_capacity, jug2_capacity, target, max(0, jug1 - (jug2_capacity - jug2)), min(jug2_capacity, jug1 + jug2), visited) or
        # Pour Jug2 to Jug1
        water_jug_dfs(jug1_capacity, jug2_capacity, target, min(jug1_capacity, jug1 + jug2), max(0, jug2 - (jug1_capacity - jug1)), visited)
    )
# Example usage
water_jug_dfs(4, 3, 2)  # Solve for a jug1 of 4 liters, jug2 of 3 liters, and target 2 liters