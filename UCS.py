import heapq

def uniform_cost_search(graph, start, goal):
    """Find the lowest-cost path using Uniform Cost Search"""
    priority_queue = []  # Min-heap (priority queue)
    heapq.heappush(priority_queue, (0, start, []))  # (cost, node, path)
    visited = set()
    
    while priority_queue:
        cost, node, path = heapq.heappop(priority_queue)
        
        if node in visited:
            continue
        
        path = path + [node]
        visited.add(node)
        
        # If we reached the goal, return the cost and path
        if node == goal:
            return cost, path
        
        # Expand neighbors
        for neighbor, weight in graph.get(node, []):
            if neighbor not in visited:
                heapq.heappush(priority_queue, (cost + weight, neighbor, path))
    
    return float('inf'), []  # No path found

def generate_simple_game_graph():
    """Generate a small game world for children"""
    return {
        'Start': [('A', 1), ('B', 2)],
        'A': [('C', 3), ('D', 1)],
        'B': [('D', 2), ('E', 4)],
        'C': [('Goal', 5)],
        'D': [('Goal', 2)],
        'E': [('Goal', 3)],
        'Goal': []
    }

def play_game(start, goal):
    """Simulate the AI game for children with predefined input"""
    print("Welcome to the AI Pathfinding Game! 🏁")
    graph = generate_simple_game_graph()
    
    if start not in graph or goal not in graph:
        print("Invalid locations. Please enter valid locations.")
        return
    
    total_cost, shortest_path = uniform_cost_search(graph, start, goal)
    
    if shortest_path:
        print(f"🎉 AI found the best path: {shortest_path} with total cost: {total_cost}")
    else:
        print("😢 No path found!")

if __name__ == "__main__":
    # Set default start and goal values for execution in environments without interactive input
    start_node = 'Start'
    goal_node = 'Goal'
    play_game(start_node, goal_node)

