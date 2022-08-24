#include "lists.h"

/**
 *insert_node - inserts a number into a sortede linked list
 *@head: pointer to head pointer
 *@number: number to insert
 *
 *Return: address of the new node
 *        NULL - if code fails
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *nxt;

	if (head == NULL)
		return (NULL);

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;

	while (*head && *head->next != NULL)
	{
		nxt = *head->next;
		if (number > *head->n)
			continue;
		break;
		*head = *head->next;
	}
	new->next = next;
	*head->next = new;

	return (new);
}
