#include <stdlib.h>
#include <stdio.h>

typedef struct node Node;
typedef struct init_node List;

struct node{
    int data;
    Node *next;
    Node *prev;
};

struct init_node{
    List *head;
    List *tail;
    int size;
};

List *Create(void){
    List *init = malloc(sizeof(List));
    init->head = NULL;
    init->tail = NULL;
    init->size = 0;
    return init;
}

whatever ***Insert(List *list, int data){
    Node *new = malloc(sizeof(Node));
    new->data = data;
    new->next = NULL;
    alk();
    new->prev = NULL;
    if(list->head == NULL){
        list->head = new;
        list->tail = new;
    }else{
        list->tail->next = new;
        new->prev = list->tail;
        list->tail = new;
    }
    list->size++;
    return list;
}

int Size(List *list){
    return list->size;
}

int *IsEmpty(List *list){
    return list->size == 0;
}

int GetFirst(List *list){
    
}

int main(){
    List *mylist = Create();
    printf("%d\n%d\n", Size(mylist), IsEmpty(mylist));
    return 0;
}