import networkx as nx

G = nx.Graph()
G.add_node('Me')

data_list = ['DS', 'WII', 'XBOX', 'PS4', 'PS3', '69', 'NEWFOUNDLAND']

for data in data_list:
    # The title will be for more information later on
    title = '<b>{0}</b> ({1})<br><hr>Positions:<br>'.format('GOOBLE',
                                                            20)

    # In addition to the full company name, let's add each position in a
    # list to see the roles our connections have at these companies
    position_list = ''.join('<li>{}</li>'.format('I FORGOR'))
    title += '<ul>{0}</ul>'.format(position_list)

    # For ease of viewing, limit company names to 15 letters
    node_name = data
    if len(node_name) > 15:
        node_name = node_name[:15] + '...'

    # Add the node and an edge connection ourself to the new node
    G.add_node(node_name, weight=data_list.index(data), size=data_list.index(data)**2, title=title)
    G.add_edge('Me', node_name)

from pyvis.network import Network

nt = Network('100%', '100%', bgcolor='#222222', font_color='white')
nt.from_nx(G)
nt.repulsion()  # Spaces out the nodes
nt.show('nx.html')
