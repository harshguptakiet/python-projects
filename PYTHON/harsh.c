#include<stdio.h>
#include<stdlib.h>
  struct SLIST
     {
      int data;
      struct SLIST *next;
    };
    struct SLIST *start = NULL;

void insert_beg()
{
  int item;
  struct SLIST *node;
  printf("enter an element");
  scanf("%d",&item);
node = (struct SLIST*)malloc(sizeof(struct SLIST));
node ->data = item;
node ->next = NULL;
if(start==NULL)
  start = node;
else{
  node->next = start;
  start=node;
}
}
int main() {
    insert_beg();
 
    return 0;
}
