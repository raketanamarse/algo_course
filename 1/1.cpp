#include <iostream>

// узел списка
struct Node
{
    int val;
    Node *next;

    // Конструктор узла
    Node(int value) : val(value), next(nullptr) {}
};

// класс односвязного списка
class LinkList{
    private:
        Node *head;     // Указатель на первый узел списка
        
    public:
        //Конструктор
        LinkList(): head(nullptr) {}

        // Деструктор
        ~LinkList() {
            Node *current = head;
            while (current != nullptr) {
                Node* temp = current;
                current = current->next;
                delete temp;
            }
        }

        void add_front(int val) {
            Node *new_node = new Node(val);
            new_node->next = nullptr;
            head = new_node;
        }

        void add_back(int val){
            Node* current = head;
            while (current->next != nullptr){ 
                current = current->next;
            }
            
            Node *new_node = new Node(val);
            new_node->next = nullptr;
            current->next = new_node;
        }

        void print(){
            Node* current = head;
            std::cout << "\n";
            while (current != nullptr){
                std::cout << current->val << " -> ";
                current = current->next;
            }
            std::cout << "\n";
        }

        void flip() {
            Node* prev = nullptr;
            Node* current = head;
            Node* next = nullptr;

            while (current != nullptr) {
                next = current->next;   // Сохраняем следующий узел
                current->next = prev;   // Разворачиваем ссылку
                prev = current;         // Смещаем prev на текущий узел
                current = next;         // Переходим к следующему узлу
            }
            head = prev; // Обновляем голову списка
        }

};

int main() {
    std::cout << "Привет, мир!" << std::endl;
    
    LinkList list;

    list.add_front(1);
    list.add_back(2);
    list.add_back(3);
    list.add_back(4);
    list.print();
    
    list.flip();
    list.print();


    return 0;
}
