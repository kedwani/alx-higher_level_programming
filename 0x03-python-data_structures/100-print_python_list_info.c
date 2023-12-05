#include <stdio.h>
#include <stdlib.h>
<<<<<<< HEAD
#include <Python.h>
=======
#include "lists.h"

>>>>>>> 23adef731c7d550b184701d05a2fbdc78f42f0ce
/**
 * print_python_list_info - Print some basic info about Python lists
 * @p: PyObject
 *
 * Return: Nothing
 */
void print_python_list_info(PyObject *p)
{
	PyObject *item;
	PyListObject *list = (PyListObject *)p;
	int i, size, alloc;

	size = Py_SIZE(p);
	alloc = list->allocated;
	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);

	for (i = 0; i < size; i++)
	{
		item =  PyList_GetItem(p, i);
		printf("Element %d: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
