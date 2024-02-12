#include "ComponentInterface.hpp";

class Keyboard : public ComputerPart {
public:
    void accept(ComputerPartVisitor &visitor) override {
        visitor.visit(*this);
    }
};

class Monitor : public ComputerPart {
public:
    void accept(ComputerPartVisitor &visitor) override {
        visitor.visit(*this);
    }
};

class Mouse : public ComputerPart {
public:
    void accept(ComputerPartVisitor &visitor) override {
        visitor.visit(*this);
    }
};

class Computer : public ComputerPart {
    ComputerPart *parts[3];

public:
    Computer() {
        parts[0] = new Keyboard();
        parts[1] = new Monitor();
        parts[2] = new Mouse();
    }

    void accept(ComputerPartVisitor &visitor) override {
        for (auto &part : parts) {
            part->accept(visitor);
        }
        visitor.visit(*this);
    }

    ~Computer() {
        for (auto &part : parts) {
            delete part;
        }
    }
};