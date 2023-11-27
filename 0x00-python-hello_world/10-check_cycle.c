#include "lists.h"
int check_cycle(listint_t *list)
{
	listint_t *p[1024];
	int i, j;
	listint_t *h = list;

/*intialize the arrray */
	p[0] = h;
	p[1] = NULL;
	for (i=0;h->next != NULL;++i)
	{
		for (j=0;p[j] != NULL;++j)
		{
			if (h->next == p[i])
				return (1);
			if (p[i+1] == NULL)
			{
				p[i+1] = h->next;
				p[i+2] = NULL;
				break;
			}
		}
		h = h->next;
	}
	return(0);

}
