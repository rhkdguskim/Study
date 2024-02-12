#ifndef COMPOENT_INTERFACE
#define COMPOENT_INTERFACE

#include <iostream>
using namespace std;

// Forward declaration
class Computer;
class Keyboard;
class Monitor;
class Mouse;

// Visitor Interface
class ComputerPartVisitor {
public:
    virtual void visit(Computer &computer) = 0;
    virtual void visit(Keyboard &keyboard) = 0;
    virtual void visit(Monitor &monitor) = 0;
    virtual void visit(Mouse &mouse) = 0;
    virtual ~ComputerPartVisitor() {}
};

// Element Interface
class ComputerPart {
public:
    virtual void accept(ComputerPartVisitor &visitor) = 0;
    virtual ~ComputerPart() {}
};
#endif