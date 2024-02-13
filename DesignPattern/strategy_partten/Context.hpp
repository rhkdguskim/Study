#ifndef CONTEXT
#define CONTEXT
#include "Strategy.hpp"

class Context
{
    public:
        Context(Strategy*);
        void doAlgorithm();

    private:
        Strategy* _instance;

};
#endif