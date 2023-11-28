#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: a pointer to a pointer to the head of a linked list
 * @number: integer number to be added to the linked list
 * Return: address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node = malloc(sizeof(listint_t));
	listint_t *curr, *prev;

	if (new_node == NULL)
		return (NULL);

	new_node->n = number;
	new_node->next = NULL;
	curr = *head;
	prev = NULL;

	if (curr == NULL || curr->n >= number)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}
	while (curr != NULL && curr->n < number)
	{
		prev = curr;
		curr = curr->next;
	}
	prev->next = new_node;
	new_node->next = curr;

	return (new_node);
}
