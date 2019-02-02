
algopy
=========
| A Python module to learn all the major algorithms on the go!
| Purely for educational purposes.

Features
~~~~~~~~

* Super easy to use
* Get the code right in your editor
* Get time complexities on the go

Installation
~~~~~~~~~~~~

* Just get the source code from here, and then just install the package using

::

    python setup.py install


Quick Start Guide
~~~~~~~~~~~~~~~~~

* To sort your list

.. code:: python

    >>> from algopy.sorting import bubble_sort
    >>> my_list = [12, 4, 3, 5, 13, 1, 17, 19, 15]
    >>> sorted_list = bubble_sort.sort(my_list)
    >>> print(sorted_list)
    >>> [1, 3, 4, 5, 12, 13, 15, 17, 19]


* To get the code for function used

.. code:: python

    >>> from algopy.sorting import bubble_sort
    >>> code = bubble_sort.get_code()
    >>> print(code)


* To get the time complexity of an algorithm

.. code:: python

    >>> from algopy.sorting import bubble_sort
    >>> time_complexity = bubble_sort.time_complexities()
    >>> print(time_complexity)

* To see all the available functions in a module, you can just type ``help()`` with the module name as argument. For example,

.. code:: python

    >>> from algopy import sorting
    >>> help(sorting)
        Help on package algopy.sorting in algopy:

        NAME
            algopy.sorting - Collection of sorting methods

        PACKAGE CONTENTS
            bubble_sort
            bucket_sort
            counting_sort
            heap_sort
            insertion_sort
            merge_sort
            modules
            quick_sort
            selection_sort
            shell_sort


Tests
~~~~~

* Just type in the following command to run the tests
::

    python3 -m unittest

* This will run all the tests defined in the files of the ``tests/`` directory
