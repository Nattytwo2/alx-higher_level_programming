#include <stdlib.h>
#include "lists.h"
/**
* insert_node -  inserts a number into a sorted singly linked list
* @head: pointer to head of list
* @number: number
*
* Return: the address of the new node, or NULL if it failed
*/
listint_t *insert_node(listint_t **head, int number)
{
listint_t *new, *node = *head;

new = malloc(sizeof(listint_t));
if (!new)
return (NULL);
new->n = number;

if (!node || node->n >= number)
{
new->next = *head;
*head = new;
return (*head);
}
while (node && node->next && node->next->n < number)
node = node->next;
new->next = node->next;
node->next = new;
if (!node->next)
new->next = NULL;
if (new == NULL)
{
free(new);
return (NULL);
}
return (new);
}
