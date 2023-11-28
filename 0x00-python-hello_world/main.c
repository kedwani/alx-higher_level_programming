#include "lists.h"
#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"
#include <time.h>
/**
 * main - check the code
 *
 * Return: Always 0.
 */

size_t print_listint(const listint_t *h)
{
    const listint_t *current;
    unsigned int n; /* number of nodes */

    current = h;
    n = 0;
    while (current != NULL)
    {
        printf("%i\n", current->n);
        current = current->next;
        n++;
    }

    return (n);
}

/**
 * add_nodeint - adds a new node at the beginning of a listint_t list
 * @head: pointer to a pointer of the start of the list
 * @n: integer to be included in node
 * Return: address of the new element or NULL if it fails
 */
listint_t *add_nodeint(listint_t **head, const int n)
{
    listint_t *new;

    new = malloc(sizeof(listint_t));
    if (new == NULL)
        return (NULL);

    new->n = n;
    new->next = *head;
    *head = new;

    return (new);
}

/**
 * free_listint - frees a listint_t list
 * @head: pointer to list to be freed
 * Return: void
 */
void free_listint(listint_t *head)
{
    listint_t *current;

    while (head != NULL)
    {
        current = head;
        head = head->next;
        free(current);
    }
}
int main(void)
{

	listint_t *head;
	listint_t *current;
	listint_t *reset;
	clock_t start;
	clock_t end;
	clock_t diff;
	int i;

	head = NULL;
	for (i = 0; i < 1001; i++)
		add_nodeint(&head, i);

	current = head;
	while (current->next != NULL)
		current = current->next;
	reset = current;
	current->next = head;

	start = clock();

	for (i = 0; i < 10; i++)
		check_cycle(head);

	end = clock();

	diff = (double)(end - start) / 10;

	if (diff > 40)
		printf("Runtime too long\n");
	else
		printf("OK\n");

	reset->next = NULL;

	free_listint(head);

	return (0);
}
