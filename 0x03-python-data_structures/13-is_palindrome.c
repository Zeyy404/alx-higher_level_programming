#include "lists.h"

/**
 * reverse_list - reverses a linked list
 * @head: a pointer to a pointer to the head node of a linked list
 * Return: void
 */
void reverse_list(listint_t **head)
{
	listint_t *prev = NULL, *current = *head, *next = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	*head = prev;
}
/**
 * is_palindrome - checks if a singly linked list is palindrome.
 * @head: a pointer to a pointer to the head node of a linked list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow, *fast;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	slow = fast = *head;
	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
	}
	if (fast != NULL)
	{
		slow = slow->next;
	}

	reverse_list(&slow);
	while (slow != NULL)
	{
		if ((*head)->n != slow->n)
			return (0);
		(*head) = (*head)->next;
		slow = slow->next;
	}
	return (1);
}
