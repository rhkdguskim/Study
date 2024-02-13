#ifndef STRATEGYB
#define STRATEGYB
#include "Strategy.hpp"

class StrategyB : public Strategy
{
    public:
        StrategyB();
        ~StrategyB();
        virtual void doAlgorithm();
};
#endif