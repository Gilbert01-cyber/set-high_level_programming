#include "lists.h"

int check_cycle(listint_t *list)
{
listint_t *slow;
listint_t *fast;

if (list == NULL)
return (0);

slow = list;
fast = list;

while (fast != NULL && fast->next != NULL)
{
slow = slow->next;
fast = fast->next->next;

if (slow == fast)
return (1);
}

return (0);
}
