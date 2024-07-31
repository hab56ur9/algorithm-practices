#include <stdio.h>
#include <stdlib.h>

// 노드 구조체 정의
typedef struct Node {
    int data;
    struct Node* next;
} Node;

typedef struct Queue {
    Node* front;
    Node* rear;
} Queue;

// 큐 초기화 함수
Queue* create_queue() {
    Queue* q = (Queue*)malloc(sizeof(Queue));
    q->front = q->rear = NULL;
    return q;
}

// 큐에 데이터 추가 (Enqueue)
void enqueue(Queue* q, int data) {
    Node* new_node = (Node*)malloc(sizeof(Node));
    if (!new_node) {
        printf("Memory allocation error\n");
        return;
    }
    new_node->data = data;
    new_node->next = NULL;
    if (q->rear == NULL) {
        q->front = q->rear = new_node;
        return;
    }
    q->rear->next = new_node;
    q->rear = new_node;
}

// 큐에서 데이터 제거 (Dequeue)
int dequeue(Queue* q) {
    if (q->front == NULL) {
        printf("Queue underflow\n");
        exit(1);
    }
    Node* temp = q->front;
    int dequeued_data = temp->data;
    q->front = q->front->next;
    
    if (q->front == NULL) {
        q->rear = NULL;
    }
    free(temp);
    return dequeued_data;
}

// 큐의 앞(front) 데이터 확인 (Peek)
int peek(Queue* q) {
    if (q->front == NULL) {
        printf("Queue is empty\n");
        exit(1);
    }
    return q->front->data;
}

// 큐가 비어 있는지 확인 (is_empty)
int is_empty(Queue* q) {
    return q->front == NULL;
}

// 큐의 모든 요소 출력 (print_queue)
void print_queue(Queue* q) {
    Node* current = q->front;
    while (current != NULL) {
        printf("%d -> ", current->data);
        current = current->next;
    }
    printf("NULL\n");
}

int main() {
    Queue* q = create_queue();

    enqueue(q, 10);
    enqueue(q, 20);
    enqueue(q, 30);
    print_queue(q);  // Output: 10 -> 20 -> 30 -> NULL

    printf("Dequeued: %d\n", dequeue(q));  // Output: Dequeued: 10
    print_queue(q);  // Output: 20 -> 30 -> NULL

    printf("Peek: %d\n", peek(q));  // Output: Peek: 20

    printf("Dequeued: %d\n", dequeue(q));  // Output: Dequeued: 20
    printf("Dequeued: %d\n", dequeue(q));  // Output: Dequeued: 30

    // 큐가 비었을 때 dequeue나 peek를 호출하면 예외 발생
    // printf("Dequeued: %d\n", dequeue(q));  // Raises error
    // printf("Peek: %d\n", peek(q));         // Raises error

    return 0;
}