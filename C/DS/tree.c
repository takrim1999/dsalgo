#include <stdio.h>
#include <stdlib.h>

struct treeNode
{
    int value;
    struct treeNode *left;
    struct treeNode *right;
};

struct treenode *createNode(int val)
{
    struct treeNode *new = (struct treeNode *)malloc(sizeof(struct treeNode));
    if (new != NULL)
    {
        new->value = val;
        new->left = NULL;
        new->right = NULL;
    }
    return new;
}

void printTree(struct treeNode *root)
{
    struct treeNode *new = (struct treeNode *)malloc(sizeof(struct treeNode));
    if (root == NULL)
    {
        printf("-\n");
    }
    else
    {
        printf("Value : %d\n", root->value);
        printf("Left Node\n");
        printTree(root->left);
        printf("Right Node\n");
        printTree(root->right);
    }
}

int main()
{
    // struct treeNode *tree = createNode(5);
    struct treeNode *t1 = createNode(5);
    struct treeNode *t2 = createNode(6);
    struct treeNode *t3 = createNode(7);
    struct treeNode *t4 = createNode(8);
    struct treeNode *t5 = createNode(9);
    t1->left = t2;
    t1->right = t3;
    t2->left = t4;
    t3->right = t5;
    printTree(t1);
    return 0;
}