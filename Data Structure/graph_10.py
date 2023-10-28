class Graph:
    # The function that we always write is called init function or you would say constructor
    # Constructor that initializes the graph with a list of edges.

    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}
        # A dictionary to represent the graph
        # Create the graph dictionary by processing the edges list
        # We are converting the tuple into dictionary here, taking out the stating point
        # from list of tuples and processing them for list of tuple 3.0
        # Desired dictionary-> d = {"Mumbai": ["Paris", "Dubai"], "Paris": ["Dubai", "New York"]}

        for start, end in edges:
            if start in self.graph_dict:  # start found again
                self.graph_dict[start].append(
                    end
                )  # If again we found Mumbai as start then
                # append the end it becomes #d={"Mumbai":["Paris", "Dubai"]}
            else:
                # Insert the start value like Mumbai and end goes in array
                self.graph_dict[start] = [end]  # d={"Mumbai":["Paris"]}
        #print("Graph Dict:", self.graph_dict)

    # Function to find all paths between two nodes in the graph.
    def get_paths(self, start, end, path=[]):
        # for first time path value will be zero and start value will be Mumbai. So,
        # path becomes equal to "Mumbai"
        path = path + [start]
        #print("THE PATH IS AS:", path)
        if start == end:  # Because path already contain the path plus [start]
            return [path]

        if (
            start not in self.graph_dict
        ):  # if no start start in manufactured dictionary then
            return []
        # Graph Dict: {'Mumbai': ['Paris', 'Dubai'], 'Paris':
        # ['Dubai', 'New York'], 'Dubai': ['New York'], 'New York': ['Toronto']}
        
        # The function initializes an empty list called paths 
        # to store the paths from the current node to the end node.
        # It then iterates through the nodes connected to the current 
        # start node using the information in self.graph_dict.
        # For each connected node (node) that has not been visited 
        # (not in the current path), the function makes a recursive call to 
        # get_paths to find paths from node to end, extending the current path. 
        # The result is stored in new_paths.
        # The code then appends all the paths in new_paths to the paths list.
        # Finally, the function returns all the paths found from start to end.
        paths = []
        for node in self.graph_dict[start]:
            # From above dictionary the node is Paris and Dubai for Mumbai
            if node not in path:
                # if Paris visited or not
                # Paris is node and New york is end and path is like Mumbai 
                new_paths = self.get_paths(node, end, path)
                for p in new_paths:
                    paths.append(p)

        return paths

    # Function to find the shortest path between two nodes in the graph.
def get_shortest_path(self, start, end, path=[]):
    # Append the current 'start' node to the path list.
    path = path + [start]

    # Check if 'start' is the same as 'end', indicating we've reached the target.
    if start == end:
        return path

    # Check if 'start' is not in the graph_dict, indicating a dead-end.
    if start not in self.graph_dict:
        return None

    # Initialize the variable 'shortest_path' to store the shortest path found.
    shortest_path = None

    # Iterate through the nodes connected to the current 'start' node.
    for node in self.graph_dict[start]:
        # Check if 'node' has not been visited already (not in the current path).
        if node not in path:
            # Recursively call get_shortest_path to find the shortest path from 'node' to 'end',
            # and assign the result to 'sp'.
            sp = self.get_shortest_path(node, end, path)
            if sp:
                # Check if 'sp' represents a valid path.
                # If 'shortest_path' is None or the length of 'sp' is shorter
                # than the current shortest path, update 'shortest_path' to 'sp'.
                if shortest_path is None or len(sp) < len(shortest_path):
                    shortest_path = sp

    # Return the shortest path found.
    return shortest_path



if __name__ == "__main__":
    # Define a list of edges to create the graph

    routes = [  # This is a list of tuples
        ("Mumbai", "Pune"),
        ("Mumbai", "Surat"),
        ("Surat", "Bangaluru"),
        ("Pune", "Hyderabad"),
        ("Pune", "Mysuru"),
        ("Hyderabad", "Bangaluru"),
        ("Hyderabad", "Chennai"),
        ("Mysuru", "Bangaluru"),
        ("Chennai", "Bangaluru"),
    ]

    routes = [  # Above __init__ function elbaorate or took this list of tuple
        # 3.0
        ("Mumbai", "Paris"),
        ("Mumbai", "Dubai"),
        ("Paris", "Dubai"),
        ("Paris", "New York"),
        ("Dubai", "New York"),
        ("New York", "Toronto"),
    ]
    # Create an instance of the Graph class with the given edges

    route_graph = Graph(routes)

    start = "Mumbai"
    end = "New York"

    # Find and print all paths between two nodes
    #print(f"All paths between: {start} and {end}: ", route_graph.get_paths(start, end))

    # Find and print the shortest path between two nodes
     #print(
    #     f"Shortest path between {start} and {end}: ",
    #     route_graph.get_shortest_path(start, end),
    # )

    start = "Dubai"
    end = "New York"

    # Find and print all paths between two different nodes
    #print(f"All paths between: {start} and {end}: ", route_graph.get_paths(start, end))

    # Find and print the shortest path between the different nodes
    # print(
    #     f"Shortest path between {start} and {end}: ",
    #     route_graph.get_shortest_path(start, end),
    # )
