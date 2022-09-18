// https://leetcode.com/problems/implement-trie-prefix-tree/
class Trie {
public:
    struct Node {
        Node* nxt[26] = {};
        bool exist = false;
    };
    
    Node* root;
    
    Trie() {
        root = new Node;
    }
    
    void insert(string word) {
        Node* now = root;
        for (char c : word) {
            int x = c - 'a';
            if (now->nxt[x] == nullptr) now->nxt[x] = new Node;
            now = now->nxt[x];
        }
        now->exist = true;
    }
    
    bool search(string word) {
        Node* now = root;
        for (char c : word) {
            int x = c - 'a';
            if (now->nxt[x] == nullptr) return false;
            now = now->nxt[x];
        }
        return now->exist;
    }
    
    bool startsWith(string prefix) {
        Node* now = root;
        for (char c : prefix) {
            int x = c - 'a';
            if (now->nxt[x] == nullptr) return false;
            now = now->nxt[x];
        }
        return true;
    }
};

/**
 * Your Trie object will be instantiated and called as such:
 * Trie* obj = new Trie();
 * obj->insert(word);
 * bool param_2 = obj->search(word);
 * bool param_3 = obj->startsWith(prefix);
 */
