#include "Context.hpp"

Context::Context(Strategy *instance) 
    : _instance(instance)
{

}

void Context::doAlgorithm()
{
    _instance->doAlgorithm();
}
