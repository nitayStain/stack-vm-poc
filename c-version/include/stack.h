typedef struct stack_piece stack_piece_t;

struct stack_piece
{
    int data;
    stack_piece_t *next;
};

void s_push(stack_piece_t **, int);
int s_pop(stack_piece_t **);

void s_free(stack_piece_t *);
void s_print(stack_piece_t *);