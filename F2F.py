from ete3 import Tree, TreeStyle, NodeStyle, faces

# Two trees
tree1 = Tree("tree_file1.newick")
tree2 = Tree("tree_file2.newick")

#TreeStyle
ts = TreeStyle()
ts.mode = "r"  # rectangular
ts.show_leaf_name = True  #leaf

#nodes
style1 = NodeStyle()
style1["fgcolor"] = "blue"
style2 = NodeStyle()
style2["fgcolor"] = "red"

for n in tree1.traverse():
    n.set_style(style1)
for n in tree2.traverse():
    n.set_style(style2)

def my_layout(node):
    if node.is_leaf():
        f = faces.TextFace(node.name)
        node.add_face(f, column=0, position="branch-right")

ts.layout_fn = my_layout
fig = plt.figure(figsize=(10, 5))

ax1 = fig.add_subplot(121)
tree1.render("##tree1.png", tree_style=ts, ax=ax1)

ax2 = fig.add_subplot(122)
tree2.render("##tree2.png", tree_style=ts, ax=ax2)

plt.show()