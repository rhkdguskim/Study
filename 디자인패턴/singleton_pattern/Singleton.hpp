#ifndef SINGLETON
#define SINGLETON
#include <mutex>
template <typename T>
class Singleton {
public:
    static T* Instance() {
        std::lock_guard<std::mutex> lock(_mutex);
        if (_instance == nullptr) {
            _instance = new T();
        }
        return _instance;
    }

    Singleton(const Singleton&) = delete;
    Singleton& operator=(const Singleton&) = delete;

protected:
    Singleton() {}
    ~Singleton() {}
private:
    static T* _instance;
    static std::mutex _mutex;
};
#endif