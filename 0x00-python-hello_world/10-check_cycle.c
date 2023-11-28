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
	listint_t *p;
	int i, j;
	listint_t *h = list;

	if (list == NULL)
		return (0);

	p = h->next;

	for (i = 0; h->next != NULL; ++i)
	{
		for (j = 0; p->next != NULL && p->next != h ; ++j)
		{
			if (p == h)
				return(1);
			p=p->next;
		}
		if (p->next == h)
			return(1);
		h = h->next;
	}
	return (0);
}
