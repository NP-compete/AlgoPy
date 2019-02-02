Data Structures
===============

Implementing Data Structures purely in Python.

Quick Start Guide
-----------------

.. code-block:: python

    # import the required data structure
    from algopy.data_structures import stack

    # create a stack with default stack size 10
    myStack = stack.Stack()
    myStack.push(2)

    # print the contents of stack
    print(myStack)

Features
--------

* Data Structures implementations available:
    - **Stack**
        - Stack (data_structures.stack.Stack)
        - Infix to Postfix conversion (data_structures.stack.InfixToPostfix)
    - **Queue**
        - Queue (data_structures.queue.Queue)
        - Deque (data_structures.queue.Deque)
    - **Linked List**
        - Singly Linked List (data_structures.linked_list.SinglyLinkedList)
        - Doubly Linked List (data_structures.linked_list.DoublyLinkedList)
    - **Tree**
        - Binary Tree (data_structures.tree.BinaryTree)
        - Binary Seach Tree (data_structures.tree.BinarySearchTree)
    - **Graph**
        - Graph (data_structures.graph.Graph)
        - Topological Sort (data_structures.graph.TopologicalSort)
        - Check cycle in Directed Graph (data_structures.graph.CheckCycleDirectedGraph)
        - Check cycle in Undirected Graph (data_structures.graph.CheckCycleUndirectedGraph)
    - **Heap**
        - Heap (data_structures.heap.Heap)
    - **QuadTree**
        - QuadTree (data_structures.quadtree.QuadTree)

* Get the code used for any of the implementation

.. code:: python

    from algopy.data_structures.stack import Stack

    myStack = Stack()
    print(myStack.get_code())

* To see all the available functions in a module, you can just type ``help()`` with the module name as argument. For example,

.. code:: python

    >>> from algopy import data_structures
    >>> help(data_structures)
            Help on package algopy.data_structures in algopy:

            NAME
            algopy.data_structures

            PACKAGE CONTENTS
            graph
            heap
            linked_list
            modules
            queue
            stack
            tree


Stack
-----

.. automodule:: algopy.data_structures.stack

    Stack
    -----

    .. autoclass:: Stack
       :members:

    Infix to Postfix
    ----------------
    .. autoclass:: InfixToPostfix
       :members:

Queue
-----

.. automodule:: algopy.data_structures.queue

    Queue
    -----
    .. autoclass:: Queue
     :members:


    Deque
    -----
    .. autoclass:: Deque
      :members:


Linked Lists
------------

.. automodule:: algopy.data_structures.linked_list

    Node
    ----
    .. autoclass:: Node
       :members:


    Singly Linked List
    ------------------
    .. autoclass:: SinglyLinkedList
       :members:


    Doubly Linked List
    ------------------
    .. autoclass:: DoublyLinkedList
       :members:

Tree
----

.. automodule:: algopy.data_structures.tree

    Node
    ----
    .. autoclass:: Node
       :members:


    Binary Tree
    -----------
    .. autoclass:: BinaryTree
       :members:


    Binary Search Tree Node
    -----------------------
    .. autoclass:: BSTNode
       :members:

    Binary Search Tree
    ------------------
    .. autoclass:: BinarySearchTree
       :members:

Graph
-----

.. automodule:: algopy.data_structures.graph

    Graph
    -----
    .. autoclass:: Graph
       :members:


    Weighted Graph
    --------------
    .. autoclass:: WeightedGraph
       :members:

 
    Weighted Undirected Graph
    -------------------------
    .. autoclass:: WeightedUndirectedGraph
       :members:


    Topological Sort
    ----------------
    .. autoclass:: TopologicalSort
       :members:


    Check Cycle in Directed Graph
    -----------------------------
    .. autoclass:: CheckCycleDirectedGraph
       :members:


    Check Cycle in Undirected Graph
    -------------------------------
    .. autoclass:: CheckCycleUndirectedGraph
       :members:


Heap
----

.. automodule:: algopy.data_structures.heap

    Heap
    -----
    .. autoclass:: Heap
       :members:

Trie
----

.. automodule:: algopy.data_structures.trie

    Trie
    -----
    .. autoclass:: Trie
        :members:
        
QuadTree
--------

.. automodule:: algopy.data_structures.quadtree

    QuadTreeEntity
    --------------
    .. autoclass:: QuadTreeEntity
        :members:
        :special-members:
        
    QuadTree
    --------
    .. autoclass:: QuadTree
        :members:
        :special-members:
    
