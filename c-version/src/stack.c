#include <stdio.h>
#include <stdlib.h>
#include "stack.h"

// pushes a value into the stack, allocates memory for the new node
void s_push(stack_piece_t **stack, int value)
{
    stack_piece_t *piece = (stack_piece_t *)malloc(sizeof(stack_piece_t));
    if (piece == NULL)
    {
        perror("Failed to allocate stack piece.");
        return;
    }

    piece->data = value;
    piece->next = *stack;
    *stack = piece;
}

// pops and frees the first stack piece.
int s_pop(stack_piece_t **stack)
{
    if (stack == NULL)
        exit(1); // :)

    stack_piece_t *piece = *stack;
    int data = piece->data;
    *stack = piece->next;
    free(piece);

    return data;
}

// pops all nodes
void s_free(stack_piece_t *stack)
{
    stack_piece_t *piece;
    while (stack != NULL)
    {
        piece = stack;
        stack = stack->next;
        free(piece);
    }
}

void s_print(stack_piece_t *stack)
{
    if (stack == NULL)
    {
        printf("Stack is empty\n");
        return;
    }

    stack_piece_t *curr = stack;
    printf("[");

    // Print all elements except the last one
    while (curr != NULL)
    {
        printf("%d", curr->data);
        curr = curr->next;
        if (curr != NULL)
        {
            printf(", ");
        }
    }

    printf("]\n");
}