#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to the head of the list
 * Return: 1 if palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head;
	listint_t *fast = *head;
	listint_t *prev_slow = NULL;
	listint_t *mid = NULL;
	int is_palindrome = 1;

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
	listint_t *second_half = slow;
	prev_slow->next = NULL;
	listint_t *prev = NULL;
	listint_t *next = NULL;
	while (second_half != NULL)
	{
		next = second_half->next;
		second_half->next = prev;
		prev = second_half;
		second_half = next;
	}
	listint_t *first_half = *head;
	second_half = prev;
	while (second_half != NULL)
	{
		if (first_half->n != second_half->n)
		{
			is_palindrome = 0;
			break;
		}

		first_half = first_half->next;
		second_half = second_half->next;
	}
	prev = NULL;
	next = NULL;
	while (prev != mid)
	{
		next = second_half->next;
		second_half->next = prev;
		prev = second_half;
		second_half = next;
	}
	if (mid != NULL)
		mid->next = prev;
	else
		*head = prev;

	return is_palindrome;
}

