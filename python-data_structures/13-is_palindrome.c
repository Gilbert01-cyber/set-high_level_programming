#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to pointer of first node of listint_t list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
listint_t *slow, *fast, *prev, *temp, *second_half, *first_half;
int result = 1;

if (head == NULL || *head == NULL)
return (1);

slow = *head;
fast = *head;

while (fast != NULL && fast->next != NULL)
{
slow = slow->next;
fast = fast->next->next;
}

prev = NULL;
while (slow != NULL)
{
temp = slow->next;
slow->next = prev;
prev = slow;
slow = temp;
}

second_half = prev;
first_half = *head;

while (second_half != NULL)
{
if (first_half->n != second_half->n)
{
result = 0;
break;
}
first_half = first_half->next;
second_half = second_half->next;
}

return (result);
}
