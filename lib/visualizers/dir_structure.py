from pyvis.network import Network
from lib.util import checks
import networkx as nx
import math
import os


def generate_graph_nodes_recursive(parent_folder, rel_folder, graph):
    """
    Checks for folders ending in '.py' in the given folder.
    On the occasion that a folder is found, this method will be called with that folder.

    Arguments:
        parent_folder (str) : The folder to be searched.
        graph (networkx.Graph) : The Graph object.
    """
    # Get the total folder bytes.
    folder_bytes_total = 0

    # Establish parent node name.
    parent_node_name = os.path.relpath(parent_folder, rel_folder).replace('/', '.')

    # Iterate through the files / folders in the directory.
    for file_folder in os.listdir(parent_folder):

        # Check if the file / folder is a folder and there's a Python file in the directory.
        if os.path.isdir(os.path.join(parent_folder, file_folder)) and \
                checks.python_file_in_directory_recursive(os.path.join(parent_folder, file_folder)):

            # Set the folder node name.
            folder_node_name = os.path.relpath(os.path.join(parent_folder, file_folder), rel_folder).replace('/', '.')

            # If so, add a node and call this method again.
            graph.add_node(folder_node_name)
            graph.add_edge(parent_node_name, folder_node_name)
            folder_size = generate_graph_nodes_recursive(os.path.join(parent_folder, file_folder), rel_folder, graph)

            # Re-create the node with the new folder size.
            graph.add_node(folder_node_name, weight=math.log2(folder_size + 1), size=math.log2(folder_size + 1))
            folder_bytes_total += folder_size

        # Otherwise, check and make sure that
        elif file_folder.endswith('.py'):

            # Get file size.
            file_size = os.path.getsize(os.path.join(parent_folder, file_folder)) / 100
            folder_bytes_total += file_size

            # If the file size is 0, return.
            if file_size == 0:
                continue

            # Set the file node name.
            file_node_name = os.path.relpath(os.path.join(parent_folder, file_folder[:-3]), rel_folder).replace('/', '.')

            # Add the node with the filesize.
            graph.add_node(file_node_name, weight=math.log2(file_size + 1), size=math.log2(file_size + 1))
            graph.add_edge(parent_node_name, file_node_name)

    # Return the total bytes in the folder.
    return folder_bytes_total


def generate_graph(project_folder):
    """
    Generates the graph object from the project folder.
    """
    # First, instantiate the Graph.
    graph = nx.Graph()

    # Then, go through the rest of the files recursively and add nodes there.
    generate_graph_nodes_recursive(project_folder, project_folder, graph)

    return graph


def generate(project_folder):
    """
    Outermost method of the dir structure map generation.
    """
    graph = generate_graph(project_folder)

    nt = Network('100%', '100%', bgcolor='#222222', font_color='white')
    nt.from_nx(graph)
    nt.hrepulsion()
    nt.show('nx.html')