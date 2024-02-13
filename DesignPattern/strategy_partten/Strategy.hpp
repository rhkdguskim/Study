#ifndef STRATEGY
#define STRATEGY

class Strategy
{
    public:
        Strategy();
        virtual ~Strategy() = 0;
        virtual void doAlgorithm() = 0;

};
#endif
