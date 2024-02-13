#include "Context.hpp"
#include "StrategyA.hpp"
#include "StrategyB.hpp"

int main() {
    Context context(new StrategyA());
    Context context2(new StrategyB());

    context.doAlgorithm();
    context2.doAlgorithm();

    return 0;
}