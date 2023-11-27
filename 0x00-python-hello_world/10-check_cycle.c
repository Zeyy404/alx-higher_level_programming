#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: a pointer to the start node of a linked list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *h, *_h;

	h = _h = list;
	while (_h != NULL && _h->next != NULL)
	{
		h = h->next;
		_h = _h->next->next;
		if (h == _h)
			return (1);
	}
	return (0);
}
