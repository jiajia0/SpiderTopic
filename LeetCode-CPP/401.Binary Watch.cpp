#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    vector<string> readBinaryWatch(int num) {
        vector<int> hours = {1,2,4,8};
        vector<int> minutes = {1,2,4,8,16,32};
        vector<string> result;
        for(int i=0;i<num;i++) {//����hour�Ŀ�����
            result.push_back(hours[i]);
            for(int j=0;j<num-i;j++) {//����mintues�Ŀ�����

            }
        }
        return result;
    }
};

int main() {
    Solution s;
    s.readBinaryWatch(1);
}
