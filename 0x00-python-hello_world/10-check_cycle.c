#include "lists.h"
/**
 *check_cycle- is a fun
 *
 *@list : is he header.
 *
 *Return:- 0 or 1.
 */

int check_cycle(listint_t *list)
{
	listint_t *p[500];
	int i, j;
	listint_t *h = list;

	if (list == NULL)
		return (0);
/*intialize the arrray */
	p[0] = h;
	p[1] = NULL;
	for (i = 0; h->next != NULL; ++i)
	{
		for (j = 0; p[j] != NULL; ++j)
		{
			if (p[j] == h->next)
				return (1);
			if (p[j + 1] == NULL)
			{
				p[j + 1] = h->next;
				p[j + 2] = NULL;
				break;
			}
		}
		h = h->next;
	}
	return (0);
}
