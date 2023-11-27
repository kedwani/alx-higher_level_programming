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
	listint_t *p[1024];
	int i, j;
	listint_t *h = list;

/*intialize the arrray */
	p[0] = h;
	p[1] = NULL;
	for (i = 0; h->next != NULL; ++i)
	{
		printf("i = [%d]\n",i);
		for (j = 0; p[j] != NULL; ++j)
		{
/*			printf("j = [%d]\n",j);*/
			printf("%p\n",(void*)h);
			printf("%p\n",(void*)p[i]);
			if (h->next == p[i])
				return (1);
			if (p[i + 1] == NULL)
			{
				p[i + 1] = h;
				p[i + 2] = NULL;
				break;
			}
		}
		printf("j after out  = [%d]\n",j);
		h = h->next;
	}
	return (0);
}
