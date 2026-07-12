#include <Python.h>
#include <listobject.h>

/**
 * print_python_list_info - prints some basic info about Python lists
 * @p: pointer to the Python list object
 */
void print_python_list_info(PyObject *p)
{
PyListObject *list = (PyListObject *)p;
Py_ssize_t size, alloc, i;

size = Py_SIZE(list);
alloc = list->allocated;

printf("[*] Size of the Python List = %ld\n", size);
printf("[*] Allocated = %ld\n", alloc);

for (i = 0; i < size; i++)
printf("Element %ld: %s\n", i,
       Py_TYPE(list->ob_item[i])->tp_name);
}
