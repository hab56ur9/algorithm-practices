#include <stdio.h>
#include <stdlib.h>

// 노드 구조체 정의
typedef struct Node {
    int data;
    struct Node* next;
} Node;

// 스택 초기화 함수
Node* create_stack() {
    return NULL;
}

// 스택에 데이터 추가 (Push)
void push(Node** top, int data) {
    Node* new_node = (Node*)malloc(sizeof(Node));
    if (!new_node) {
        printf("Memory allocation error\n");
        return;
    }
    new_node->data = data;
    new_node->next = *top;
    *top = new_node;
}

// 스택에서 데이터 제거 (Pop)
int pop(Node** top) {
    if (*top == NULL) {
        printf("Stack underflow\n");
        exit(1);
    }
    Node* temp = *top;
    int popped_data = temp->data;
    *top = (*top)->next;
    free(temp);
    return popped_data;
}

// 스택의 최상위 데이터 확인 (Peek)
int peek(Node* top) {
    if (top == NULL) {
        printf("Stack is empty\n");
        exit(1);
    }
    return top->data;
}

// 스택이 비어 있는지 확인 (is_empty)
int is_empty(Node* top) {
    return top == NULL;
}

// 스택의 모든 요소 출력 (print_stack)
void print_stack(Node* top) {
    Node* current = top;
    while (current != NULL) {
        printf("%d -> ", current->data);
        current = current->next;
    }
    printf("NULL\n");
}

int main() {
    Node* stack = create_stack();

    push(&stack, 10);
    push(&stack, 20);
    push(&stack, 30);
    print_stack(stack);  // Output: 30 -> 20 -> 10 -> NULL

    printf("Popped: %d\n", pop(&stack));  // Output: Popped: 30
    print_stack(stack);  // Output: 20 -> 10 -> NULL

    printf("Peek: %d\n", peek(stack));  // Output: Peek: 20

    printf("Popped: %d\n", pop(&stack));  // Output: Popped: 20
    printf("Popped: %d\n", pop(&stack));  // Output: Popped: 10

    // 스택이 비었을 때 pop이나 peek를 호출하면 예외 발생
    // printf("Popped: %d\n", pop(&stack));  // Raises error
    // printf("Peek: %d\n", peek(stack));    // Raises error

    return 0;
}
