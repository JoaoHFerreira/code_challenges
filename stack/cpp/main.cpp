#include <iostream>
#include <stack>

class Stack {
private:
    std::stack<int> s;

public:
    Stack() {
        std::cout << "Stack initialized\n";
    }

    void push(int value) {
        s.push(value);
        std::cout << "Pushed: " << value << "\n";
    }

    int pop() {
        if (isEmpty()) {
            std::cout << "Stack Underflow\n";
            return -1;
        }
        int val = s.top();
        s.pop();
        std::cout << "Popped: " << val << "\n";
        return val;
    }

    int peek() const {
        if (isEmpty()) {
            std::cout << "Stack is empty\n";
            return -1;
        }
        return s.top();
    }

    bool isEmpty() const {
        return s.empty();
    }

    int size() const {
        return s.size();
    }

    void status() const {
        std::cout << "Top: " << peek() << ", Size: " << size() << "\n";
    }
};


int main() {
    Stack myStack;

    myStack.push(5);
    myStack.push(10);
    myStack.push(15);

    myStack.status();

    myStack.pop();
    myStack.status();

    std::cout << (myStack.isEmpty() ? "Empty\n" : "Not Empty\n");

    return 0;
}
