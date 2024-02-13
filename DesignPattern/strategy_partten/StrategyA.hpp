#ifndef STRATEGYA
#define STRATEGYA

#include "Strategy.hpp"
class StrategyA : public Strategy
{
    public:
        StrategyA();
        ~StrategyA();
        virtual void doAlgorithm();
};
#endif