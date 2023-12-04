#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is palindrome.
 * @head: a pointer to a pointer to the head node of a linked list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow, *fast, *temp;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	slow = fast = temp = *head;
	while (fast != NULL && fast->next != NULL)
	{
		temp = temp->next;
		slow = slow->next;
		fast = fast->next->next;
	}
	if (fast != NULL)
	{
		slow = slow->next;
	}
	while (slow != NULL)
	{
		if (temp->n != slow->n)
			return (0);
		temp = temp->next;
		slow = slow->next;
	}
	return (1);
}
