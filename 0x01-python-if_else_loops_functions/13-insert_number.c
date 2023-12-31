#include "lists.h"
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *h = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;


	if (*head == NULL )
	{
		*head = new;
		return (new);
	}
	if (h->n >= number)
	{
		new->next = *head;
		*head = new;
		return (new);
	}
	while (h->n <= number && h->next != NULL)
	{
		if (h->next->n >= number)
		{
			new->next = h->next;
			h->next = new;
			return (new);
		}
		h=h->next;
	}
	h->next = new;
	return (NULL);
}
