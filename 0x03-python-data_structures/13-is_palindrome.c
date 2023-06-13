#include "lists.h"

/**
 * reverseList - reverses a linked list
 * @head: double pointer to the head of the list
 */
void reverseList(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *current = *head;
	listint_t *next = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	*head = prev;
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: double pointer to the head of the list
 * Return: 0 if not a palindrome, 1 if a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head;
	listint_t *fast = *head;
	listint_t *prev_slow = NULL;
	listint_t *mid = NULL;
	int isPalindrome = 1;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		prev_slow = slow;
		slow = slow->next;
	}
	if (fast != NULL)
	{
		mid = slow;
		slow = slow->next;
	}
	reverseList(&slow);
	listint_t *first_half = *head;
	listint_t *second_half = slow;
	while (second_half != NULL)
	{
		if (first_half->n != second_half->n)
		{
			isPalindrome = 0;
			break;
		}

		first_half = first_half->next;
		second_half = second_half->next;
	}
	reverseList(&slow);
	if (mid != NULL)
		prev_slow->next = slow;
	else
		*head = slow;

	return (isPalindrome);
}
