#include "ComponentInterface.hpp"

class ComputerPartDisplayVisitor : public ComputerPartVisitor {
public:
    void visit(Computer &computer) override {
        cout << "Displaying Computer." << endl;
    }

    void visit(Keyboard &keyboard) override {
        cout << "Displaying Keyboard." << endl;
    }

    void visit(Monitor &monitor) override {
        cout << "Displaying Monitor." << endl;
    }

    void visit(Mouse &mouse) override {
        cout << "Displaying Mouse." << endl;
    }
};