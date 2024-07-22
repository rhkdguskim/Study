#include <iostream>
#include <string>
#include <unordered_set>
#include <unordered_map>
#include <memory>

using namespace std;

struct TrieNode
{
    unordered_map<char, unique_ptr<TrieNode>> childs;
    bool is_finished = false;
};

class Trie
{
    private:
        unique_ptr<TrieNode> node;
    public:
        Trie()
        {
            node = make_unique<TrieNode>();
        }

        void insert(const string& word)
        {
            TrieNode* cur = node.get();

            for(auto &chr : word)
            {
                if(cur->childs.find(chr) == cur->childs.end())
                {
                    cur->childs[chr] = make_unique<TrieNode>();
                }

                cur = cur->childs[chr].get();
            }

            cur->is_finished = true;   
        }

        bool search(const string& word)
        {
            TrieNode* cur = node.get();

            for(auto &chr : word)
            {
                if(cur->childs.find(chr) == cur->childs.end()) return false;

                cur = cur->childs[chr].get();
            }

            return cur->is_finished;
        }
};

int main()
{

}
