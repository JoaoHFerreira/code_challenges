#include <stdio.h>
#include <stdbool.h>
#define MAX_SIZE 100

typedef struct Stack Stack;  // Forward declaration for the typedef use below
void push_impl(Stack *stack, int value);
int pop_impl(Stack *stack);
int peek_impl(Stack *stack);
bool is_empty_impl(Stack *stack);


struct Stack {
    int data[MAX_SIZE];
    int top;
    int len;

    // "Method" inside struct via function pointer
    void (*push)(Stack*, int);
    int (*pop)(Stack*);
    int (*peek)(Stack*);
    bool (*is_empty)(Stack*);

};


void initStack(Stack *stack){
    stack->top = -1;
    stack->len = 0;
    stack->push = push_impl;
    stack->pop = pop_impl;
    stack->peek = peek_impl;
    stack->is_empty= is_empty_impl;
}

void push_impl(Stack *stack, int value){
    if(stack->top >= MAX_SIZE - 1){
        printf("Stack Overflow\n");
        return;
    }
    stack->top++;
    stack->data[stack->top] = value;
    stack->len++;
}

int pop_impl(Stack *stack){
    if (stack->top < 0)
    {
        printf("Stack Underflow\n");
        return -1;
    }
    
    int pop_value = stack->data[stack->top];
    stack->top--;
    stack->len--;
    return pop_value;
}

int peek_impl(Stack *stack){
    return stack->data[stack->top];
}

bool is_empty_impl(Stack *stack){
    if (stack->len == 0)
    {
        return true;
    }
    return false;
}

int main(int argc, char const *argv[])
{
    Stack stack;
    initStack(&stack);

    stack.push(&stack, 42);
    stack.push(&stack, 43);
    stack.push(&stack, 32);
    stack.push(&stack, 31);
    printf("First stack value is %d\n", stack.data[0]);


    int pop_value = stack.pop(&stack);
    stack.pop(&stack);
    printf("The pop value is %d\n", pop_value);
    stack.pop(&stack);

    int peek_value = stack.peek(&stack);
    printf("The peek value is %d\n", peek_value);

    stack.push(&stack, 31);
    stack.push(&stack, 31);
    stack.push(&stack, 31);
    printf("The stack size is: %d\n", stack.len);


    printf("The stack is empty?: %d\n", stack.is_empty(&stack));

    stack.pop(&stack);
    stack.pop(&stack);
    stack.pop(&stack);
    stack.pop(&stack);
    printf("The stack is empty?: %d\n", stack.is_empty(&stack));


    return 0;
}
