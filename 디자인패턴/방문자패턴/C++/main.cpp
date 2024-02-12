#include "ConcreateComponent.hpp"
#include "ConcreateVisitor.hpp"

int main() {
    ComputerPart *computer = new Computer();
    ComputerPartVisitor *visitor = new ComputerPartDisplayVisitor();

    computer->accept(*visitor);

    delete visitor;
    delete computer;

    return 0;
}