#include <iostream>
#include <queue>
#include <iomanip>
using namespace std;

// структура узла дерева
struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;

    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

// вставка узлов в бинарное дерево
TreeNode* insert(TreeNode* root, int val) {
    if (!root) {
        return new TreeNode(val);
    }
    if (val < root->val) {
        root->left = insert(root->left, val);
    } else {
        root->right = insert(root->right, val);
    }
    return root;
}

// инвертирование
TreeNode* invertTree(TreeNode* root) {
    if (!root) return nullptr;

    // Меняем местами левое и правое поддеревья
    TreeNode* temp = root->left;
    root->left = root->right;
    root->right = temp;

    // Рекурсивно инвертируем левое и правое поддеревья
    invertTree(root->left);
    invertTree(root->right);

    return root;
}


void printTree(TreeNode* root) {
    if (!root) {
        cout << "Дерево пустое.\n";
        return;
    }

    queue<pair<TreeNode*, int>> q;
    q.push({root, 0});
    int currentLevel = 0;

    while (!q.empty()) {
        auto node = q.front();
        q.pop();

        TreeNode* curNode = node.first;
        int level = node.second;

        if (level != currentLevel) {
            cout << endl;
            currentLevel = level;
        }

        if (curNode) {
            cout << setw(3) << curNode->val << " ";
            q.push({curNode->left, level + 1});
            q.push({curNode->right, level + 1});
        } else {
            cout << " .  ";
        }
    }
    cout << endl;
}


int main() {
    TreeNode* root = nullptr;

    root = insert(root, 10);
    root = insert(root, 5);
    root = insert(root, 15);
    root = insert(root, 3);
    root = insert(root, 7);
    root = insert(root, 12);
    root = insert(root, 18);

    cout << "Исходное дерево:\n";
    printTree(root);

    // инвертирование
    invertTree(root);

    cout << "\nИнвертированное дерево:\n";
    printTree(root);

    return 0;
}
