#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

class Solution {
public:
    int leastBricks(vector<vector<int>>& wall) {
        int maxBrick = wall.size();//���Ĳ��.
        int minBrick = wall.size();//��С�Ĳ�Σ�Ĭ��Ϊ����Ρ�
        unordered_map<int,int> width;//��������ÿ�����ȶ�Ӧ�ĸ�����
        int sum;//����������ߵ�ש�ĳ���
        for(int i = 0; i < wall.size(); i++) {//�ֱ�ѭ��ÿ�㡣
            sum = 0;
            for(int j = 0; j < wall[i].size() - 1; j++) {//�ֱ�Ƚ�ÿ�������ש����Ҫ��ȥ1����Ϊ����Ҫ�����ܵĿ�ȡ�
                sum += wall[i][j];//�õ���ǰ���ת�ĳ��ȡ�
                width[sum]++;//��ǰ��߳�����map��+1.
                //cout << sum << ", ";
                //cout << width[sum] << "\n";
                minBrick = min(minBrick,maxBrick - width[sum]);
            }
            //cout << endl << endl;
        }
        //cout << minBrick;
        return minBrick;
    }
};

int main() {
    Solution s;
    vector<vector<int>> wall;
    vector<int> a1;
    vector<int> a2;
    vector<int> a3;
    vector<int> a4;
    vector<int> a5;
    vector<int> a6;

    /*a1.push_back(1);
    a2.push_back(1);
    a3.push_back(1);*/

    a1.push_back(1);
    a1.push_back(2);
    a1.push_back(2);
    a1.push_back(1);

    a2.push_back(3);
    a2.push_back(1);
    a2.push_back(2);

    a3.push_back(1);
    a3.push_back(3);
    a3.push_back(2);

    a4.push_back(2);
    a4.push_back(4);

    a5.push_back(3);
    a5.push_back(1);
    a5.push_back(2);

    a6.push_back(1);
    a6.push_back(3);
    a6.push_back(1);
    a6.push_back(1);

    wall.push_back(a1);
    wall.push_back(a2);
    wall.push_back(a3);
    wall.push_back(a4);
    wall.push_back(a5);
    wall.push_back(a6);
    s.leastBricks(wall);
}
